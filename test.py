import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from collections import OrderedDict
import Questions

# main widget
class MyWidget(QtWidgets.QWidget):
    question_tracker = 0 # index of current question
    question = 0 # used to index the question of the current question 
    def __init__(self):
        super().__init__()

# ______Button elements_________________________________________
        self.nextbutton = QtWidgets.QPushButton("Next")
        self.prevbutton = QtWidgets.QPushButton("Prev")
        self.answerbutton = QtWidgets.QPushButton("View Answer")

# ______Text elements(Labels)___________________________________
        self.question_on_screen = QtWidgets.QLabel(
            str(Questions.questions.question_list[self.question_tracker]
            [MyWidget.question][int(MyWidget.question)]),
            alignment=QtCore.Qt.AlignCenter)
        self.answer_on_screen = QtWidgets.QLabel("")

#_______Creating layout_________________________________________
        self.layout = QtWidgets.QVBoxLayout(self)

# ______Adding elements to layout_______________________________ 
        self.layout.addWidget(self.question_on_screen)
        self.layout.addWidget(self.answer_on_screen)
        self.layout.addWidget(self.nextbutton)
        self.layout.addWidget(self.prevbutton)
        self.layout.addWidget(self.answerbutton)

# ______Adding functions to buttons_____________________________
        self.nextbutton.clicked.connect(self.question_next)
        self.prevbutton.clicked.connect(self.question_prev)
        self.answerbutton.clicked.connect(self.view_ans)

    def question_index():
        
        pass

    def view_ans(self):
        """Views answer by question to index 1 """
        answer = str(Questions.questions.question_list[self.question_tracker]
        [1]) 
        self.answer_on_screen.setText(f"Answer: {answer}")

        pass

  
    def question_next(self):
        """Adds 1 to the current questions index to change to next question"""
        question_list = Questions.questions.question_list
        if((MyWidget.question_tracker +1 < len(question_list))):
            self.answer_on_screen.setText("click view answer to see answer")
            MyWidget.question_tracker +=1
            question = str(Questions.questions.question_list[self.question_tracker]
            [int(MyWidget.question)])
            self.question_on_screen.setText(f"Question: {question}")
        else:
            return

    def question_prev(self):
        """Subtracts 1 from current question index to go to prev question"""
        if(not(MyWidget.question_tracker-1 < 0)):
            self.answer_on_screen.setText("click view answer to see answer")
            MyWidget.question_tracker -=1
            question = str(Questions.questions.question_list[self.question_tracker]
            [int(MyWidget.question)])
            self.question_on_screen.setText(f"Question: {question}")
    
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())

# Add more comments----done
# find solution to wrongish initial question display
# add a way to dynamically and questions and answer
# .. .. .. .. dynamically delete questions and answers
# maybe change some variable names.