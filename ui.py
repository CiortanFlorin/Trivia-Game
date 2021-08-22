from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface():

    def __init__(self, quiz_brain: QuizBrain):
        #Window
        self.quiz = quiz_brain
        self.windows = Tk()
        self.windows.title("Quizzler")
        self.windows.config(padx=20, pady=20, bg=THEME_COLOR)
        #Canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Some Stuff", font=("Arial", 20, "italic"), fill=THEME_COLOR, width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        #Buttons
        right_img = PhotoImage(file="images/true.png")
        wrong_img = PhotoImage(file="images/false.png")

        self.right_button = Button(width=100, height=97, image=right_img, bg=THEME_COLOR, highlightthickness=0, command= self.right)
        self.right_button.grid(row=2, column=0)

        self.wrong_button = Button(width=100, height=97, image=wrong_img, bg=THEME_COLOR, highlightthickness=0, command= self.wrong)
        self.wrong_button.grid(row=2, column=1)

        #Label
        self.label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.label.grid(row=0, column=1)

        self.next_question()

        self.windows.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the Quizz.")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")
    def right(self):
        self.give_feedback(self.quiz.check_answer("True"))
    def wrong(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.windows.after(1000, self.next_question)
