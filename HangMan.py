class Game(object):

    word_list = [['t', 'r', 'a', 'i', 'n'],
             ['c', 'r', 'i', 's', 'p'],
             ['t', 'a', 'c', 'o', 's'],
             ['c', 'l', 'i', 'c', 'k']]

    def __init__(self):
        self.livesLeft = 5
        self.word = ['t', 'r', 'a', 'i', 'n']
         
    def decrementLife(self):
        self.livesLeft -= 1
        
    def isAlive(self):
        return self.livesLeft > 0
        
    def checkLetterInWord(targetLetter, self):
        for letter in self.word:
            print (letter)
            if (targetLetter == letter):
                return True
        print (word)
        return False


        