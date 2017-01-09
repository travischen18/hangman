import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import HangMan

class HangManGUI(QWidget):

    alphabet = ['A', 'B', 'C', 'D', 'E',
                'F', 'G', 'H', 'I', 'J', 'K',
                'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                'S', 'T', 'U', 'V', 'W', 'X',
                'Y', 'Z']

    def __init__(self):
        self.buttonList = []
        super(HangManGUI, self).__init__()
        
        ThisGame = HangMan.Game()
        self.guessedLetters = ThisGame.getCorrectArray()
        self.word = ThisGame.getWord()

        self.livesCount = ThisGame.getNumLives()
        
        self.initUI()
        
    def initUI(self):
        
        self.generateLetterButtons()
        
        self.setGeometry(300, 300, 600, 450)
        self.setWindowTitle('HangMan')
        self.show()
        
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        pen = QPen(Qt.black, 3, Qt.SolidLine)
        qp.setPen(pen)
        
        #gallows
        qp.drawLine(75, 60, 75, 20)
        qp.drawLine(150, 20, 75, 20)
        qp.drawLine(150, 20, 150, 200)
        
        #head
        if (self.livesCount < 6):
            qp.drawEllipse(60, 60, 30, 30)
        
        #body
        if (self.livesCount < 5):
            qp.drawLine(75, 90, 75, 135)
        
        #left arm
        if (self.livesCount < 4):
            qp.drawLine(75, 105, 50, 100)
            
        #right arm
        if (self.livesCount < 3):
            qp.drawLine(75, 105, 100, 100)
        
        #left leg
        if (self.livesCount < 2):
            qp.drawLine(75, 135, 50, 160)
            
        #right leg
        if (self.livesCount < 1):
            qp.drawLine(75, 135, 100, 160)
        
        
        # letter lines
        qp.drawLine(20, 250, 60, 250)
        qp.drawLine(70, 250, 110, 250)
        qp.drawLine(120, 250, 160, 250)
        qp.drawLine(170, 250, 210, 250)
        qp.drawLine(220, 250, 260, 250)

        # Text

        if (self.guessedLetters[0] == 1):
            qp.drawText(40, 240, self.word[0])
        if (self.guessedLetters[1] == 1):
            qp.drawText(90, 240, self.word[1])
        if (self.guessedLetters[2] == 1):
            qp.drawText(140, 240, self.word[2])
        if (self.guessedLetters[3] == 1):
            qp.drawText(190, 240, self.word[3])
        if (self.guessedLetters[4] == 1):
            qp.drawText(240, 240, self.word[4])


        qp.end()
        
    def drawEllipse(self, event, qp, pen):
        qp.setPen(pen)
        qp.drawEllipse(60, 60, 30, 30)
    
    def generateLetterButtons(self): 
        for num in range (0, 26):
             self.buttonList.append(QPushButton(HangManGUI.alphabet[num], self))
             self.buttonList[num].move(50*(num%9), 300+ (40 * (num // 9)))
             # self.buttonList[num].clicked.connect(self.decrementLives)
             
    
        
    def updateGame(self):
        self.update()
    
    def onButtonClick(self, button):
        button.setEnabled(False)


def main():
    app = QApplication(sys.argv)
    gui = HangManGUI()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()