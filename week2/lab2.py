import random

elements = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon"]
chosenElement = elements[random.randint(0, len(elements) - 1)]
print("An element has been chosen...")
guess = input("Guess the element: ").upper().strip()
guessCount = 0
while guess != chosenElement.upper() and guessCount < 2:
    guessCount += 1
    print("You guessed the wrong element! Try again.")
    match guessCount:
        case 1:
            print("The first letter is: " + chosenElement[0])
        case 2:
            print("The second letter is: " + chosenElement[1])
        case _:
            print("You ran out of guesses!")
    guess = input("Guess the element: ").upper().strip()
if guessCount == 3:
    print("You didn't guess the element!")
    print("The element was " + chosenElement)
if guess == chosenElement.upper():
    print("Congratulations! You guessed the correct element! " + chosenElement)
    if chosenElement == "Hydrogen":
        print("Hydrogen is cool")
    if chosenElement == "Helium":
        print("Helium is cool")
    if chosenElement == "Lithium":
        print("Lithium is cool")
    if chosenElement == "Beryllium":
        print("Beryllium is cool")
    if chosenElement == "Boron":
        print("Boron is cool")
    if chosenElement == "Carbon":
        print("Carbon is cool")
    if chosenElement == "Nitrogen":
        print("Nitrogen is cool")
    if chosenElement == "Oxygen":
        print("Oxygen is cool")
    if chosenElement == "Fluorine":
        print("Fluorine is cool")
    if chosenElement == "Neon":
        print("Neon is cool")