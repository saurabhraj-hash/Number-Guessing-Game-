
import random

def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("\n===== NUMBER GUESSING GAME =====")
    print("Guess a number between 1 and 100!")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
            elif guess < secret_number:
                print("Too Low! Try again.")
            elif guess > secret_number:
                print("Too High! Try again.")
            else:
                print(f"\nCongratulations! You guessed it!")
                print(f"Attempts: {attempts}")
                break

        except ValueError:
            print("Please enter a valid number.")

def main():
    while True:
        play_game()

        again = input("\nPlay again? (yes/no): ").lower()

        if again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()

