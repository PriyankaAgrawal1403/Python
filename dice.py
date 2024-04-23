import random

def roll_dice():
    print("Welcome to the Roll Dice Game!")
    print("Press Enter to roll the dice. Type 'exit' to end the game.")

    while True:
        user_input = input("Press Enter to roll the dice: ").strip().lower()

        if user_input == 'exit':
            print("Exiting the game...")
            break

        if user_input == '':
            # Generate a random number between 1 and 6 (inclusive)
            dice_roll = random.randint(1, 6)
            print(f"You rolled a {dice_roll}!")

def main():
    roll_dice()

if __name__ == "__main__":
    main()