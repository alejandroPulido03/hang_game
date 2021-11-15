import os

import media


class GameState:
    def __init__(self):
        self.points = 0
        self.lifes = 10
        self._word = 'test'
    
    @property
    def getWord(self):
        return self._word
    
    @getWord.setter
    def setWord(self, randWord):
        self._word = randWord

    def newWord(self):
        with open("./data.txt", 'r', encoding='utf-8') as datasetWords:
            datalist = datasetWords.readlines()
            import random
            randomWord = random.randrange(0, len(datalist))
            self._word = datalist[randomWord]
    
    def newMatch(self):
        self.newWord()
        RandWord = Word(self.getWord)
        match = Match(RandWord)
        match.startMatch()



class Match:
    def __init__(self, Word):
        self.Word = Word
        self.board = ('_ ' * (self.Word.lenWord - 1))

    def startMatch(self):
        print(self.board, self.Word.word)
        Hangman = Man()
        #while(Hangman > 0):
        userElection = input('Choose a letter and press enter: ')
        isAMatch = self.matchLetter(userElection)
        if isAMatch:
            self.board = self.putBoard(userElection)
            print(Hangman.parts)
        else:
            Hangman.parts -=1
            print(Hangman.parts)

        self.updatePoints(isAMatch)
        print(self.board)
    #def newHangGame():

    def matchLetter(self, letter):
        return letter in self.Word.word

    def putBoard(self, letter):
        splitWrd = list(self.Word.word)
        return ''.join(list(map(lambda ltr : f'{letter} ' if ltr == letter else '_ ', splitWrd)))

    def updatePoints(self, postvPoints):
        pass

class Word:
    def __init__(self, word):
        self.word = word
        self.lenWord = len(word)

class Man:
    def __init__(self):
        self.parts = 6 

def startInterface():
    print(media.title)
    input('Press enter to start, Press control C to exit')
    os.system('clear')
    Game = GameState()
    Game.newMatch()

if __name__ == '__main__':
    startInterface()
