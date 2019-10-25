import random
sticks = 10
players = ["player", "computer"]
current_player = None

#Prints out the rules
rules = ["Choose an amount of sticks to remove", "You must choose between 1 and 3 sticks", "When there are no sticks left, the last person who played wins"]
print("Welcome to the Stick Game!")
print("The rules are the following: ")
for rule in rules:
    print("  - " + rule)

while sticks > 0:
    print("\nThere are " + str(sticks) + " stick(s) left")
    #Player's turn
    current_player = players[0]
    amount = int(input("How many sticks do you want to remove? Remember to choose between 1 and 3: "))
    #Makes sure you choose between 1 and 3
    while amount > 3 or amount <= 0:
        amount = int(input("Amount must be between 1 and 3, try again: "))
    sticks -= amount
    print("There are " + str(sticks) + " stick(s) left")
    if sticks <= 0:
        break

    #Computer's turn; makes sure computer doesn't choose more than provided amount of sticks
    current_player = players[1]
    if sticks >= 3:
        computer_amount = random.randint(1, 3)
    elif sticks == 2:
        computer_amount = random.randint(1, 2)
    elif sticks == 1:
        computer_amount == 1
    print("The computer chose to remove " + str(computer_amount) + " stick(s)")
    sticks -= computer_amount

#If you were playing last, you won
if current_player == players[0]:
    print("YOU WON!!!")

#If the computer was playing last, they won
elif current_player == players[1]:
    print("\nThere are " + str(sticks) + " stick(s) left")
    print("\nSorry, you lost. Better luck next time!")
