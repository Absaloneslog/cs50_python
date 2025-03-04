print("I'm thinking a number:")
print("If you want to get out of here you have to guess")
print("hint: from 1 to 20")

def main():
    guess = get_guess()
    password = "12"
    if guess == password:
        print(f"correct, {guess} is the number. NOW you're free.")
    else:
        print("Incorrect, try again.")
        main()

def get_guess():
    guess = input("Enter your guess: ")
    return guess

main()
