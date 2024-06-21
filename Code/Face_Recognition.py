import os
import time
from datetime import datetime
import csv
from threading import Thread
import cv2
from tkinter import *
from PIL import Image, ImageTk
import mysql.connector
from queue import Queue

class face_recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face_Recognition_System")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open("Facial-Recognition.jpg")
        img_top = img_top.resize((650, 700), Image.LANCZOS)
        self.photoimage4 = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimage4)
        f_lbl.place(x=0, y=55, width=650, height=700)

        img_bottom = Image.open("/facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        img_bottom = img_bottom.resize((950, 700), Image.LANCZOS)
        self.photoimage5 = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimage5)
        f_lbl.place(x=650, y=55, width=950, height=700)

        b1_1 = Button(self.root, text="Face Recognition", cursor="hand2", font=("times new roman", 18, "bold"), bg="red", fg="white", command=self.start_recognition)
        b1_1.place(x=1035, y=650, width=200, height=40)

        # URL of the IP Webcam stream
        self.camera = cv2.VideoCapture(0) # Replace 'your_phone_ip_address' with your phone's IP address

        self.last_save_timestamps = {}

        # Queue for frame processing
        self.frame_queue = Queue(maxsize=1)

        # Flag to control the recognition loop
        self.recognition_active = False

        # Start the camera thread
        self.camera_thread = Thread(target=self.capture_frames)
        self.camera_thread.start()

    def capture_frames(self):
        while True:
            ret, frame = self.camera.read()

            if ret:
                if not self.frame_queue.full():
                    self.frame_queue.put(frame)
                else:
                    # Skip frame if queue is full
                    self.frame_queue.get()
                    self.frame_queue.put(frame)

    def start_recognition(self):
        # Start the recognition thread
        self.recognition_active = True
        recognition_thread = Thread(target=self.recognize)
        recognition_thread.start()

    def recognize(self):
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        recognizer.read('trainer.yml')

        font = cv2.FONT_HERSHEY_SIMPLEX

        while self.recognition_active:
            if not self.frame_queue.empty():
                frame = self.frame_queue.get()

                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = faceCascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

                for (x, y, w, h) in faces:
                    roiGray = gray[y:y+h, x:x+w]
                    id_, conf = recognizer.predict(roiGray)

                    if conf < 95:
                        user_info = self.get_user_info(id_)

                        if user_info is not None and self.can_save_record(id_):
                            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                            cv2.putText(frame, f"User: {user_info['User']}, Name: {user_info['Name']}", (x, y-10), font, 0.9, (0, 255, 0), 2)
                            # Save the recognized face details to the record.csv file
                            self.save_to_csv(user_info)
                            # Update last save timestamp
                            self.last_save_timestamps[id_] = time.time()

                    else:
                        # Unknown face detected
                        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
                        cv2.putText(frame, "Unknown Person", (x, y-10), font, 0.9, (0, 0, 255), 2)
                        # Save unknown face
                        self.save_unknown_face(frame)


                cv2.imshow('frame', frame)
                key = cv2.waitKey(1)

                if key == 27:
                    self.recognition_active = False

        # Release the camera and close all OpenCV windows
        self.camera.release()
        cv2.destroyAllWindows()

    def save_unknown_face(self, face_image):
        unknown_folder = r"C:\Users\91914\Desktop\Face_Recognition_System\unknown"
        if not os.path.exists(unknown_folder):
            os.makedirs(unknown_folder)

        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        unknown_face_filename = os.path.join(unknown_folder, f"{timestamp}.jpg")

        cv2.imwrite(unknown_face_filename, face_image)
        print(f"Unknown face saved as: {unknown_face_filename}")

    def can_save_record(self, user_id):
        # Check if the user's timestamp exists and if 2 minutes have passed
        return user_id not in self.last_save_timestamps or time.time() - self.last_save_timestamps[user_id] >= 120

    def get_user_info(self, id_):
        try:
            connection = mysql.connector.connect(
                host="Host Name",
                user="root",
                password="Your Mysql Password",
                database="face_recognizer"
            )

            cursor = connection.cursor(dictionary=True)
            # Convert id_ to int before using it in the query
            cursor.execute(f"SELECT * FROM door WHERE User={int(id_)}")
            user_info = cursor.fetchone()

            return user_info

        except Exception as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            connection.close()

    def save_to_csv(self, user_info):
        try:
            # Get current date and time
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

            # Create or open the CSV file in append mode
            with open('record.csv', 'a', newline='') as file:
                writer = csv.writer(file)

                # Write header if the file is empty
                if os.path.getsize('record.csv') == 0:
                    writer.writerow(['Timestamp', 'User', 'Name', 'Aadhaar_no', 'Age', 'Gender', 'Email_id'])

                # Convert integer values to strings before writing to CSV
                writer.writerow([timestamp, str(user_info['User']), user_info['Name'], str(user_info['Aadhaar_no']), str(user_info['Age']), user_info['Gender'], user_info['Email_id']])

        except Exception as e:
            print(f"Error saving to CSV: {e}")

if __name__ == "__main__":
    root = Tk()
    obj = face_recognition(root)
    root.mainloop()