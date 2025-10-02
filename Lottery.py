import random

class LotteryGame:
    def __init__(self):
        self.winning = set(random.sample(range(1, 61), 6))
        self.player = set()
        self.match = 0
        self.prize = 0

    def get_player_numbers(self):
        print("WELCOME TO THE LOTTERY! TRY YOUR LUCK WITH US!")
        while len(self.player) < 6:
            try:
                num = int(input(f"Please Enter number {len(self.player) + 1}: "))
                if num < 1 or num > 60:
                    print("Number must be between 1 and 60.")
                elif num in self.player:
                    print("Number already entered. Choose a different number.")
                else:
                    self.player.add(num)
            except ValueError:
                print("Invalid input. Please enter a number.")

    def calculate_prize(self):
        self.match = len(self.winning & self.player)
        self.prize = 1_000_000 if self.match == 6 else self.match * 1000

    def show_results(self):
        print("\n------ LOTTERY RESULTS ------")
        print("Winning Numbers:", sorted(self.winning))
        print("Your Numbers:", sorted(self.player))
        print("Matched:", self.match)
        print("Prize: ₱", self.prize)

    def play(self):
        self.get_player_numbers()
        self.calculate_prize()
        self.show_results()

if __name__ == "__main__":
    game = LotteryGame()
    game.play()
