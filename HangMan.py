import random

class Game(object):

    word_list = ['train', 'crisp', 'tacos', 'click']

    def __init__(self):
        self.livesLeft = 5
        self.word = Game.word_list[random.randint(0, len(Game.word_list) - 1)]
        self.correctArray = [0, 0, 0, 0, 0]; 

    def getWord(self):
        return self.word

    def getCorrectArray(self):
        return self.correctArray

    def decrementLife(self):
        self.livesLeft -= 1
       
    def getWordLength(self):
        return len(self.word)
         
    def getNumLives(self):
        return self.livesLeft
        
    def isAlive(self):
        return self.livesLeft > 0
        
    def makeGuess(self, letter):
        if (updateCorrectArray() == False):
            self.livesLeft -= 1
        
    def checkLetterInWord(self, targetLetter):
        if targetLetter in self.word:
            return True
        return False

    # Given a letter, returns a list containing the indices in the 
    # word where that letter occurs
    # If the letter does not occur in the word, then return the empty list
    def updateCorrectArray(self, letter):
    
        isCorrectGuess == False
    
        for num in range (0, len(self.word) - 1):
            if self.word[num] == letter:
                correctArray[num] = 1
                isCorrectGuess = True
        
        return isCorrectGuess

        