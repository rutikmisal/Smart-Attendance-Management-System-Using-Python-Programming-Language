from tkinter import *
from tkinter import ttk
import sys

class Chatbot:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition Attendance System")
        self.root.state('zoomed')  # Maximize window
        self.root.configure(bg="lightblue")
        sys.setrecursionlimit(2000)

        self.var_question = StringVar()

        # Chat Frame
        chatbox = LabelFrame(root, bd=2, relief=RIDGE, text="Chat Bot", font=("Garamond", 14, "bold"), fg="red", bg="lightblue")
        chatbox.pack(fill=BOTH, expand=1, padx=10, pady=10)

        # Chat History Text
        self.chat_history = Text(chatbox, bd=1, relief=RIDGE, font=("Arial", 12), wrap=WORD, state='disabled')
        self.chat_history.pack(fill=BOTH, expand=1, padx=10, pady=(10,0))

        # Scrollbar for chat history
        scrollbar = Scrollbar(self.chat_history)
        self.chat_history.config(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=RIGHT, fill=Y)
        scrollbar.config(command=self.chat_history.yview)

        # Question Combobox
        qn_frame = Frame(chatbox, bg="lightblue")
        qn_frame.pack(fill=X, pady=10)

        qn = ttk.Combobox(qn_frame, state="readonly", width=60, textvariable=self.var_question, font=("Arial", 15))
        qn["values"] = (
            "Select Question",
            "How does facial recognition work?",
            "What is machine learning?",
            "What is your name?",
            "What is Python programming?",
            "Where can we use face recognition systems?",
            "Why is face recognition attendance system better than manual attendance?",
            "What are the advantages and disadvantages of face recognition attendance system?",
            "Who created you?",
            "Can I use this system offline?",
            "How many students can be tracked?",
            "How to improve recognition accuracy?",
            "What is LBPH?",
            "What is a classifier in face recognition?",
            "How is attendance stored?",
            "What camera specifications are recommended?",
            "Is this system secure?"
        )
        qn.current(0)
        qn.pack(side=LEFT, padx=10, fill=X, expand=1)

        # Send Button
        send = Button(qn_frame, text="Send", font=("Arial", 15, "bold"), bg="blue", fg="white", command=self.send_message)
        send.pack(side=LEFT, padx=5)

        # Clear Chat Button
        clear_btn = Button(qn_frame, text="Clear Chat", font=("Arial", 15, "bold"), bg="red", fg="white", command=self.clear_chat)
        clear_btn.pack(side=LEFT, padx=5)

        # Predefined responses (more descriptive)
        self.responses = {
            "How does facial recognition work?": (
                "Facial recognition works by analyzing facial features such as the distance between the eyes, nose shape, and jawline. "
                "The system captures an image and converts it to a numerical representation. "
                "It then compares the image with stored faces in the database and calculates a similarity score. "
                "Modern systems use deep learning to improve accuracy and handle variations like lighting, expressions, and angles. "
                "This method is used for security, authentication, and automated attendance."
            ),
            "What is machine learning?": (
                "Machine learning is a branch of AI that allows computers to learn from data without explicit programming. "
                "It uses algorithms to detect patterns, make predictions, and improve over time with more data. "
                "Machine learning is used in face recognition, recommendation systems, natural language processing, and more. "
                "It enables automation and smarter decision-making in various applications."
            ),
            "What is your name?": (
                "I am a chatbot designed for the Face Recognition Attendance System. "
                "My purpose is to answer questions related to the system, its functionalities, and technical aspects. "
                "You can ask me about installation, features, and how the system works in detail. "
                "I am here to help users understand the system and solve common queries effectively."
            ),
            "What is Python programming?": (
                "Python is a high-level programming language known for its simplicity and readability. "
                "It supports multiple programming paradigms like procedural, object-oriented, and functional programming. "
                "Python is widely used in web development, data science, AI, and machine learning. "
                "Its extensive libraries make it suitable for projects like face recognition attendance systems."
            ),
            "Where can we use face recognition systems?": (
                "Face recognition systems are used in schools, colleges, and workplaces for automated attendance. "
                "They are also deployed in security systems, banking, airports, and retail analytics. "
                "Other uses include smartphone authentication, time tracking, and access control. "
                "These systems improve accuracy, save time, and prevent manual errors in recording data."
            ),
            "Why is face recognition attendance system better than manual attendance?": (
                "Face recognition attendance systems eliminate the need for manual roll calls, reducing human error. "
                "They prevent proxy attendance and buddy punching. "
                "Automation speeds up the process and allows real-time monitoring. "
                "Attendance records are stored digitally, making reporting and analysis easier. "
                "Overall, it improves efficiency, security, and accuracy."
            ),
            "What are the advantages and disadvantages of face recognition attendance system?": (
                "Advantages: High accuracy, time-saving, secure, and automated attendance. "
                "It prevents fraudulent attendance and reduces manual work. "
                "Disadvantages: Privacy concerns, dependency on lighting, and occasional recognition errors. "
                "Proper setup, multiple face samples, and regular updates improve reliability."
            ),
            "Who created you?": (
                "I was created by developer Rohan Vaggu. "
                "I am programmed to help users understand the Facial Recognition Attendance System, "
                "answer common questions, and provide guidance on usage and troubleshooting."
            ),
            "Can I use this system offline?": (
                "Yes, the system can work offline. "
                "All face data and attendance records are stored locally in a database. "
                "No internet is required for recognition or marking attendance, ensuring privacy and reliability."
            ),
            "How many students can be tracked?": (
                "The system can track hundreds of students depending on database size and hardware. "
                "Adding more students may require retraining the model for accuracy. "
                "It is scalable for medium to large classrooms with proper optimization."
            ),
            "How to improve recognition accuracy?": (
                "Accuracy improves by capturing multiple images of each student from different angles. "
                "Good lighting, proper camera placement, and high-resolution cameras help. "
                "Regular retraining of the model with updated images ensures reliable performance."
            ),
            "What is LBPH?": (
                "LBPH stands for Local Binary Patterns Histogram. "
                "It is a face recognition algorithm that analyzes local patterns in the face. "
                "LBPH is robust to lighting variations and widely used in attendance systems. "
                "It creates histograms of facial features and compares them for identification."
            ),
            "What is a classifier in face recognition?": (
                "A classifier is a trained model that can identify faces based on patterns in the images. "
                "It learns from existing data and predicts the identity of a new face. "
                "In attendance systems, classifiers help determine which student is present accurately."
            ),
            "How is attendance stored?": (
                "Attendance is stored in a local database or CSV file with details like name, roll number, date, and time. "
                "This allows easy tracking, reporting, and exporting of attendance records for analysis and backup."
            ),
            "What camera specifications are recommended?": (
                "A good resolution camera with at least 720p is recommended. "
                "The camera should have proper lighting support and be positioned to capture faces clearly. "
                "High-resolution cameras improve recognition accuracy and reduce errors."
            ),
            "Is this system secure?": (
                "Yes, the system stores data locally, ensuring privacy. "
                "Face images and attendance records are protected in the database. "
                "Only authorized personnel should access the system to maintain security."
            )
        }

    def send_message(self):
        question = self.var_question.get()
        if question == "Select Question":
            return
        answer = self.responses.get(question, "Sorry, I don't understand that question.")
        self.chat_history.config(state='normal')
        self.chat_history.insert(END, f"\nYou: {question}\nBot: {answer}\n")
        self.chat_history.see(END)  # Scroll to bottom
        self.chat_history.config(state='disabled')

    def clear_chat(self):
        self.chat_history.config(state='normal')
        self.chat_history.delete(1.0, END)
        self.chat_history.config(state='disabled')


if __name__ == "__main__":
    root = Tk()
    obj = Chatbot(root)
    root.mainloop()