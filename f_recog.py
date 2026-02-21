import cv2
import mysql.connector
from datetime import datetime
import os
import pandas as pd
from tkinter import messagebox

def f_recog():
    try:
        face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        if not os.path.exists("classifier.xml"):
            messagebox.showerror("Error", "Classifier file missing! Train your faces first.")
            return
        clf.read("classifier.xml")  # trained LBPH classifier

        # Connect to database
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="student_data"
        )
        cursor = conn.cursor()

        attendance_list = []  # store tuples: (Name, Roll, Division, Date, Time, Status)
        recognized_ids = set()  # to track already marked students

        cap = cv2.VideoCapture(0)
        font = cv2.FONT_HERSHEY_SIMPLEX

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in faces:
                face_roi = gray[y:y+h, x:x+w]
                face_id, conf = clf.predict(face_roi)

                # Only accept good matches
                if conf < 60:
                    cursor.execute(
                        "SELECT Name, Roll_No, Division, Enrollment FROM student_data WHERE Attendance_ID=%s",
                        (str(face_id),)
                    )
                    result = cursor.fetchone()
                    if result:
                        name, roll, division, enrollment = result
                        label = f"{name} | Roll:{roll} | Div:{division}"
                        color = (0, 255, 0)
                        status = "Present"

                        # Add to attendance only once
                        if enrollment not in recognized_ids:
                            now = datetime.now()
                            attendance_list.append((
                                name, roll, division,
                                now.strftime("%Y-%m-%d"),
                                now.strftime("%H:%M:%S"),
                                status
                            ))
                            recognized_ids.add(enrollment)
                    else:
                        label = f"{name} | Roll:{roll} | Div:{division}"
                        color = (0, 0, 255)
                else:
                    label = "Unknown"
                    color = (0, 0, 255)

                cv2.rectangle(frame, (x, y), (x+w, y+h), color, 3)
                cv2.putText(frame, label, (x, y-10), font, 0.8, color, 2)

            cv2.imshow("Attendance - Press ENTER to exit", frame)
            if cv2.waitKey(1) == 13:  # Enter key
                break

        cap.release()
        cv2.destroyAllWindows()
        conn.close()

        # Save attendance if any student recognized
        if attendance_list:
            os.makedirs("Attendance_Records", exist_ok=True)
            filename = f"Attendance_Records/Attendance_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
            df = pd.DataFrame(attendance_list, columns=["Name", "Roll_No", "Division", "Date", "Time", "Status"])
            df.to_csv(filename, index=False)
            messagebox.showinfo("Success", f"Attendance Saved!\n{filename}")
        else:
            messagebox.showinfo("Info", "No recognized students.")

    except Exception as e:
        messagebox.showerror("Error", str(e))