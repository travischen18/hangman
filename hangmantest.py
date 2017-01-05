import HangMan

game1 = HangMan.Game()

game1.decrementLife()
print (game1.isAlive())
print (game1.checkLetterInWord('r'))

print ('r' == 'r')