import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import testMod


class HangManGUI(QWidget):

    alphabet = ['A', 'B', 'C', 'D', 'E',
                'F', 'G', 'H', 'I', 'J', 'K',
                'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                'S', 'T', 'U', 'V', 'W', 'X',
                'Y', 'Z']

    def __init__(self):
        self.buttonList = []
        super(HangManGUI, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        
        self.generateLetterButtons()
        
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('HangMan')
        self.show()
    
    def generateLetterButtons(self): 
        for num in range (0, 26):
             self.buttonList.append(QPushButton(HangManGUI.alphabet[num], self))
             self.buttonList[num].move(50*(num%5), 40 * (num // 5))
             self.buttonList[num].clicked.connect(self.onButtonClick(self.buttonList[num]))
             
    def onButtonClick(self, button):
        button.setEnabled(False)
 
    def onChanged(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()
        testMod.hello()

def main():
    app = QApplication(sys.argv)
    gui = HangManGUI()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()