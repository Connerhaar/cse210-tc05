class Jumper:

    def __init__(self):
        self.alive = True
        self.parachute = {}

    def create_parachute(self):
        # prints out the parachute line by line by assigning a each line to a number in a dicitonary
        # then printing each number out in a while statement loop
        self.parachute = {
            1: " ______ ",
            2: "/      \ ",
            3: "\      / ",
            4: " \    / ",
            5: "  (OxO)",
            6: "  \ | / ",
            7: "    |",
            8: "   / \ ",
            9: "^^^^^^^^^^"
        }
        parachute = self.parachute
        return parachute

    def remove_parachute(self):
        # When check_guess is False it calls this function and then removes the first value in the dictionary
        # in affect this would remove the parachute
        parachute = self.parachute
        del parachute[0]
        return parachute

    def print_parachute(self):
        # prints the parachute
        parachute = self.parachute
        for key in parachute:
            print(key)

    def is_alive(self):
        parachute = self.parachute
        if parachute[0] == "  (OxO)":
            self.alive = False
        else:
            self.alive = True
        
