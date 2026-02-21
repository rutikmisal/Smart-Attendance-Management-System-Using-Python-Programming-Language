from tkinter import *
from PIL import Image, ImageTk
from addface import AddFace
from attendance_view import AttendanceView
from f_recog import f_recog
from chatbot import Chatbot
import os
import webbrowser
from developers import Developers
from helpandsupport import HelpAndSupport
from tkinter import messagebox

class FaceRecognitionSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition Attendance System")
        self.root.geometry("1280x1000")
        self.root.resizable(False, False)

        # Background
        try:
            bg = Image.open("program_images/bg10.jpeg").resize((1700,800))
            self.bg_img = ImageTk.PhotoImage(bg)
            Label(self.root, image=self.bg_img).place(x=0,y=0, relwidth=1, relheight=1)
        except:
            self.root.configure(bg="white")

        # Title
        Label(self.root, text="FACE RECOGNITION ATTENDANCE SYSTEM",
              font=("Garamond", 30, "bold"), bg="black", fg="white").pack(fill=X, pady=20)

        # Buttons Frame
        frame1 = Frame(self.root, bg="white")
        frame1.pack(pady=40)
        frame2 = Frame(self.root, bg="white")
        frame2.pack(pady=10)

        # Images
        self.images = {}
        image_paths = {
            "student":"program_images/AddFaceButton.jpeg",
            "attendance":"program_images/TakeAttendanceButton.jpeg",
            "view":"program_images/Checkattendancebutton.jpeg",
            "manual":"program_images/usermanual.jpeg",
            "dev":"program_images/AboutDeveloper.jpeg",
            "chat":"program_images/chatbot.jpeg",
            "help":"program_images/help.jpeg",
            "exit":"program_images/ExitButton.jpeg"
        }

        for key,path in image_paths.items():
            try:
                img = Image.open(path).resize((140,140))
                self.images[key] = ImageTk.PhotoImage(img)
            except:
                self.images[key] = None

        # Row 1
        row1_buttons = [
            ("Student Details", self.images["student"], self.open_student),
            ("Take Attendance", self.images["attendance"], self.start_attendance),
            ("View Attendance", self.images["view"], self.open_attendance),
            ("User Manual", self.images["manual"], self.show_manual)
        ]
        for i,(text,img,cmd) in enumerate(row1_buttons):
            btn = Button(frame1, image=img, text=text if img is None else "", compound=TOP, command=cmd, cursor="hand2")
            btn.grid(row=0, column=i, padx=30)
            Label(frame1, text=text, font=("Arial",12,"bold"), bg="white").grid(row=1,column=i)

        # Row 2
        row2_buttons = [
            ("Help & Support", self.images["help"], self.open_help),
            ("Chat Bot", self.images["chat"], self.open_chat),
            ("About Developers", self.images["dev"], self.open_developers),
            ("Exit", self.images["exit"], self.exit_system)
        ]
        for i,(text,img,cmd) in enumerate(row2_buttons):
            btn = Button(frame2, image=img, text=text if img is None else "", compound=TOP, command=cmd, cursor="hand2")
            btn.grid(row=0, column=i, padx=30)
            Label(frame2, text=text, font=("Arial",12,"bold"), bg="white").grid(row=1,column=i)

    # Functions
    def open_student(self):
        new_window = Toplevel(self.root)
        AddFace(new_window)

    def start_attendance(self):
        f_recog()

    def open_attendance(self):
        new_window = Toplevel(self.root)
        AttendanceView(new_window)

    def open_chat(self):
        new_window = Toplevel(self.root)
        Chatbot(new_window)

    def open_help(self):
        new_window = Toplevel(self.root)
        HelpAndSupport(new_window)

    def open_developers(self):
        new_window = Toplevel(self.root)
        Developers(new_window)

    def show_manual(self):
        pdf_path = "IJCRT2402465.pdf"
        if os.path.exists(pdf_path):
            webbrowser.open(pdf_path)
        else:
            messagebox.showerror("Error", "User manual not found!")

    def exit_system(self):
        if messagebox.askyesno("Exit","Do you want to exit?"):
            self.root.destroy()


if __name__=="__main__":
    root=Tk()
    app = FaceRecognitionSystem(root)
    root.mainloop()