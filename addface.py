from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
import cv2
import os
import numpy as np
from PIL import Image
import sys

class AddFace:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1700x1080")
        self.root.configure(bg="lightblue")
        sys.setrecursionlimit(2000)

        # Variables
        self.var_attend_id = StringVar()
        self.var_enrollment = StringVar()
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_Cource = StringVar()
        self.var_Year = StringVar()
        self.var_division = StringVar()

        # Title
        title = Label(self.root, text="Student Management System", font=("Garamond", 25, "bold"), bg="lightblue")
        title.pack(side=TOP, fill=X, pady=10)

        # Main Frame
        main_frame = Frame(self.root, bd=2, relief=RIDGE)
        main_frame.place(x=10, y=90, width=1280, height=560)

        # Left Frame for Input
        left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details", font=("Garamond", 14, "bold"), fg="red")
        left_frame.place(x=10, y=10, width=600, height=530)

        # Right Frame for Table
        right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Table", font=("Garamond", 14, "bold"), fg="red")
        right_frame.place(x=570, y=10, width=650, height=530)

        # =================== Left Frame Inputs ===================
        Label(left_frame, text="Attendance ID:", font=("Garamond", 12)).grid(row=0, column=0, padx=5, pady=5, sticky=W)
        Entry(left_frame, textvariable=self.var_attend_id, font=("Garamond", 12)).grid(row=0, column=1, padx=5, pady=5)

        Label(left_frame, text="Enrollment No:", font=("Garamond", 12)).grid(row=1, column=0, padx=5, pady=5, sticky=W)
        Entry(left_frame, textvariable=self.var_enrollment, font=("Garamond", 12)).grid(row=1, column=1, padx=5, pady=5)

        Label(left_frame, text="Roll No:", font=("Garamond", 12)).grid(row=2, column=0, padx=5, pady=5, sticky=W)
        Entry(left_frame, textvariable=self.var_roll, font=("Garamond", 12)).grid(row=2, column=1, padx=5, pady=5)

        Label(left_frame, text="Name:", font=("Garamond", 12)).grid(row=3, column=0, padx=5, pady=5, sticky=W)
        Entry(left_frame, textvariable=self.var_name, font=("Garamond", 12)).grid(row=3, column=1, padx=5, pady=5)

        Label(left_frame, text="Course:", font=("Garamond", 12)).grid(row=4, column=0, padx=5, pady=5, sticky=W)
        course_combo = ttk.Combobox(left_frame, textvariable=self.var_Cource, state="readonly", font=("Garamond", 12), width=20)
        course_combo["values"] = ("Select Branch", "Computer", "Mechanical", "Civil", "Chemical")
        course_combo.current(0)
        course_combo.grid(row=4, column=1, padx=5, pady=5)

        Label(left_frame, text="Year:", font=("Garamond", 12)).grid(row=5, column=0, padx=5, pady=5, sticky=W)
        year_combo = ttk.Combobox(left_frame, textvariable=self.var_Year, state="readonly", font=("Garamond", 12), width=20)
        year_combo["values"] = ("Select Year", "First Year", "Second Year", "Third Year")
        year_combo.current(0)
        year_combo.grid(row=5, column=1, padx=5, pady=5)

        Label(left_frame, text="Division:", font=("Garamond", 12)).grid(row=6, column=0, padx=5, pady=5, sticky=W)
        div_combo = ttk.Combobox(left_frame, textvariable=self.var_division, state="readonly", font=("Garamond", 12), width=20)
        div_combo["values"] = ("Select Division", "A", "B")
        div_combo.current(0)
        div_combo.grid(row=6, column=1, padx=5, pady=5)

        # Buttons Frame inside left_frame (using grid)
        btn_frame = Frame(left_frame)
        btn_frame.grid(row=7, column=0, columnspan=2, pady=10, padx=5)

        Button(btn_frame, text="Save", width=12, command=self.add_student, bg="blue", fg="white", font=("Garamond", 12, "bold")).grid(row=0, column=0, padx=5, pady=5)
        Button(btn_frame, text="Update", width=12, command=self.update_student, bg="green", fg="white", font=("Garamond", 12, "bold")).grid(row=0, column=1, padx=5, pady=5)
        Button(btn_frame, text="Delete", width=12, command=self.delete_student, bg="red", fg="white", font=("Garamond", 12, "bold")).grid(row=1, column=0, padx=5, pady=5)
        Button(btn_frame, text="Reset", width=12, command=self.reset_data, bg="orange", fg="white", font=("Garamond", 12, "bold")).grid(row=1, column=1, padx=5, pady=5)

        Button(btn_frame, text="Add Photo Sample", width=25, command=self.create_dataset, bg="purple", fg="white", font=("Garamond", 12, "bold")).grid(row=2, column=0, columnspan=2, padx=5, pady=5)
        Button(btn_frame, text="Train Face Classifier", width=25, command=self.train_classifier, bg="brown", fg="white", font=("Garamond", 12, "bold")).grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        # =================== Right Frame Table ===================
        table_frame = Frame(right_frame, bd=2, relief=RIDGE)
        table_frame.pack(fill=BOTH, expand=1)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(table_frame, columns=("Attendance_ID", "Enrollment", "RollNo", "Name", "Course", "Year", "Division"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        for col in ("Attendance_ID", "Enrollment", "RollNo", "Name", "Course", "Year", "Division"):
            self.student_table.heading(col, text=col)
            self.student_table.column(col, width=100)

        self.student_table["show"] = "headings"
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.auto_attendance_id()
        self.fetch_data()

    # =================== Functions ===================
    def auto_attendance_id(self):
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="root", database="Student_data")
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM student_data")
            count = cursor.fetchone()[0] + 1
            self.var_attend_id.set(f"ATT{count:03d}")
            conn.close()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def add_student(self):
        if self.var_enrollment.get() == "" or self.var_roll.get() == "" or self.var_name.get() == "" or \
           self.var_Cource.get() == "Select Branch" or self.var_Year.get() == "Select Year" or self.var_division.get() == "Select Division":
            messagebox.showerror("Error", "All Fields are Required")
            return
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="root", database="Student_data")
            cursor = conn.cursor()
            cursor.execute("""INSERT INTO student_data (Attendance_ID, Enrollment, Roll_No, Name, Course, Year, Division)
                              VALUES (%s,%s,%s,%s,%s,%s,%s)""",
                           (self.var_attend_id.get(), self.var_enrollment.get(), self.var_roll.get(),
                            self.var_name.get(), self.var_Cource.get(), self.var_Year.get(), self.var_division.get()))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Student Added Successfully")
            self.fetch_data()
            self.reset_data()
        except mysql.connector.IntegrityError:
            messagebox.showerror("Error", "Enrollment already exists!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def fetch_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="root", database="Student_data")
            cursor = conn.cursor()
            cursor.execute("SELECT Attendance_ID, Enrollment, Roll_No, Name, Course, Year, Division FROM student_data")
            rows = cursor.fetchall()
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("", END, values=row)
            conn.close()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        row = content["values"]
        if row:
            self.var_attend_id.set(row[0])
            self.var_enrollment.set(row[1])
            self.var_roll.set(row[2])
            self.var_name.set(row[3])
            self.var_Cource.set(row[4])
            self.var_Year.set(row[5])
            self.var_division.set(row[6])

    def update_student(self):
        if self.var_enrollment.get() == "":
            messagebox.showerror("Error", "Select a student to update")
            return
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="root", database="Student_data")
            cursor = conn.cursor()
            cursor.execute("""UPDATE student_data SET Attendance_ID=%s, Roll_No=%s, Name=%s, Course=%s, Year=%s, Division=%s
                              WHERE Enrollment=%s""",
                           (self.var_attend_id.get(), self.var_roll.get(), self.var_name.get(),
                            self.var_Cource.get(), self.var_Year.get(), self.var_division.get(), self.var_enrollment.get()))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Student Updated Successfully")
            self.fetch_data()
            self.reset_data()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete_student(self):
        if self.var_enrollment.get() == "":
            messagebox.showerror("Error", "Select a student to delete")
            return
        try:
            delete = messagebox.askyesno("Delete", "Do you want to delete this student?")
            if delete:
                conn = mysql.connector.connect(host="localhost", user="root", password="root", database="Student_data")
                cursor = conn.cursor()
                cursor.execute("DELETE FROM student_data WHERE Enrollment=%s", (self.var_enrollment.get(),))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Student Deleted Successfully")
                self.fetch_data()
                self.reset_data()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def reset_data(self):
        self.var_enrollment.set("")
        self.var_roll.set("")
        self.var_name.set("")
        self.var_Cource.set("Select Branch")
        self.var_Year.set("Select Year")
        self.var_division.set("Select Division")
        self.auto_attendance_id()

    # =================== Face Dataset ===================
    def create_dataset(self):
        if self.var_enrollment.get() == "" or self.var_name.get() == "":
            messagebox.showerror("Error", "Select a student")
            return
        try:
            face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

            def face_cropped(img):
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    return gray[y:y+h, x:x+w]

            cap = cv2.VideoCapture(0)
            img_id = 0
            os.makedirs("Face_Dataset", exist_ok=True)

            while True:
                ret, frame = cap.read()
                if face_cropped(frame) is not None:
                    img_id += 1
                    face = cv2.resize(face_cropped(frame), (450, 450))
                    cv2.imwrite(f"Face_Dataset/{self.var_enrollment.get()}.{img_id}.jpg", face)
                    cv2.putText(face, str(img_id), (50,50), cv2.FONT_HERSHEY_COMPLEX, 2, (0,255,0), 2)
                    cv2.imshow("Cropped Face", face)
                if cv2.waitKey(1) == 13 or img_id == 100:
                    break

            cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo("Result", f"Dataset Generated for {self.var_name.get()}")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def train_classifier(self):
        try:
            data_dir = "Face_Dataset"
            path = [os.path.join(data_dir, f) for f in os.listdir(data_dir)]

            faces = []
            ids = []

            for image in path:
                img = Image.open(image).convert("L")
                imageNp = np.array(img, "uint8")
                enrollment_id = int(image.split(".")[0].split(".")[0][-3:]) if image.split(".")[0][-3:].isdigit() else 0
                faces.append(imageNp)
                ids.append(enrollment_id)
                cv2.imshow("Training", imageNp)
                cv2.waitKey(1)

            ids = np.array(ids)
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.train(faces, ids)
            clf.write("classifier.xml")
            cv2.destroyAllWindows()
            messagebox.showinfo("Result", "Training Completed")
        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = Tk()
    app = AddFace(root)
    root.mainloop()