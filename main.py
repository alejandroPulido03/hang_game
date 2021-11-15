import os
from posix import listdir

import media


class GameState:
    def __init__(self):
        self.points = 0
        self.lifes = 3
        self._word = ''
    
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
        while self.lifes > 0:
            self.newWord()
            RandWord = Word(self.getWord)
            match = Match(RandWord)
            match.newHangGame(self.lifes)
            self.lifes -=1
        if self.points > 100:
            print('You win')
        else:
            print('Game Over')



class Match:
    def __init__(self, Word):
        self.Word = Word
        self.board = ('_ ' * (self.Word.lenWord - 1))
    
    def newHangGame(self, lifes):
        Hangman = Man()
        while(Hangman.parts > 0):
            print(f'Hangman parts: {Hangman.parts} \t \t \t Lifes: {lifes} ')
            print(self.board)
            if(self.board.replace(' ', '') == self.Word.word.replace('\n', '')):
                print('You win')
                break
            userElection = input('Choose a letter and press enter: ')
            isAMatch = self.matchLetter(userElection)
            if isAMatch:
                self.board = self.putBoard(userElection)
            else:
                Hangman.parts -=1

            self.updatePoints(isAMatch)
            os.system('clear')
            
        if Hangman.parts == 0: print(f'You lose, the word was {self.Word.word}')
        try:
            input('Enter to continue, Press control C to exit: ')
        except:
            exit()
        os.system('clear')

    def matchLetter(self, letter):
        return letter in self.Word.word

    def putBoard(self, letter):
        splitWrd = list(self.Word.word)
        splitBrd = self.board.split(' ')
        return ' '.join(list(map(lambda ltr, actual : f'{ltr}' if self.normalize(ltr) == letter and letter != actual else actual, splitWrd, splitBrd)))

    def updatePoints(self, postvPoints):
        #TODO: System of points
        pass

    def normalize(self, ltr):
        accents = {
            'á': 'a',
            'é': 'e',
            'í' : 'i',
            'ó' : 'o',
            'ú' : 'u'
        }
        return accents.get(ltr) or ltr
class Word:
    def __init__(self, word):
        self.word = word
        self.lenWord = len(word)

class Man:
    def __init__(self):
        self.parts = 6 

def startInterface():
    print(media.title)
    try:
        input('Press enter to start, Press control C to exit: ')
    except:
        exit()
    
    os.system('clear')
    Game = GameState()
    Game.newMatch()

if __name__ == '__main__':
    startInterface()
