import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import random
import string
from bcrypt import hashpw, gensalt
import mysql.connector

class ForgotPasswordPage:
    def __init__(self, parent):
        self.parent = parent
        self.parent.withdraw()  # Hide the main app window temporarily

        self.forgot_password_window = tk.Toplevel(parent)
        self.forgot_password_window.geometry("1530x790+0+0")  # Set the same size as LoginPage
        self.forgot_password_window.title("Forgot Password")

        img = Image.open("1000_F_119115529_mEnw3lGpLdlDkfLgRcVSbFRuVl6sMDty (1).jpg")
        img = img.resize((1500, 790), Image.LANCZOS)
        self.background_image = ImageTk.PhotoImage(img)

        self.canvas = tk.Canvas(self.forgot_password_window, width=500, height=300)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, anchor="nw", image=self.background_image)

        # Calculate the center coordinates
        center_x = (self.forgot_password_window.winfo_screenwidth() - 500) // 2
        center_y = (self.forgot_password_window.winfo_screenheight() - 300) // 2

        # Increased font size for labels and buttons
        heading_font = ("Arial", 24, "bold")
        label_font = ("Arial", 16)
        entry_font = ("Arial", 14)
        button_font = ("Arial", 16, "bold")

        # Adding a heading
        self.label_heading = tk.Label(self.forgot_password_window, text="Forgot Password", font=heading_font, bg="white")
        self.label_heading.place(x=center_x + 100, y=center_y - 20)

        self.label_email = tk.Label(self.forgot_password_window, text="Enter your email:", font=label_font)
        self.entry_email = tk.Entry(self.forgot_password_window, font=entry_font)
        self.button_send_email = tk.Button(self.forgot_password_window, text="Send Email", bg="#007bff", fg="white", command=self.send_email, font=button_font)

        self.label_email.place(x=center_x, y=center_y + 50)
        self.entry_email.place(x=center_x + 175, y=center_y + 50)
        self.button_send_email.place(x=center_x + 150, y=center_y + 100)
        self.forgot_password_window.protocol("WM_DELETE_WINDOW", self.on_closing)

    def send_email(self):
        email = self.entry_email.get()

        if email:
            # Connect to the database
            connection = mysql.connector.connect(
                host="Host Name",
                user="root",
                password="Your Mysql Password",
                database="face_recognizer"
            )
            cursor = connection.cursor(dictionary=True)

            # Check if the email exists in the database
            cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
            user = cursor.fetchone()

            if user:
                # Generate a new random password
                new_password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))

                # Update the password in the database
                hashed_password = hashpw(new_password.encode('utf-8'), gensalt())
                cursor.execute("UPDATE users SET password = %s WHERE email = %s", (hashed_password, email))
                connection.commit()

                # Send the new password to the user's email
                self.send_password_email(email, new_password)

                messagebox.showinfo("Password Reset", "A new password has been sent to your email.")
                self.forgot_password_window.destroy()
            else:
                messagebox.showerror("Email Not Found", "The provided email address is not registered.")
        else:
            messagebox.showwarning("Email Required", "Please enter your email address.")

    def send_password_email(self, to_email, new_password):
        # Replace these placeholder values with your actual Gmail address and App Password
        smtp_username = "Your Gmail Address"  # Your Gmail address
        smtp_password = "Your Password"  # Your App Password

        # Configure email server settings
        smtp_server = "smtp.gmail.com"  # Gmail SMTP server address
        smtp_port = 587

        # Create the email message
        subject = "Password Reset"
        body = f"Your new password is: {new_password}"

        message = MIMEMultipart()
        message['From'] = smtp_username
        message['To'] = to_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(smtp_username, to_email, message.as_string())

    def on_closing(self):
        self.parent.deiconify()  # Show the main app window
        self.forgot_password_window.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    app = ForgotPasswordPage(root)
    root.mainloop()