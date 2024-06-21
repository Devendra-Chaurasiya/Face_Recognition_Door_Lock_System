import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from bcrypt import hashpw, gensalt
import mysql.connector
from datetime import datetime

class SignupPage:
    def __init__(self, parent):
        self.parent = parent
        self.parent.withdraw()  # Hide the main app window temporarily

        self.signup_window = tk.Toplevel(parent)
        self.signup_window.geometry("1530x790+0+0")
        self.signup_window.title("Signup")

        # Load the background image for the signup page
        img = Image.open("1000_F_119115529_mEnw3lGpLdlDkfLgRcVSbFRuVl6sMDty (1).jpg")  # Replace with the actual path to your image
        img = img.resize((1500, 790), Image.LANCZOS)
        self.background_image = ImageTk.PhotoImage(img)

        # Create a canvas to display the background image
        self.canvas = tk.Canvas(self.signup_window, width=600, height=400)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, anchor="nw", image=self.background_image)

        # Connect to the database
        self.connection = mysql.connector.connect(
                host="Host Name",
                user="root",
                password="Your Mysql Password",
                database="face_recognizer"
            )
        self.cursor = self.connection.cursor(dictionary=True)

        # Increased font size for labels and buttons
        label_font = ("Arial", 20)
        entry_font = ("Arial", 18)
        button_font = ("Arial", 20, "bold")

        self.label_username = tk.Label(self.signup_window, text="Username:", font=label_font, bg="white")
        self.entry_username = tk.Entry(self.signup_window, font=entry_font, bg="lightgray")
        self.label_password = tk.Label(self.signup_window, text="Password:", font=label_font, bg="white")
        self.entry_password = tk.Entry(self.signup_window, show="*", font=entry_font, bg="lightgray")
        self.label_dob = tk.Label(self.signup_window, text="Date of Birth:", font=label_font, bg="white")
        self.entry_dob = tk.Entry(self.signup_window, font=entry_font, bg="lightgray")
        self.label_email = tk.Label(self.signup_window, text="Email:", font=label_font, bg="white")
        self.entry_email = tk.Entry(self.signup_window, font=entry_font, bg="lightgray")
        self.label_phone = tk.Label(self.signup_window, text="Phone No.:", font=label_font, bg="white")
        self.entry_phone = tk.Entry(self.signup_window, font=entry_font, bg="lightgray")

        self.button_signup = tk.Button(self.signup_window, text="Signup", bg="#007bff", fg="white", command=self.signup, font=button_font)

        # Calculate the center coordinates
        center_x = (self.signup_window.winfo_screenwidth() - 600) // 2
        center_y = (self.signup_window.winfo_screenheight() - 400) // 2

        # Place widgets at the center
        self.label_username.place(x=center_x, y=center_y + 50)
        self.entry_username.place(x=center_x + 150, y=center_y + 50)
        self.label_password.place(x=center_x, y=center_y + 100)
        self.entry_password.place(x=center_x + 150, y=center_y + 100)
        self.label_dob.place(x=center_x, y=center_y + 150)
        self.entry_dob.place(x=center_x + 200, y=center_y + 150)
        self.label_email.place(x=center_x, y=center_y + 200)
        self.entry_email.place(x=center_x + 150, y=center_y + 200)
        self.label_phone.place(x=center_x, y=center_y + 250)
        self.entry_phone.place(x=center_x + 150, y=center_y + 250)
        self.button_signup.place(x=center_x + 150, y=center_y + 300, width=100)

        self.signup_window.protocol("WM_DELETE_WINDOW", self.on_closing)

    def signup(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        dob_str = self.entry_dob.get()
        email = self.entry_email.get()
        phone = self.entry_phone.get()

        if not username or not password or not dob_str or not email or not phone:
            messagebox.showwarning("Empty Fields", "Please fill in all the details.")
            return

        try:
            # Convert the date string to a datetime object
            dob = datetime.strptime(dob_str, "%d/%m/%Y").strftime("%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Invalid Date", "Please enter a valid date in the format DD/MM/YYYY.")
            return

        # Check if the username already exists
        self.cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        existing_user = self.cursor.fetchone()

        if existing_user:
            messagebox.showerror("Signup Failed", "Username already exists. Please choose another username.")
        else:
            # Insert user details into the database
            hashed_password = hashpw(password.encode('utf-8'), gensalt())
            self.cursor.execute("INSERT INTO users (username, password, dob, email, phone) VALUES (%s, %s, %s, %s, %s)",
                                (username, hashed_password, dob, email, phone))
            self.connection.commit()
            messagebox.showinfo("Signup Successful", "Signup successful! Please log in.")

    def on_closing(self):
        self.parent.deiconify()  # Show the main app window
        self.signup_window.destroy()


if __name__ == '__main__':
    root = tk.Tk()
    app = SignupPage(root)
    root.mainloop()