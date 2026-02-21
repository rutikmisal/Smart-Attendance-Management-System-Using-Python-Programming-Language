from tkinter import *
from PIL import Image, ImageTk
import sys

class HelpAndSupport:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition Attendance System")
        self.root.state('zoomed')  # maximize window
        self.root.configure(bg="lightblue")
        sys.setrecursionlimit(2000)

        # ===== Background Image =====
        bg_image = Image.open("program_images/support_bg.jpeg")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        bg_image = bg_image.resize((screen_width, screen_height), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = Label(self.root, image=self.bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # ===== Title =====
        title = Label(self.root, text="HELP AND SUPPORT", font=("Garamond", 40, "bold"), fg="white", bg="black")
        title.pack(pady=20, fill=X)

        # ===== Info Text =====
        info_text = ("For any problem related Attendance System\n"
                     "Contact or report problem to the following email or phone number:")
        info_label = Label(self.root, text=info_text, font=("Garamond", 25, "bold"), fg="black", bg="lightblue", justify=CENTER)
        info_label.pack(pady=40)

        # ===== Contact Info =====
        contact_text = ("Email: rohanvaggu2416@gmail.com\n"
                        "rutikmisal1982@gmail.com\n"
                        "Contact: 8669061913 / 9822994330")
        contact_label = Label(self.root, text=contact_text, font=("Garamond", 30, "bold"), fg="black", bg="lightblue", justify=CENTER)
        contact_label.pack(pady=30)

def main():
    root = Tk()
    app = HelpAndSupport(root)
    root.mainloop()

if __name__ == "__main__":
    main()