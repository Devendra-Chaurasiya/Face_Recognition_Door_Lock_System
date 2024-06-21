import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from bcrypt import checkpw
import mysql.connector
from forgot_password import ForgotPasswordPage
from main import Face_Recognition_System

class LoginPage:
    def __init__(self, parent):
        self.parent = parent
        self.parent.withdraw()

        self.login_window = tk.Toplevel(parent)
        self.login_window.geometry("1530x790+0+0")
        self.login_window.title("Login")

        img = Image.open("1000_F_119115529_mEnw3lGpLdlDkfLgRcVSbFRuVl6sMDty (1).jpg")
        img = img.resize((1500, 790), Image.LANCZOS)
        self.background_image = ImageTk.PhotoImage(img)

        self.canvas = tk.Canvas(self.login_window, width=500, height=300)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, anchor="nw", image=self.background_image)

        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="ASDC200220042",
            database="face_recognizer"
        )
        self.cursor = self.connection.cursor(dictionary=True)

        label_font = ("Arial", 20)
        entry_font = ("Arial", 18)
        button_font = ("Arial", 20, "bold")

        self.label_username = tk.Label(self.login_window, text="Username:", font=label_font, bg="white")
        self.entry_username = tk.Entry(self.login_window, font=entry_font, bg="lightgray")
        self.label_password = tk.Label(self.login_window, text="Password:", font=label_font, bg="white")
        self.entry_password = tk.Entry(self.login_window, show="*", font=entry_font, bg="lightgray")

        self.button_forgot_password = tk.Button(self.login_window, text="Forgot Password", command=self.open_forgot_password, font=button_font)
        self.button_forgot_password.place(x=668, y=425, width=300)

        center_x = (self.login_window.winfo_screenwidth() - 500) // 2
        center_y = (self.login_window.winfo_screenheight() - 300) // 2

        self.label_username.place(x=center_x, y=center_y + 50)
        self.entry_username.place(x=center_x + 150, y=center_y + 50)
        self.label_password.place(x=center_x, y=center_y + 100)
        self.entry_password.place(x=center_x + 150, y=center_y + 100)

        self.button_login = tk.Button(self.login_window, text="Login", bg="#007bff", fg="white", command=self.login, font=button_font)
        self.button_login.place(x=center_x + 150, y=center_y + 200, width=100)

        self.login_window.protocol("WM_DELETE_WINDOW", self.on_closing)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if not username or not password:
            messagebox.showwarning("Empty Fields", "Please fill in all the details.")
            return

        self.cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = self.cursor.fetchone()

        if user and checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
            messagebox.showinfo("Login Successful", "Login successful!")
            self.open_face_recognition_system()
        else:
            messagebox.showerror("Login Failed", "Login unsuccessful. Please check your username and password.")

    def open_forgot_password(self):
        forgot_password_page = ForgotPasswordPage(self.login_window)

    def open_face_recognition_system(self):
        face_recognition_system = Face_Recognition_System(self.login_window)

    def on_closing(self):
        self.parent.deiconify()
        self.login_window.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    app = LoginPage(root)
    root.mainloop()
