from tkinter import *

class MathQuiz:
    def __init__(self,parent):

        self.Questions = Frame(parent)
        self.Questions.grid(row=0, column=1)

        self.QuestionsLabel = Label(self.Questions, text = "Quiz Questions",
                                    bg = "black", fg = "white", width = 20, padx = 30, pady = 10,
                                    font = ("Time", "14", "bold italic"))
        self.QuestionsLabel.grid(columnspan=2)
        self.HomeButton = Button(self.Questions, text = "Next")
        self.HomeButton.grid(row = 8, column = 1)

if __name__ == "__main__":
    root = Tk()
    frames = MathQuiz(root)
    root.title("Quiz")
    root.mainloop()

    
