from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import sys
import os

class Developers:
    def __init__(self, root):
        self.root = root
        self.root.title("About Developers")
        self.root.state('zoomed')  # Maximize window
        self.root.configure(bg="lightblue")
        sys.setrecursionlimit(2000)

        # Background Image
        bg_path = os.path.join("program_images", "bvp.jpeg")
        bg_image = Image.open(bg_path)
        self.bg_image_resized = bg_image.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image_resized)
        bg_label = Label(self.root, image=self.bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Title
        title_label = Label(self.root, text="About Developers", font=("Garamond", 35, "bold"), bg="white", fg="black")
        title_label.pack(fill=X, pady=20)

        # Developer Frame
        dev_frame = Frame(self.root, bg="lightblue")
        dev_frame.pack(fill=BOTH, expand=1, padx=50, pady=50)

        # Developer info: (image_path, name, info)
        developers = [
            ("kanak.jpeg", "Kanak Hiran", "Role: Tester \nEmail: kanakhiran@gmail.com"),
            ("Rutik.jpeg", "Rutik Misal", "Role: Frontend & Backend Developer\nEmail: rutikmisal1982@gmail.com"),
            ("Rohan.jpeg", "Rohan Vaggu", "Role: Designer\nEmail: rohanvaggu2416@gmail.com"),
            ("suyash.jpeg", "Suyash Waykar", "Role: QA Engineer\nEmail: suyashwaykar@gmail.com")
        ]

        self.photo_images = []
        for i, (img_file, name, info) in enumerate(developers):
            img_path = os.path.join("program_images", img_file)
            img = Image.open(img_path)
            img = img.resize((200, 200), Image.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            self.photo_images.append(photo)

            # Button with image + command
            btn = Button(dev_frame, image=photo, cursor="hand2",
                         command=lambda n=name, inf=info: self.show_info(n, inf))
            btn.grid(row=0, column=i, padx=30, pady=10)

            # Label below the image
            lbl = Label(dev_frame, text=name, font=("Garamond", 15, "bold"), bg="lightblue")
            lbl.grid(row=1, column=i, pady=10)

    def show_info(self, name, info):
        messagebox.showinfo(f"{name} Info", info)


if __name__ == "__main__":
    root = Tk()
    obj = Developers(root)
    root.mainloop()