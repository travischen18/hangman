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
        
        self.ThisGame = HangMan.Game()
        
        self.guessedLetters = self.ThisGame.getCorrectArray()
        self.word = self.ThisGame.getWord()
        self.livesCount = self.ThisGame.getNumLives()
        self.gameState = self.ThisGame.getGameState()

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
    
    def generateLetterButtons(self): 
        for num in range (0, 26):
             self.buttonList.append(QPushButton(HangManGUI.alphabet[num], self))
             self.buttonList[num].move(50*(num%9), 300+ (40 * (num // 9)))
             
        # have to do this outside the loop apparently
        self.buttonList[0].clicked.connect(lambda: self.buttonClick(0))
        self.buttonList[1].clicked.connect(lambda: self.buttonClick(1))
        self.buttonList[2].clicked.connect(lambda: self.buttonClick(2))
        self.buttonList[3].clicked.connect(lambda: self.buttonClick(3))
        self.buttonList[4].clicked.connect(lambda: self.buttonClick(4))
        self.buttonList[5].clicked.connect(lambda: self.buttonClick(5))
        self.buttonList[6].clicked.connect(lambda: self.buttonClick(6))
        self.buttonList[7].clicked.connect(lambda: self.buttonClick(7))
        self.buttonList[8].clicked.connect(lambda: self.buttonClick(8))
        self.buttonList[9].clicked.connect(lambda: self.buttonClick(9))
        self.buttonList[10].clicked.connect(lambda: self.buttonClick(10))
        self.buttonList[11].clicked.connect(lambda: self.buttonClick(11))
        self.buttonList[12].clicked.connect(lambda: self.buttonClick(12))
        self.buttonList[13].clicked.connect(lambda: self.buttonClick(13))
        self.buttonList[14].clicked.connect(lambda: self.buttonClick(14))
        self.buttonList[15].clicked.connect(lambda: self.buttonClick(15))
        self.buttonList[16].clicked.connect(lambda: self.buttonClick(16))
        self.buttonList[17].clicked.connect(lambda: self.buttonClick(17))
        self.buttonList[18].clicked.connect(lambda: self.buttonClick(18))
        self.buttonList[19].clicked.connect(lambda: self.buttonClick(19))
        self.buttonList[20].clicked.connect(lambda: self.buttonClick(20))
        self.buttonList[21].clicked.connect(lambda: self.buttonClick(21))
        self.buttonList[22].clicked.connect(lambda: self.buttonClick(22))
        self.buttonList[23].clicked.connect(lambda: self.buttonClick(23))
        self.buttonList[24].clicked.connect(lambda: self.buttonClick(24))
        self.buttonList[25].clicked.connect(lambda: self.buttonClick(25))

             
    def buttonClick(self, num):

        self.ThisGame.makeGuess(HangManGUI.alphabet[num].lower())
        
        # updates the game
        self.updateGame()
        # updates the GUI
        self.update()
        
    def updateGame(self):
        self.livesCount = self.ThisGame.getNumLives()
        self.guessedLetters = self.ThisGame.getCorrectArray()
        self.gameState = self.ThisGame.getGameState()
    
    def onButtonClick(self, button):
        button.setEnabled(False)


def main():
    app = QApplication(sys.argv)
    gui = HangManGUI()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()