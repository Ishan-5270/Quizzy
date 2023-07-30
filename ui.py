from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#765827"

class QuizUI():

    def __init__(self, quiz_brain:QuizBrain):
        # quiz_brain:QuizBrain specified the type of the object 
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzy")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score_label = Label(text=f"Score:", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 
                                                     125, 
                                                     width = 280,
                                                     text="Some question text", 
                                                     fill=THEME_COLOR, 
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)


        true_image = PhotoImage(file="true.png")
        false_image = PhotoImage(file="false.png")
        self.button_check = Button(image=true_image, highlightthickness=0, command= self.is_right_answer_true)
        self.button_check.grid(row=2, column=0)

        self.button_cross = Button(image=false_image, highlightthickness=0, command= self.is_right_answer_false)
        self.button_cross.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()
    
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Your Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've reached the end of the quiz! Your final score is {self.quiz.score}")
            self.button_check.config(state="disabled")
            self.button_cross.config(state="disabled")
            # taps into the command state of the button and diables them 

    
    def is_right_answer_true(self):
        self.user_feedback(self.quiz.check_answer("True"))
        

    def is_right_answer_false(self):
        self.user_feedback(self.quiz.check_answer("False"))


    def user_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")
            # for canvas it is config not item config 
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
        # the second input is the command we want to invoke after 1000 seconds 
