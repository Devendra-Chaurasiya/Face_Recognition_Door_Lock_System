from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class door:
    def __init__(self, root):
        self.root = root
        self.user_id = 0  # Initialize user_id to 0
        self.root.geometry("1530x790+0+0")
        self.root.title("Door Lock Management System")

        # *******variables**********
        self.var_Use=StringVar()
        self.var_User=StringVar()
        self.var_Name=StringVar()
        self.var_Phone_no=StringVar()
        self.var_Phone_no1=StringVar()
        self.var_Marital_status=StringVar()
        self.var_Aadhaar_no=StringVar()
        self.var_Age=StringVar()
        self.var_DOB=StringVar()
        self.var_Gender=StringVar()
        self.var_Email_id=StringVar()
        self.var_Connection=StringVar()

    #first image
        img=Image.open("download (1).jpg")
        img=img.resize((550,130),Image.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimage)
        f_lbl.place(x=500,y=0,width=500,height=130)

    #first image
        img1=Image.open("images (1).jpg")
        img1=img1.resize((550,130),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimage1)
        f_lbl.place(x=0,y=0,width=500,height=130)

    #third image
        img2=Image.open("images (1).jpg")
        img2=img2.resize((550,130),Image.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimage2)
        f_lbl.place(x=1000,y=0,width=550,height=130)

    #background image

        img3=Image.open("dev.jpg")
        img3=img3.resize((1530,710),Image.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimage3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text=" USER REGISTRATION ",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1500,height=600)

    #left side label frame

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Fill The Details",font=("times new roman",13,"bold"))
        Left_frame.place(x=10,y=10,width=810,height=580)

        img_left=Image.open("student button 1.jpg")
        img_left=img_left.resize((520,130),Image.LANCZOS)
        self.photoimage_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimage_left)
        f_lbl.place(x=50,y=0,width=720,height=130)


        #current course
        info_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="information",font=("times new roman",12,"bold"))
        info_frame.place(x=5,y=135,width=800,height=110)

#use for           1
        use_label=Label(info_frame,text="Use For",font=("times new roman",13,"bold"),bg="white")
        use_label.grid(row=0,column=0,padx=10)
        use_combo=ttk.Combobox(info_frame,textvariable=self.var_Use,font=("times new roman",13,"bold"),state="readonly",width=20)
        use_combo["values"]=("Home Security","Office Use","Attendance Monitoring",)
        use_combo.current(0)
        use_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #current user type  2
        user_label=Label(info_frame,text="User",font=("times new roman",13,"bold"),bg="white")
        user_label.grid(row=0,column=2,padx=10,sticky=W)
        user_combo=ttk.Combobox(info_frame,textvariable=self.var_User,font=("times new roman",13,"bold"),state="readonly",width=20)
        user_combo["values"]=("ALL","Admin","Member")
        user_combo.current(0)
        user_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #current user name  3
        Martial_status_label=Label(info_frame,text="NAME:",font=("times new roman",13,"bold"),bg="white")
        Martial_status_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        Martial_status_entry=ttk.Entry(info_frame,textvariable=self.var_Name,width=20,font=("times new roman",13,"bold"))
        Martial_status_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

    #current email no1    4
        Phone_no_label=Label(info_frame,text="Phone no:",font=("times new roman",13,"bold"),bg="white")
        Phone_no_label.grid(row=1,column=2,padx=10,sticky=W)

        Phone_no_label_entry=ttk.Entry(info_frame,textvariable=self.var_Phone_no,width=20,font=("times new roman",13,"bold"))
        Phone_no_label_entry.grid(row=1,column=3,padx=2,pady=10,sticky=W)

#current class student information
        info_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="User Details",font=("times new roman",12,"bold"))
        info_frame.place(x=5,y=250,width=800,height=300)

