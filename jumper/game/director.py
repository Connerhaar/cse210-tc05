from game.console import Console
from game.jumper import Jumper
from game.word_bank import Word_Bank


class Director:
    def __init__(self):
        self.console = Console('game.wordlist.10000.txt')
        self.correct = True
        self.keep_playing = True

    def start_game(self):
        Word_Bank.load_list()
        Word_Bank.choose_word()
        Jumper.create_parachute()
        Word_Bank.get_blank()

    def get_inputs(self):
        guess = (self.console.read("Guess a letter [a-z]: ")).lower()
        self.correct = Word_Bank.check_guess(guess)

    def do_updates(self):
        if self.correct == True:
            Jumper.print_parachute()
        elif self.correct == False:
            Jumper.remove_parachute()
            Jumper.print_parachute()
        else:
            self.console.write("You already guessed that letter")
            self.get_inputs()

    def do_outputs(self):
        alive = Jumper.is_alive()
        if alive == False:
            self.keep_playing = False
            self.console.write(f"Oh no he died! the word was {Word_Bank.word}")

        else:
            if Word_Bank.check_win == True:
                self.console.write(f"You did it!")
