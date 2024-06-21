import os
import numpy as np
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import cv2
import mysql.connector

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face_Recognition_System")
        self.path = 'data'  # Make 'path' a class attribute
        self.db = mysql.connector.connect(
            host="host Nmae",
            user="root",
            password="Your Password",
            database="face_recognizer"
        )

        title_lbl = Label(self.root, text=" TRAIN DATA SET ", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open("TrainingDevelopment.jpg")
        img_top = img_top.resize((1530, 325), Image.LANCZOS)
        self.photoimage4 = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimage4)
        f_lbl.place(x=0, y=55, width=1530, height=325)

        b1_1 = Button(self.root, text="SCAN DATA", command=self.train_classifier, cursor="hand2",
                      font=("times new roman", 30, "bold"), bg="red", fg="white")
        b1_1.place(x=0, y=380, width=1530, height=60)

        img_bottom = Image.open("60e7ffd92eb4126a297b610da07cfe22.jpg")
        img_bottom = img_bottom.resize((1530, 325), Image.LANCZOS)
        self.photoimage5 = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimage5)
        f_lbl.place(x=0, y=440, width=1530, height=325)

    def train_classifier(self):
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

        def get_images_and_labels(path):
            image_paths = [os.path.join(path, f) for f in os.listdir(path)]
            face_samples = []
            ids = []

            for image_path in image_paths:
                PIL_img = Image.open(image_path).convert('L')
                img_numpy = np.array(PIL_img, 'uint8')

                # Extracting user_id from the filename
                _, user_id, img_id = os.path.splitext(os.path.basename(image_path))[0].split('.')
                user_id = int(user_id)

                faces = detector.detectMultiScale(img_numpy)

                for (x, y, w, h) in faces:
                    face_samples.append(img_numpy[y:y + h, x:x + w])
                    ids.append(user_id)

            return face_samples, ids

        print("\n [INFO] Training faces. It will take a few seconds. Wait ...")

        faces, ids = get_images_and_labels(self.path)
        recognizer.train(faces, np.array(ids))

        recognizer.write('trainer.yml')
        print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))

def main():
    root = Tk()
    obj = Train(root)
    root.mainloop()

if __name__ == "__main__":
    main()