#current student ID    5
        Phone_no1_label=Label(info_frame,text="Phone no:",font=("times new roman",13,"bold"),bg="white")
        Phone_no1_label.grid(row=1,column=0,padx=10,sticky=W)

        Phone_no1_entry=ttk.Entry(info_frame,textvariable=self.var_Phone_no1,width=20,font=("times new roman",13,"bold"))
        Phone_no1_entry.grid(row=1,column=1,padx=10,sticky=W)

#student Marital_status   6
        Martial_status_label=Label(info_frame,text="Martial Status",font=("times new roman",13,"bold"),bg="white")
        Martial_status_label.grid(row=1,column=2,padx=10,sticky=W)
        Martial_status_combo=ttk.Combobox(info_frame,textvariable=self.var_Marital_status,font=("times new roman",13,"bold"),state="readonly",width=20)
        Martial_status_combo["values"]=("ALL","Married","Un married")
        Martial_status_combo.current(0)
        Martial_status_combo.grid(row=1,column=3,padx=10,pady=5,sticky=W)

    #student Aadhar_no      7
        Aadhaar_no_label=Label(info_frame,text="Aadhaar no:",font=("times new roman",13,"bold"),bg="white")
        Aadhaar_no_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        Aadhaar_no_label_entry=ttk.Entry(info_frame,textvariable=self.var_Aadhaar_no,width=20,font=("times new roman",13,"bold"))
        Aadhaar_no_label_entry.grid(row=2,column=1,padx=2,pady=10,sticky=W)


    # student age     8

        age_no_label=Label(info_frame,text="Age:",font=("times new roman",13,"bold"),bg="white")
        age_no_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        age_no_label_entry=ttk.Entry(info_frame,textvariable=self.var_Age,width=20,font=("times new roman",13,"bold"))
        age_no_label_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

    # student gender      9

        gender_label=Label(info_frame,text="Gender:",font=("times new roman",13,"bold"),bg="white")
        gender_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        gender_combo=ttk.Combobox(info_frame,textvariable=self.var_Gender,font=("times new roman",13,"bold"),state="readonly",width=20)
        gender_combo["values"]=("Male","Female","Others",)
        gender_combo.current(0)
        gender_combo.grid(row=3,column=3,padx=10,pady=10,sticky=W)


    # student date of birth     10

        dob_label=Label(info_frame,text="DOB:",font=("times new roman",13,"bold"),bg="white")
        dob_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        dob_label_entry=ttk.Entry(info_frame,textvariable=self.var_DOB,width=20,font=("times new roman",13,"bold"))
        dob_label_entry.grid(row=3,column=1,padx=2,pady=5,sticky=W)

    # student email id     11

        email_label=Label(info_frame,text="Email Id:",font=("times new roman",13,"bold"),bg="white")
        email_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        email_label_entry=ttk.Entry(info_frame,textvariable=self.var_Email_id,width=20,font=("times new roman",13,"bold"))
        email_label_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)



        #radio buttons

        self.var_radio1=StringVar()
        radionbtn1=ttk.Radiobutton(info_frame,variable=self.var_radio1,text="Take photo sample",value="YES")
        radionbtn1.grid(row=6,column=0)

        self.var_radio2=StringVar()
        radionbtn2=ttk.Radiobutton(info_frame,variable=self.var_radio1,text="No photo sample",value="NO")
        radionbtn2.grid(row=6,column=1)


    # button frame

        btn_frame=Frame(info_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=20,y=215,width=750,height=36)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=18,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn = Button(btn_frame, text="Update", width=18, font=("times new roman", 13, "bold"), bg="blue", fg="white", command=self.update_data)
        update_btn.grid(row=0, column=1)

        # Bind the delete_data function to the "Delete" button
        delete_btn = Button(btn_frame, text="Delete", width=18, font=("times new roman", 13, "bold"), bg="blue", fg="white", command=self.delete_data)
        delete_btn.grid(row=0, column=2)

        # Bind the reset function to the "Reset" button
        reset_btn = Button(btn_frame, text="Reset", width=18, font=("times new roman", 13, "bold"), bg="blue", fg="white", command=self.reset)
        reset_btn.grid(row=0, column=3)

