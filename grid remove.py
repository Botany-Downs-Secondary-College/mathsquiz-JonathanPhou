from tkinter import *

class MathQuiz:
    def __init__(self,parent):

        self.welcome = Frame(parent)
        self.welcome.grid(row=0, column=0)

        self.TitleLabel = Label(self.welcome, text = "Welcome to Maths Quiz",
                            bg = "black", fg = "white", width = 20, padx = 30, pady = 10,
                            font = ("Time", "14", "bold italic"))
        self.TitleLabel.grid(columnspan = 2)

        self.NextButton = Button(self.welcome, text = "Next")
        self.NextButton.grid(row = 8, column = 1)
    
        self.Questions = Frame(parent)
        self.Questions.grid(row=0, column=1)

        self.QuestionsLabel = Label(self.Questions, text = "Quiz Questions",
                                    bg = "black", fg = "white", width = 20, padx = 30, pady = 10,
                                    font = ("Time", "14", "bold italic"))
        self.QuestionsLabel.grid(columnspan=2)
        self.HomeButton = Button(self.Questions, text = "Next")
        self.HomeButton.grid(row = 8, column = 1)

    def show_Welcome(self):
        self.Questions.grid_remove()
        self.Welcome.grid()
    
    def show_Questions(self):
        self.Welcomer.grid_remove()
        self.Questions.grid()

if __name__ == "__main__":
    root = Tk()
    frames = MathQuiz(root)
    root.title("Quiz")
    root.mainloop()



    
