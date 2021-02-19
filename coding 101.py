from tkinter import *
from tkinter import ttk
from random import *

class MathQuiz:
    def __init__(self,parent):
        self.welcome = Frame(parent)
        self.welcome.grid(row=0, column=0)
        self.TitleLabel = Label(self.welcome, text = "Welcome to Maths Quiz",
                            bg = "black", fg = "white", width = 20, padx = 30, pady = 10,
                            font = ("Time", "14", "bold italic"))
        self.TitleLabel.grid(columnspan = 2)
        self.NextButton = ttk.Button(self.welcome, text = "Next", command = self.show_Questions)
        self.NextButton.grid(row = 8, column = 1)
        self.Questions = Frame(parent)
        self.QuestionsLabel = Label(self.Questions, text = "Quiz selection",
                                    bg = "black", fg = "white", width = 20, padx = 30, pady = 10,
                                    font = ("Time", "14", "bold italic"))
        self.difficultyLabel = Label(self.Questions)
        self.IntroLabel = Label(self.Questions, text = "This program helps younger student practice", fg = "black", padx = 10, pady = 10,
                            font = ("Time", "10", "bold italic"))
        self.WarningLabel = Label(self.Questions)
        self.problem = Frame(parent)
        self.problemLabel = Label(self.problem, text = "Quiz Questions", bg = "black", fg = "white", width = 25, padx = 30, pady = 10,
                                    font = ("Time", "14", "bold italic"))
        self.Problems = Label(self.problem, text = "", padx = 10, pady = 10)


    def show_Welcome(self):
        self.Questions.grid_remove()
        self.problem.grid_remove()
        self.welcome.grid()
    
    def show_Questions(self):
        self.welcome.grid_remove()
        self.Questions.grid()
        self.QuestionsLabel.grid(columnspan=2)
        self.Questions.grid(row=0, column=1)
        self.HomeButton = ttk.Button(self.Questions, text = "Home", command = self.show_Welcome)
        self.HomeButton.grid(row = 9, column =0)
        self.next_button = ttk.Button(self.Questions, text = "Next", command = self.maths_questions)
        self.next_button.grid(row = 9, column = 1)
        self.IntroLabel.grid(row = 2, column =0)
        self.NameLabel = Label(self.Questions, text = "Name", anchor = W , fg = "black", width = 25, padx = 30, pady = 10,
                            font = ("Time", "14", "bold italic"))
        self.NameLabel.grid(row = 3, column = 0)
        self.NameEntry = ttk.Entry(self.Questions, width = 15)
        self.NameEntry.grid(row = 3, column = 1)
        self.AgeLabel = Label(self.Questions, text = "Age", anchor = W , fg = "black", width = 30, padx = 30, pady = 10,
                            font = ("Time", "14", "bold italic"))
        self.AgeLabel.grid(row = 4, column = 0)
        self.AgeLabel.grid(columnspan=2)
        self.AgeEntry = ttk.Entry(self.Questions, width = 15)
        self.AgeEntry.grid(row = 4, column = 1)
        self.difficultyLabel.grid(row=4, column =0)
        self.difficulty = ["Easy","Medium","Hard"]
        self.diff_lvl = StringVar()
        self.diff_lvl.set(0)
        self.diff_btns = []

        for i in range(len(self.difficulty)):
            rb = Radiobutton(self.Questions, variable = self.diff_lvl, value = i, text = self.difficulty[i],
                         anchor = W, padx = 50, width = "5", height = "2")
            self.diff_btns.append(rb)
            rb.grid(row = i+5, column = 0, sticky = W)

        try:
            if self.NameEntry.get() == "":
                self.WarningLabel.configure(text = "Enter name")
                self.NameEntry.focus()

            elif self.NameEntry.get().isalpha == False:
                self.WarningLabel.configure(text = "Enter text")
                self.NameEntry.delete(0,END)
                self.NameEntry.focus()
                
            elif self.AgeEntry.get() == "":
                self.WarningLabel.configure(text = "Enter age")
                self.AgeEntry.focus()

            elif int(self.NameEntry.get()) > 12:
                 self.WarningLabel.configure(text = "Old Boomer")
                 self.AgeEntry.delete(0,END)
                 self.AgeEntry.focus()

            elif int(self.NameEntry.get()) < 0:
                 self.WarningLabel.configure(text = "Just no.")
                 self.AgeEntry.delete(0,END)
                 self.AgeEntry.focus()

            elif int(self.NameEntry.get()) > 5:
                 self.WarningLabel.configure(text = "Too young")
                 self.AgeEntry.delete(0,END)
                 self.AgeEntry.focus()
            
            else:
                self.Welcome.grid_remove()
                self.Questions.grid_remove()
                self.maths_questions.grid()

        except ValueError:
            self.WarningLabel.configure(text = "Please enter a number")
            self.AgeEntry.delete(0,END)
            self.AgeEntry.focus()

    def maths_questions(self):
        self.welcome.grid_remove()
        self.Questions.grid_remove()
        self.problem.grid()
        self.problemLabel.grid(row = 0, column = 1, columnspan=2)
        self.HomeButton = ttk.Button(self.problem, text = "Home", command = self.show_Welcome)
        self.HomeButton.grid(row = 3, column =1)
        self.next_button = ttk.Button(self.problem, text = "Next", command = self.maths_questions)
        self.next_button.grid(row = 3, column = 2)
    
        if self.diff_lvl.get() == "0":
            x = randrange(10)
            y = randrange(10)
            self.answer = x + y
            question_text =str(x) + " + " + str(y) + "  = "
            self.Problems.configure(text = question_text)
            self.Problems.grid(row = 2, column = 1)

        elif self.diff_lvl.get() == "1":
            x = randrange(10)
            y = randrange(15)
            self.answer = 1.5 * x + 1.5 * y
            question_text = str(1.5 * x)  + " + " + str( 1.5 * y)  + "  = "
            self.Problems.configure(text = question_text)
            self.Problems.grid(row = 2, column = 1)

        else:
            x = randrange(20)
            y = randrange(398)
            z = randrange(413)
            self.answer = 2 * x + 2 * y + z
            question_text = str(2 * x) + " + " + str( 2 * y) + " + " + str(z) + " = "           
            self.Problems.configure(text = question_text)
            self.Problems.grid(row = 2, column = 1)
    
if __name__ == "__main__":
    root = Tk()
    frames = MathQuiz(root)
    root.title("Quiz")
    root.mainloop()



    
