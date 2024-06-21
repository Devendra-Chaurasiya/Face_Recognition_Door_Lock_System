from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
from railway import door
from train import Train
from Face_Recognition import face_recognition
from tkinter import Tk, Toplevel, Label, Canvas, Scrollbar, Frame, VERTICAL, HORIZONTAL, LEFT, RIGHT, TOP, BOTTOM, X, Y


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


    
    #first image
        img=Image.open("images.jpg")
        img=img.resize((550,130),Image.Resampling.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimage)
        f_lbl.place(x=0,y=0,width=500,height=130)

    #second image
        img1=Image.open("3 (2).jpg")
        img1=img1.resize((550,130),Image.Resampling.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimage1)
        f_lbl.place(x=500,y=0,width=550,height=130)

    #third image
        img2=Image.open("4.jpg")
        img2=img2.resize((550,130),Image.Resampling.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimage2)
        f_lbl.place(x=1000,y=0,width=550,height=130)



    #background image   FACE RECOGNITION DOOR LOCK SYSTEM

        img3=Image.open("dev.jpg")
        img3=img3.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)

        bg_image=Label(self.root,image=self.photoimage3)
        bg_image.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_image,text=" FACE RECOGNITION SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

    #family button
        img4=Image.open("images (3).jpg")
        img4=img4.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimage4=ImageTk.PhotoImage(img4)
        b1=Button(bg_image,image=self.photoimage4,command=self.railway_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)
        b1_1=Button(bg_image,text="family details",command=self.railway_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="red")
        b1_1.place(x=200, y=300, width=220, height=40)
    #detect face button
        img5=Image.open("face detector.jpg")
        img5=img5.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimage5=ImageTk.PhotoImage(img5)
        b1=Button(bg_image,image=self.photoimage5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)
        b1_1=Button(bg_image,text="face detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="red")
        b1_1.place(x=500,y=300,width=220,height=40)
    #attendance button
        img6 = Image.open("attendance.jpg")
        img6 = img6.resize((220, 220), Image.LANCZOS)
        self.photoimage6 = ImageTk.PhotoImage(img6)
        b1 = Button(bg_image, image=self.photoimage6, cursor="hand2", command=self.open_record_file)
        b1.place(x=800, y=100, width=220, height=220)
        b1_1 = Button(bg_image, text="Records", cursor="hand2", command=self.open_record_file, font=("times new roman", 15, "bold"), bg="darkblue", fg="red")
        b1_1.place(x=800, y=300, width=220, height=40)  # Adjusted the y-coordinate to avoid overlap

    #help button
        # Help Desk button
        img7 = Image.open("help.jpg")
        img7 = img7.resize((220, 220), Image.LANCZOS)  # Use LANCZOS resampling
        self.photoimage7 = ImageTk.PhotoImage(img7)
        b1 = Button(bg_image, image=self.photoimage7, cursor="hand2", command=self.show_help_info)
        b1.place(x=1100, y=100, width=220, height=220)
        b1_1 = Button(bg_image, text="HELP DESK", cursor="hand2", command=self.show_help_info, font=("times new roman", 15, "bold"), bg="darkblue", fg="red")
        b1_1.place(x=1100, y=300, width=220, height=40)

#face scanner button
        img8=Image.open("face scanner.jpg")
        img8=img8.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimage8=ImageTk.PhotoImage(img8)
        b1=Button(bg_image,image=self.photoimage8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=380,width=220,height=220)
        b1_1=Button(bg_image,text="Face Scanner",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="red")
        b1_1.place(x=200,y=580,width=220,height=40)
#students photo face button
        img9=Image.open("image.jpg")
        img9=img9.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimage9=ImageTk.PhotoImage(img9)
        b1 = Button(bg_image, image=self.photoimage9, cursor="hand2", command=self.open_student_images)
        b1.place(x=500, y=380, width=220, height=220)
        b1_1 = Button(bg_image, text="image", cursor="hand2", command=self.open_student_images, font=("times new roman", 15, "bold"), bg="darkblue", fg="red")
        b1_1.place(x=500, y=580, width=220, height=40)
        self.student_images_dir = "data"

#developer info button
        #intruder button
        img10 = Image.open("developer.jpg")
        img10 = img10.resize((220, 220), Image.LANCZOS)
        self.photoimage10 = ImageTk.PhotoImage(img10)
        b1 = Button(bg_image, image=self.photoimage10, cursor="hand2", command=self.open_intruder_images)
        b1.place(x=800, y=380, width=220, height=220)
        b1_1 = Button(bg_image, text="Intruder", cursor="hand2", command=self.open_intruder_images, font=("times new roman", 15, "bold"), bg="darkblue", fg="red")
        b1_1.place(x=800, y=580, width=220, height=40)

    #exit face button
        # Exit button
        img11 = Image.open("log out.jpg")
        img11 = img11.resize((220, 220), Image.LANCZOS)  # Use LANCZOS resampling
        self.photoimage11 = ImageTk.PhotoImage(img11)
        b1 = Button(bg_image, image=self.photoimage11, cursor="hand2", command=self.exit_program)
        b1.place(x=1100, y=380, width=220, height=220)
        b1_1 = Button(bg_image, text="EXIT", cursor="hand2", command=self.exit_program, font=("times new roman", 15, "bold"), bg="darkblue", fg="red")
        b1_1.place(x=1100, y=580, width=220, height=40)

    def open_img(self):
        os.startfile("data")
        def doorface_classifier(self):
            data_dir=("data")
            path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
    faces=[]
    ids=[]
        # ******************function buttons*******************************
    def railway_details(self):
        self.new_window=Toplevel(self.root)
        self.app=door(self.new_window)
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=face_recognition(self.new_window)
    def open_record_file(self):
        # Open "record.csv" in Microsoft Word
        os.startfile("record.csv")

    def open_student_images(self):
        if not os.path.exists(self.student_images_dir):
            print("Student images directory not found.")
            return

        student_images_window = Toplevel(self.root)
        student_images_window.title("Student Images")

        # Set the window size and position
        student_images_window.geometry("1530x790+0+0")

        frame = Frame(student_images_window)
        frame.pack(fill=BOTH, expand=YES)

        canvas = Canvas(frame, bd=0, highlightthickness=0)
        hscrollbar = Scrollbar(frame, orient=HORIZONTAL)
        vscrollbar = Scrollbar(frame, orient=VERTICAL)
        hscrollbar.pack(side=BOTTOM, fill=X)
        vscrollbar.pack(side=RIGHT, fill=Y)
        canvas.pack(side=LEFT, fill=BOTH, expand=YES)
        canvas.config(xscrollcommand=hscrollbar.set, yscrollcommand=vscrollbar.set)
        hscrollbar.config(command=canvas.xview)
        vscrollbar.config(command=canvas.yview)

        img_frame = Frame(canvas)
        canvas.create_window((0, 0), window=img_frame, anchor='nw')

        total_width = 0  # To track the total width of images

        for filename in os.listdir(self.student_images_dir):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                img = Image.open(os.path.join(self.student_images_dir, filename))
                img = img.resize((220, 220), Image.LANCZOS)
                photo = ImageTk.PhotoImage(img)
                label = Label(img_frame, image=photo)
                label.photo = photo  # Store a reference to the image to avoid garbage collection
                label.pack(side="left")
                total_width += 220  # Assuming images are 220 pixels wide

        img_frame.update_idletasks()
        canvas.config(scrollregion=(0, 0, total_width, 220))

        student_images_window.mainloop()
    def open_intruder_images(self):
        intruder_images_dir = "unknown"

        if not os.path.exists(intruder_images_dir):
            print("Intruder images directory not found.")
            return

        intruder_images_window = Toplevel(self.root)
        intruder_images_window.title("Intruder Images")

        frame = Frame(intruder_images_window)
        frame.pack(fill=BOTH, expand=YES)

        canvas = Canvas(frame, bd=0, highlightthickness=0)
        hscrollbar = Scrollbar(frame, orient=HORIZONTAL)
        vscrollbar = Scrollbar(frame, orient=VERTICAL)
        hscrollbar.pack(side=BOTTOM, fill=X)
        vscrollbar.pack(side=RIGHT, fill=Y)
        canvas.pack(side=LEFT, fill=BOTH, expand=YES)
        canvas.config(xscrollcommand=hscrollbar.set, yscrollcommand=vscrollbar.set)
        hscrollbar.config(command=canvas.xview)
        vscrollbar.config(command=canvas.yview)

        img_frame = Frame(canvas)
        canvas.create_window((0,0), window=img_frame, anchor='nw')

        for filename in os.listdir(intruder_images_dir):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                img = Image.open(os.path.join(intruder_images_dir, filename))
                img = img.resize((220, 220), Image.LANCZOS)
                photo = ImageTk.PhotoImage(img)
                label = Label(img_frame, image=photo)
                label.photo = photo  # Store a reference to the image to avoid garbage collection
                label.pack(side="left")

        img_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

        intruder_images_window.mainloop()

    def exit_program(self):
        self.root.destroy()

    def show_help_info(self):
        help_info = "Contact No.: 1234567890\nEmail Id: Dev12@gmail.com"
        help_window = Toplevel(self.root)
        help_window.title("Help Desk Information")
        help_window.geometry("1530x790+0+0")  # Set the size of the help window to match the main window

        frame = Frame(help_window)
        frame.place(relx=0.5, rely=0.5, anchor=CENTER)  # Center the frame

        help_label = Label(frame, text=help_info, font=("times new roman", 20, "bold"), bg="white", fg="red")
        help_label.pack(padx=20, pady=20)



if __name__ == "__main__":
     root=Tk()
     obj=Face_Recognition_System(root)
     root.mainloop()