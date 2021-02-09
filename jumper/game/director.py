from game.console import Console
from game.jumper import Jumper
from game.word_bank import Word_Bank


class Director:
    def __init__(self):
        self.correct = True
        self.keep_playing = True
        self.console = Console()
        self.jumper = Jumper()
        self.word_bank = Word_Bank()

    def start_game(self):
        self.word_bank.load_list("wordlist.txt")
        self.word_bank.choose_word()
        self.jumper.create_parachute()
        self.word_bank.get_blank()

        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
            

    def get_inputs(self):
        guess = (self.console.read("Guess a letter [a-z]: ")).lower()
        self.correct = Word_Bank.check_guess(guess)

    def do_updates(self):
        if self.correct == True:
            self.jumper.print_parachute()
        elif self.correct == False:
            self.jumper.remove_parachute()
            self.jumper.print_parachute()
        else:
            self.console.write("You already guessed that letter")
            self.get_inputs()

    def do_outputs(self):
        alive = self.jumper.is_alive()
        if alive == False:
            self.keep_playing = False
            self.console.write(f"Oh no he died! the word was {Word_Bank.word}")

        else:
            if self.word_bank.check_win == True:
                self.console.write(f"You did it!")
