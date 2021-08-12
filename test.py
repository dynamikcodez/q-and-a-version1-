import sys
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush, QFont
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
import Questions

class MainWindow(QWidget):
    question_tracker = 0 # index of current question
    question = 0 # used to index the question of the current question 
    def __init__(self):
       QWidget.__init__(self)
       self.setWindowTitle("My App")
       self.setGeometry(100,100,1000,800)

       oImage = QImage("background.jpg")

       sImage = oImage.scaled(QSize(rect.width(),rect.height()))      
       #sImage = oImage.scaled(QSize(1366,768))                   # resize Image to widgets size
       palette = QPalette()
       palette.setBrush(QPalette.Window, QBrush(sImage))                        
       self.setPalette(palette)

       self.label = QLabel('Test', self)                        # test, if it's really backgroundimage
       self.label.setGeometry(50,50,200,50)

    # ______Button elements_________________________________________
       self.nextbutton = QtWidgets.QPushButton("Next")
       self.prevbutton = QtWidgets.QPushButton("Prev")
       self.answerbutton = QtWidgets.QPushButton("View Answer")
       self.nextbutton.move(500,500)

    # ______Text elements(Labels)___________________________________
       self.question_on_screen = QtWidgets.QLabel(
            str(Questions.questions.question_list[self.question_tracker]
            [MainWindow.question][int(MainWindow.question)]),
            alignment=QtCore.Qt.AlignCenter)
       self.question_on_screen.setFont(QFont('Arial', 30))

       self.answer_on_screen = QtWidgets.QLabel("")
       self.answer_on_screen.setFont(QFont('Arial', 10))

    #_______Creating layout_________________________________________
       self.layout = QtWidgets.QGridLayout(self)

    # ______Adding elements to layout_______________________________ 
       self.layout.addWidget(QtWidgets.QLabel(""),0,1)
       self.layout.addWidget(self.question_on_screen,1,1)
       self.layout.addWidget(self.answer_on_screen,2,1)
       self.layout.addWidget(self.nextbutton,3,2)
       self.layout.addWidget(self.prevbutton,3,0)
       self.layout.addWidget(self.answerbutton,3,1)

    # ______Adding functions to buttons_____________________________
       self.nextbutton.clicked.connect(self.question_next)
       self.prevbutton.clicked.connect(self.question_prev)
       self.answerbutton.clicked.connect(self.view_ans)

       self.nextbutton.move(500,500)
       self.show()

    def question_index():
        
        pass

    def view_ans(self):
        """Views answer by question to index 1 """
        answer = str(Questions.questions.question_list[self.question_tracker]
        [1]) 
        question = str(Questions.questions.question_list[self.question_tracker]
        [int(MainWindow.question)])
        self.question_on_screen.setText(f"Question: {question}\n\nAnswer: {answer}")
        #self.answer_on_screen.setText(f"Answer: {answer}")

        pass

  
    def question_next(self):
        """Adds 1 to the current questions index to change to next question"""
        question_list = Questions.questions.question_list
        if((MainWindow.question_tracker +1 < len(question_list))):
            self.answer_on_screen.setText(" ")
            MainWindow.question_tracker +=1
            question = str(Questions.questions.question_list[self.question_tracker]
            [int(MainWindow.question)])
            self.question_on_screen.setText(f"Question: {question}")
        else:
            return

    def question_prev(self):
        """Subtracts 1 from current question index to go to prev question"""
        if(not(MainWindow.question_tracker-1 < 0)):
            self.answer_on_screen.setText(" ")
            MainWindow.question_tracker -=1
            question = str(Questions.questions.question_list[self.question_tracker]
            [int(MainWindow.question)])
            self.question_on_screen.setText(f"Question: {question}")
    


       

if __name__ == "__main__":

    app = QApplication(sys.argv)
    screen = app.primaryScreen()
    #print('Screen: %s' % screen.name())
    size = screen.size()  
    rect = screen.availableGeometry()
    oMainwindow = MainWindow()
    sys.exit(app.exec_())