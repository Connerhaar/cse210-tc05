import random

class Word_Bank:
    def __init__(self):
        self.word = ""
        self.blank = ""
        self.guesses = ''
        self.word_list = []
        self.length = 0

    def choose_word(self):
        maximum = len(self.word_list)
        number = random.randint(1, maximum)
        self.word = self.word_list[number]
        self.hide_word()

    def load_list(self, filename):
        with open(filename) as reader:
            self.word_list = reader.readlines()

    def hide_word(self):
        self.length = len(self.word)
        for _ in range(1, self.length):
            self.blank = self.blank + '_ '

    def check_guess(self, guess):
        if guess in self.guesses:
            status = 'Invalid'
        else:
            self.guesses = self.guesses + guess
            status = True
            if guess in self.word:
                status = True
                self.replace(guess)
            else:
                status = False
        return status

    def replace(self, letter):
        s = list(self.blank)
        for i in range(0, len(self.word)):
            if self.word[i] == letter:
                s[i*2] = letter
        self.blank = ''.join(s)

    def get_blank(self):
        return self.blank

    def check_win(self):
        alive = True
        if '_' in self.blank:
            alive = True
        else:
            alive = False
        return alive
