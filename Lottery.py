import random

winning = set(random.sample(range(1, 61), 6))

print("WELCOME TO THE LOTTERY TRY YOUR LUCK TO US!")

player = set(int(input(f"Please Enter number {i+1}: ")) for i in range(6))

match = len(winning & player)
prize = 1_000_000 if match == 6 else match * 1000

# Results
print("\n------ LOTTERY RESULTS ------")
print("Winning Numbers:", winning)
print("Your Numbers:", player)
print("Matched:", match)
print("Prize: ₱", prize)
