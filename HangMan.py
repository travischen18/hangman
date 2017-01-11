import random

class Game(object):

    word_list = ['train', 'crisp', 'tacos', 'click', 'words', 'euros', 'trite', 'fluff', 'power']

    def __init__(self):
        self.livesLeft = 6
        self.word = Game.word_list[random.randint(0, len(Game.word_list) - 1)]
        self.correctArray = [0] * len(self.word); 
        
        # gameState = 0 : not over; = 1 : won; = 2 : lost;
        self.gameState = 0;

    def getWord(self):
        return self.word

    def getCorrectArray(self):
        return self.correctArray
       
    def getWordLength(self):
        return len(self.word)
         
    def getNumLives(self):
        return self.livesLeft
        
    def isAlive(self):
        return self.livesLeft > 0
        
    def makeGuess(self, letter):
        if (self.gameState == 0):
            if (self.updateCorrectArray(letter) == False):
                self.livesLeft -= 1
                
        self.updateGameState()
        
    def getGameState(self):
        return self.gameState
        
    def updateGameState(self):
    
        if (self.wordIsGuessed()):
            self.gameState = 1
        elif (self.livesLeft > 0):
            self.gameState = 0
        else:
            self.gameState = 2

            
    def wordIsGuessed(self):
        if 0 in self.correctArray:
            return False
        else:
            return True

    # Update the 'correct array'
    def updateCorrectArray(self, letter):
    
        isCorrectGuess = False
    
        for num in range (0, len(self.word)):
            if self.word[num] == letter:
                self.correctArray[num] = 1
                isCorrectGuess = True
        
        return isCorrectGuess

        