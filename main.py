import os
from posix import listdir

import media


class GameState:
    def __init__(self):
        self.points = 0
        self.lifes = 10
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
            match.newHangGame(self.lifes, self.points)
            self.lifes -=1
            self.points += match.matchPoints
        if self.points > 50:
            print(f'\n\n\n {media.YOUWIN} \n \t\t\t\t Points: {self.points}')
        else:
            print(f'\n\n\n {media.YOULOSE} \n \t\t\t\t Points: {self.points}')



class Match:
    def __init__(self, Word):
        self.Word = Word
        self.board = ('_ ' * (self.Word.lenWord - 1))
        self.matchPoints = 0
    
    def newHangGame(self, lifes, points):

        Hangman = Man()

        while(Hangman.parts > 0):

            print(f'🛡️: {Hangman.parts} \t \t \t ❤️: {lifes} \t \t \t 🪙: {points} \n\n')
            print(f'\t \t \t' + self.board)
            print(f'\n \n' + media.HANGMANPICS[Hangman.parts])
            if(self.board.replace(' ', '') == self.Word.word.replace('\n', '')):
                print('\t\t\t\t You win')
                break
            userElection = input(f'\t\t Choose a letter and press enter: ')
            isAMatch = self.matchLetter(userElection)
            if isAMatch:
                self.board = self.putBoard(userElection)

            else:
                Hangman.parts -=1

            self.updatePoints(isAMatch)
            os.system('clear')
            
        if Hangman.parts == 0: 
            print(f'\n \t \t You die, the word was {self.Word.word} \n  {media.YOUDIED}')

        try:
            input('\t Enter to continue, Press control C to exit: ')
        except:
            os.system('clear')
            exit()
        os.system('clear')

    def matchLetter(self, letter):
        return letter in self.Word.word
    
    def updatePoints(self, postvPoints):
        if postvPoints:
            from functools import reduce
            numOfChanges = len(list(filter(lambda d: d.isalpha(), self.board)))
            self.matchPoints += abs(numOfChanges - self.matchPoints)
        else:
            self.matchPoints = -1
        

    def putBoard(self, letter):
        splitWrd = list(self.Word.word)
        splitBrd = self.board.split(' ')
        return ' '.join(list(map(lambda ltr, actual : f'{ltr}' if self.normalize(ltr) == letter and letter != actual else actual, splitWrd, splitBrd)))

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
    os.system('clear')
    print('\n\n\n\n')
    print(media.TITLE)
    print('\n \t\t\t\t  Coded with ❤️ by @diegop384')
    try:
        input('\n \t\t\t Press enter to start, Press control C to exit: ')
    except:
        os.system('clear')
        exit()
    
    os.system('clear')
    Game = GameState()
    Game.newMatch()

if __name__ == '__main__':
    startInterface()