#    888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        btn_frame1=Frame(info_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=20,y=245,width=750,height=36)

        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=37,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,command=self.update_photo_sample,text="update Photo Sample",width=37,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)



    #right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="",font=("times new roman",13,"bold"))
        Right_frame.place(x=750,y=10,width=720,height=580)

        img_right=Image.open("images (4).jpg")
        img_right=img_right.resize((720,130),Image.LANCZOS)
        self.photoimage_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimage_right)
        f_lbl.place(x=50,y=0,width=720,height=130)


    # %%%%%%%%%%%%% searching system %%%%%%%%%%%%%%%
        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=135,width=710,height=70)

        search_label=Label(search_frame,text="Search By:",font=("times new roman",15,"bold"),bg="red",fg="black")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",13,"bold"),state="readonly",width=15)
        search_combo["values"]=("select","Aadhaar no:","Phone No","Name")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(search_frame,command=self.search_door,text="Search",width=13,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn=Button(search_frame,text="Show All",width=13,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)


#table frame
        table_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        table_frame.place(x=5,y=210,width=710,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.door_table=ttk.Treeview(table_frame,column=("Use","User", "Name", "Phone_no", "Phone_no1", "Aadhaar_no","Marital_status", "Age","DOB","Gender", "Email_id", "Connection","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.door_table.xview)
        scroll_y.config(command=self.door_table.yview)


        self.door_table.heading("Use",text="Use")
        self.door_table.heading("User",text="User")
        self.door_table.heading("Name",text="Name")
        self.door_table.heading("Phone_no",text="Phone no")
        self.door_table.heading("Phone_no1",text="Phone no1")
        self.door_table.heading("Marital_status",text="Marital status")
        self.door_table.heading("Aadhaar_no",text="Aadhaar no")
        self.door_table.heading("Age",text="Age")
        self.door_table.heading("DOB",text="DOB")
        self.door_table.heading("Gender",text="Gender")
        self.door_table.heading("Email_id",text="Email id")
        self.door_table.heading("Connection",text="Connection")
        self.door_table.heading("photo",text="PhotoSampleStatus")
        self.door_table["show"]="headings"

        self.door_table.column("Use",width=100)
        self.door_table.column("User",width=100)
        self.door_table.column("Name",width=100)
        self.door_table.column("Phone_no",width=100)
        self.door_table.column("Phone_no1",width=100)
        self.door_table.column("Marital_status",width=100)
        self.door_table.column("Aadhaar_no",width=100)
        self.door_table.column("Name",width=100)
        self.door_table.column("Age",width=100)
        self.door_table.column("DOB",width=100)
        self.door_table.column("Gender",width=100)
        self.door_table.column("Email_id",width=100)
        self.door_table.column("Connection",width=100)
        self.door_table.column("photo",width=150)

        self.door_table.pack(fill=BOTH,expand=1)
        self.door_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


    #*****************function decleration**************

    def add_data(self):
        if (
            self.var_User.get() == "select User"
            or self.var_Name.get() == ""
            or self.var_Use.get() == ""
        ):
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                host="Host Name",
                user="root",
                password="Your Mysql Password",
                database="face_recognizer"
            )
                my_cursor = conn.cursor()

         

                # Insert data into the database
                my_cursor.execute("INSERT INTO door (`Use`, `User`, Name, Phone_no, Phone_no1, Marital_status, Aadhaar_no, Age, DOB, Gender, Email_id, Connection) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (
                        self.var_Use.get(),
                        self.var_User.get(),
                        self.var_Name.get(),
                        self.var_Phone_no.get(),
                        self.var_Phone_no1.get(),
                        self.var_Marital_status.get(),
                        self.var_Aadhaar_no.get(),
                        self.var_Age.get(),
                        self.var_DOB.get(),
                        self.var_Gender.get(),
                        self.var_Email_id.get(),
                        self.var_Connection.get(),
                    ),
                )


                conn.commit()
                self.fetch_data()
                messagebox.showinfo(
                    "success", "Passenger details have been added successfully", parent=self.root
                )
            except Exception as es:
                messagebox.showerror("Error", f"Error adding data: {str(es)}", parent=self.root)


#****************************Fetch data********************************
    def fetch_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="ASDC200220042", database="face_recognizer")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM door")
            data = my_cursor.fetchall()

            if len(data) != 0:
                self.door_table.delete(*self.door_table.get_children())
                for row in data:
                    self.door_table.insert('', END, values=row)
            conn.commit()
            conn.close()  # Close the connection
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching data: {str(e)}", parent=self.root)

#*********************************grt cursor*********************
    def get_cursor(self, event=""):
        cursor_focus = self.door_table.focus()  # Update to self.door_table
        content = self.door_table.item(cursor_focus)
        data = content["values"]

        self.var_Use.set(data[0])
        self.var_User.set(data[1])
        self.var_Name.set(data[2])
        self.var_Phone_no.set(data[3])
        self.var_Phone_no1.set(data[4])
        self.var_Marital_status.set(data[5])
        self.var_Aadhaar_no.set(data[6])
        self.var_Age.set(data[7])
        self.var_DOB.set(data[8])
        self.var_Gender.set(data[9])
        self.var_Email_id.set(data[10])
        self.var_Connection.set(data[11])
        self.var_radio1.set(data[12])



    # update function9
    # Update function
    def update_data(self):
        if self.var_Use.get() == "select Use" or self.var_User.get() == "" or self.var_Name.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do You Want To Update This Passenger's Details", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="ASDC200220042", database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("UPDATE door SET `Use`=%s, `User`=%s, `Name`=%s, `Phone_no`=%s, `Phone_no1`=%s, `Marital_status`=%s, `Aadhaar_no`=%s, `Age`=%s, `DOB`=%s, `Gender`=%s, `Email_id`=%s, `Connection`=%s, `PhotoSample`=%s WHERE `Aadhaar_no`=%s", (
                                        self.var_Use.get(),
                                        self.var_User.get(),
                                        self.var_Name.get(),
                                        self.var_Phone_no.get(),
                                        self.var_Phone_no1.get(),
                                        self.var_Marital_status.get(),
                                        self.var_Aadhaar_no.get(),
                                        self.var_Age.get(),
                                        self.var_DOB.get(),
                                        self.var_Gender.get(),
                                        self.var_Email_id.get(),
                                        self.var_Connection.get(),
                                        self.var_radio1.get(),
                                        self.var_Aadhaar_no.get()  # Use Aadhaar_no as a unique identifier
                                    ))

                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success", "Passenger details successfully updated", parent=self.root)
                else:
                    if not Update:
                        return
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)


                # Function to delete a student record
    def delete_data(self):
        selected_row = self.door_table.focus()  # Get the selected row
        data = self.door_table.item(selected_row)
        aadhaar_no = data["values"][6]  # Assuming Aadhaar_no is in the 7th column

        if aadhaar_no:
            confirm_delete = messagebox.askyesno("Confirm Deletion", "Do you want to delete this passenger's record?")
            if confirm_delete:
                try:
                    conn = mysql.connector.connect(host="localhost", username="root", password="ASDC200220042", database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("DELETE FROM door WHERE Aadhaar_no=%s", (aadhaar_no,))
                    conn.commit()
                    conn.close()
                    self.fetch_data()  # Refresh the table
                    messagebox.showinfo("Success", "Passenger's record deleted successfully", parent=self.root)
                except Exception as es:
                    messagebox.showerror("Error", f"Error deleting record: {str(es)}", parent=self.root)
        else:
            messagebox.showerror("Error", "Please select a passenger record to delete", parent=self.root)

    # Function to reset input fields
    def reset(self):
        self.var_Use.set("select Use")
        self.var_User.set("select User")
        self.var_Name.set("select Name")
        self.var_Phone_no.set("select Phone_no")
        self.var_Phone_no1.set("")
        self.var_Marital_status.set("")
        self.var_Aadhaar_no.set("")
        self.var_Age.set("")
        self.var_DOB.set("Male")
        self.var_Gender.set("")
        self.var_Email_id.set("")
        self.var_Connection.set("")
        self.var_radio1.set("NO")

# ============= Generate data set Take photo Samples   ============
    # Function to generate dataset by capturing face samples
    def generate_dataset(self):
            if self.var_Use.get() == "select Use" or self.var_User.get() == "" or self.var_Aadhaar_no.get() == "":
                messagebox.showerror("Error", "All Fields are required", parent=self.root)
            else:
                try:
                    conn = mysql.connector.connect(host="localhost", username="root", password="ASDC200220042",
                                                database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("SELECT * FROM door")
                    myresult = my_cursor.fetchall()
                    id = 0
                    for x in myresult:
                        id += 1

                    face_classifier = cv2.CascadeClassifier(
                        "C:\\Users\\91914\\Desktop\\Face_Recognition_System\\haarcascade_frontalface_default.xml")

                    def face_cropped(img):
                        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                        faces = face_classifier.detectMultiScale(gray, 1.3, 5)

                        for (x, y, w, h) in faces:
                            face_cropped = img[y:y + h, x:x + w]
                            return face_cropped
                        
                    ip_address = 'http://192.168.43.159:8080/video'
                    cap = cv2.VideoCapture(0)
                    img_id = 0
                    while True:
                        ret, my_frame = cap.read()
                        if face_cropped(my_frame) is not None:
                            img_id += 1
                            face = cv2.resize(face_cropped(my_frame), (450, 450))
                            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                            file_name_path = f"data/user.{str(id)}.{str(img_id)}.jpg"
                            cv2.imwrite(file_name_path, face)
                            cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                            cv2.imshow("Cropped Face", face)

                        if cv2.waitKey(1) == 13 or int(img_id) == 100:
                            break

                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Result", "Generating data sets completed!!!!")
                except Exception as es:
                    messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)



    # Function to update the photo sample for the selected student
    def update_photo_sample(self):
        selected_row = self.door_table.focus()  # Get the selected row
        data = self.door_table.item(selected_row)
        aadhaar_no = data["values"][6]  # Assuming Aadhaar_no is in the 7th column

        if aadhaar_no:
            try:
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y + h, x:x + w]
                        return face_cropped

                ip_address = 'http://192.168.43.148:8080/video'
                cap = cv2.VideoCapture(ip_address)
                img_id = 0

                while True:
                    ret, my_frame = cap.read()

                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = f"data/user.{str(aadhaar_no)}.{str(img_id)}.jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Updated Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Updated photo sample saved successfully")
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)
        else:
            messagebox.showerror("Error", "Please select a passenger record to update the photo sample", parent=self.root)
# Function to search for a student by Roll No or Phone No
    def search_door(self):
        if self.var_search.get() != "":
            conn = mysql.connector.connect(host="localhost", username="root", password="ASDC200220042",
                                        database="face_recognizer")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM door WHERE Name=%s OR Phone_no=%s", (self.var_search.get(), self.var_search.get()))
            data = my_cursor.fetchall()
            if len(data) == 0:
                messagebox.showinfo("Info", "No record found", parent=self.root)
            else:
                self.door_table.delete(*self.door_table.get_children())
                for i in data:
                    self.door_table.insert("", END, values=i)
                conn.commit()
            conn.close()
        else:
            messagebox.showerror("Error", "Please enter Name  or Phone No to search", parent=self.root)
    # Function to display all records
    def show_all(self):
        self.fetch_data()

if __name__ == "__main__":
    root = Tk()
    obj = door(root)
    root.mainloop()