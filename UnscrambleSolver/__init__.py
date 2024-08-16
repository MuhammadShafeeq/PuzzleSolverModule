import json

NAME = "Unscramble Solver"
VERSION = "0.0.1"


class UnscrambleSolver(object):
    def __init__(self, letters):
        self.wdict = self.set_dict()
        self.letters = letters
        self.solutions = {}

    def solve(self):
        self.wdict = [word for word in self.wdict if all(char in self.letters for char in word)]
        self.wdict = [word for word in self.wdict if len(word) <= len(self.letters)]
        for i in self.wdict:
            if len(i) < 3:
                continue
            l = str(len(i)) + " letter words"
            if l in self.solutions:
                self.solutions[l].append(i)
            else:
                self.solutions[l] = [i, ]

    def get_solutions(self):
        return self.solutions
    @staticmethod
    def set_dict():
        dictionary = []
        with open("dictionary.txt", "r") as f:
            for i in f.read().split():
                dictionary.append(i)
        return dictionary

    @staticmethod
    def get_definition(word):
        with open('dictionary.json', 'r') as f:
            dict1 = json.load(f)
        definition = dict1[word]
        return definition