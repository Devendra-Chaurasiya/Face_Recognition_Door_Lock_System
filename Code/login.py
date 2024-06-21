import tkinter as tk
from PIL import Image, ImageTk
from login_page import LoginPage
from signup_page import SignupPage

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Login and Signup")

        # Load the background image
        img = Image.open("1000_F_119115529_mEnw3lGpLdlDkfLgRcVSbFRuVl6sMDty (1).jpg")  # Replace with the actual path to your image
        img = img.resize((1530, 790), Image.LANCZOS)
        self.background_image = ImageTk.PhotoImage(img)

        # Create a canvas to display the background image
        self.canvas = tk.Canvas(self.root, width=1530, height=790)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, anchor="nw", image=self.background_image)

        # Increased font size for labels and buttons
        button_font = ("Arial", 20, "bold")

        self.button_login = tk.Button(self.root, text="Login", bg="#007bff", fg="white", command=self.open_login_page, font=button_font)
        self.button_signup = tk.Button(self.root, text="Signup", bg="#007bff", fg="white", command=self.open_signup_page, font=button_font)

        # Place buttons
        self.button_login.place(x=800, y=300, width=300)
        self.button_signup.place(x=800, y=400, width=300)

    def open_login_page(self):
        LoginPage(self.root)

    def open_signup_page(self):
        SignupPage(self.root)


if __name__ == '__main__':
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()