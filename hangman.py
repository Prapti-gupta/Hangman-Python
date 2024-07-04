import random

def hangman():
    word = random.choice(["tiger", "superman", "thor", "doraemon", "avenger", "water", "stream"])
    validletter = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessmade = ''
    while len(word) > 0:
        main = ""
        missed = 0
        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + " "
        if main == word:
            print(main)
            print("CONGRATULATIONS!")
            print("You win! :)")
            break
        print("Guess the word:", main)
        print("Enter an Alphabet:")
        guess = input().casefold()

        if guess in validletter:
            guessmade = guessmade + guess
        else:
            print("zEnter a valid character")
            guess = input()
        if guess not in word:
            turns = turns - 1
        if turns == 9:
            print("\n 9 TURNS LEFT !")
            print("  ---------  ")
            print(" |         | ")
            print("  ---------  ")

        if turns == 8:
            print("\n 8 TURNS LEFT !")
            print("  ----------  ")
            print(" |         | ")
            print(" |    O    | ")
            print(" |         | ")
            print("  ---------  ")

        if turns == 7:
            print("\n7 TURNS LEFT !")
            print("  ----------  ")
            print(" |         | ")
            print(" |    O    | ")
            print(" |    |    | ")
            print(" |         | ")
            print("  ---------  ")

        if turns == 6:
            print("\n6 TURNS LEFT !")
            print("  ----------  ")
            print(" |         | ")
            print(" |    O    | ")
            print(" |    |    | ")
            print(" |   /     | ")
            print(" |         | ")
            print("  ---------  ")

        if turns == 5:
            print("\n5 TURNS LEFT !")
            print("  ----------  ")
            print(" |         | ")
            print(" |    O    | ")
            print(" |    |    | ")
            print(" |   / \   | ")
            print(" |         | ")
            print("  ---------  ")

        if turns == 4:
            print("\n4 TURNS LEFT !")
            print("  ----------  ")
            print(" |         | ")
            print(" |  \ O    | ")
            print(" |    |    | ")
            print(" |   / \   | ")
            print(" |         | ")
            print("  ---------  ")

        if turns == 3:
            print("\n3 TURNS LEFT !")
            print("  ----------  ")
            print(" |         | ")
            print(" |  \ O /  | ")
            print(" |    |    | ")
            print(" |   / \   | ")
            print(" |         | ")
            print("  ---------  ")

        if turns == 2:
            print("\n2 TURNS LEFT !")
            print("  ----------  ")
            print(" |         | ")
            print(" |  \ O /| | ")
            print(" |    |    | ")
            print(" |   / \   | ")
            print(" |         | ")
            print("  ---------  ")

        if turns == 1:
            print("\n1 TURNS LEFT !")
            print("Last breaths counting. Take care!")
            print("  ----------  ")
            print(" |         | ")
            print(" |  \ O_|/ | ")
            print(" |    |    | ")
            print(" |   / \   | ")
            print(" |         | ")
            print("  ---------  ")

        if turns == 0:
            print("\nYou lose! :()")
            print("You let a kind man die")
            print("  ----------  ")
            print(" |         | ")
            print(" |    O_|  | ")
            print(" |   /|\   | ")
            print(" |   / \   | ")
            print(" |         | ")
            print("  ---------  ")
            break

name = input("Enter your name: ")
print(f"Welcome {name}")
print("=====================")
print("\nTry to guess the word in less than 10 attempts")
hangman()
print()
