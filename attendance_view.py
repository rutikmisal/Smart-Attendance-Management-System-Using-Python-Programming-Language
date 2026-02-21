from tkinter import *
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import sys

class AttendanceView:
    def __init__(self, root):
        self.root = root
        self.root.title("View Attendance")
        self.root.state('zoomed')
        self.root.configure(bg="lightblue")
        sys.setrecursionlimit(2000)

        title = Label(root, text="View Attendance", font=("Garamond", 35, "bold"), bg="lightblue")
        title.pack(side=TOP, fill=X)

        main_frame = Frame(root, bd=2, bg="lightblue")
        main_frame.pack(fill=BOTH, expand=1, padx=10, pady=10)

        scroll_x = ttk.Scrollbar(main_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(main_frame, orient=VERTICAL)

        self.attendance_table = ttk.Treeview(main_frame,
                                             columns=("Name", "Course", "Year", "Enrollment", "Roll_no", "Date", "Time", "Status"),
                                             xscrollcommand=scroll_x.set,
                                             yscrollcommand=scroll_y.set,
                                             show="headings")
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.attendance_table.xview)
        scroll_y.config(command=self.attendance_table.yview)

        for col, width in zip(["Name", "Course", "Year", "Enrollment", "Roll_no", "Date", "Time", "Status"],
                              [200, 100, 100, 150, 100, 120, 120, 100]):
            self.attendance_table.heading(col, text=col)
            self.attendance_table.column(col, width=width, anchor="center")
        self.attendance_table.pack(fill=BOTH, expand=1)

        Button(root, text="Load Attendance CSV", command=self.load_csv,
               bg="blue", fg="white", font=("Garamond", 15, "bold")).pack(pady=10)

    def load_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            try:
                df = pd.read_csv(file_path)
                self.attendance_table.delete(*self.attendance_table.get_children())
                for index, row in df.iterrows():
                    self.attendance_table.insert("", "end", values=(row["Name"], row["Course"], row["Year"],
                                                                    row["Enrollment"], row["Roll_no"],
                                                                    row["Date"], row["Time"], row["Status"]))
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load CSV:\n{e}")


if __name__ == "__main__":
    root = Tk()
    app = AttendanceView(root)
    root.mainloop()