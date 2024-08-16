# Remember that correct accepts position from 0 while misplaced takes from 1
# File checked and conformed working


NAME = "WordleSolver"
VERSION = "0.0.1"

class WordleSolver(object):
    def __init__(self):
        self.words = None
        self.solutions = None
        self.correct = {}
        self.misplaced = {}
        self.incorrect = []

    def get_words(self):
        return self.words

    def get_solution(self):
        return self.solutions

    def set_words(self):
        with open("words.txt", "r") as f:
            self.words = f.read().split()
        return self.words

    def set_correct(self, correct):
        self.correct = correct

    def set_incorrect(self, incorrect):
        self.incorrect = incorrect

    def set_misplaced(self, misplaced):
        self.misplaced = misplaced

    def ch_letters(self):
        self.words = [word for word in self.words if not any(char in word for char in self.incorrect)]
        self.words = [word for word in self.words if all(char in word for char in self.correct.values())]
        self.words = [word for word in self.words if all(char in word for char in self.misplaced)]

    def ch_correct(self):
        temp = []
        for word in self.words:
            for pos in self.correct:
                if word[pos] != self.correct[pos]:
                    if word not in temp:
                        temp.append(word)

        while temp:
            if temp[0] in self.words:
                self.words.remove(temp[0])
                temp.pop(0)

    def ch_misplaced(self):
        temp = []
        for word in self.words:
            for letter in self.misplaced:
                if any(index - 1 == word.find(letter) for index in self.misplaced[letter]):
                    temp.append(word)

        while temp:
            if temp[0] in self.words:
                self.words.remove(temp[0])
                temp.pop(0)

    def set_solution(self):
        self.solutions = self.words
