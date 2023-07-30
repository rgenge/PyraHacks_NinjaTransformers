import tkinter as tk
from tkinter import messagebox

class Quiz:
    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

questions = [
    Quiz("What is the ruling planet of Aries?", "Mars"),
    Quiz("What element is associated with Taurus?", "Earth"),
    Quiz("What is the ruling planet of Gemini?", "Mercury"),
    Quiz("What element is associated with Cancer?", "Water"),
    Quiz("What is the ruling planet of Leo?", "Sun"),
    Quiz("What element is associated with Virgo?", "Earth"),
    Quiz("What is the ruling planet of Libra?", "Venus"),
]

class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("400x200")
        self.title("Astrology Quiz")
        self.question_number = 0
        self.correct_answers = 0
        self.question_label = tk.Label(self)
        self.question_answer= tk.Label(self)
        self.answer_entry = tk.Entry(self)
        self.submit_button = tk.Button(self, text="Submit", command=self.check_answer)
        self.next_button = tk.Button(self, text="Next", command=self.ask_question)
        self.question_label.pack()
        self.answer_entry.pack()
        self.submit_button.pack()
        self.next_button.pack()
        self.question_label.pack()
        self.ask_question()

    def ask_question(self):
        if self.question_number < len(questions):
            self.question_label.config(text=questions[self.question_number].question)
        else:
            messagebox.showinfo("Quiz Finished", f"You answered {self.correct_answers} out of {len(questions)} questions correctly!")
            self.destroy()

    def check_answer(self):
        if self.answer_entry.get().lower() == questions[self.question_number].correct_answer.lower():
            self.correct_answers += 1
            self.question_label.config(text="Correct!")
        else:
            self.question_label.config(text="Incorrect! answer was: " + questions[self.question_number].correct_answer)
        self.answer_entry.delete(0, tk.END)
        self.question_number += 1
if __name__ == "__main__":
    app = Application()
    app.mainloop()
