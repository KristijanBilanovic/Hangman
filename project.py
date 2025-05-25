import random
import sys
from rich.console import Console
from rich.markdown import Markdown

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

lives = 6

won = """# 🎉 CONGRADULATIONS YOU'VE WON 🎉"""
lost = """# 😞 YOU'VE LOST, BETTER LUCK NEXT TIME 😞 """
console = Console()

def main():

    with open("words.txt", "r") as file:
        lines = file.readlines()
        word = lines[random.randint(0, 2999)].strip().upper()


    display_word = ""

    display_word = init_dis(word)

    print("\n Welocme to Hangman (Kristijan's Version). Now, BABY, LET THE GAMES BEGEN!")

    while (lives != 0):
        print(HANGMANPICS[6 - lives], "   ", output(display_word))
        guess = input("Guess a letter: ").upper()

        display_word = replace(word, display_word, guess)

        if word == display_word:
            print(HANGMANPICS[6 - lives], "   ", output(display_word))
            console.print(Markdown(won))
            sys.exit(0)

    print(HANGMANPICS[6 - lives], " ", output(display_word))
    console.print(Markdown(lost))
    console.print("The word was: " +  word, style="bold underline red")
    print("\n")
    sys.exit(0)


def init_dis(word):
    string = ""
    for _ in range(len(word)):
        string += "_"
    return string


def replace (word, display_word, guess):
    global lives
    found_once = False
    word = word.upper()
    guess = guess.upper()
    for _ in range(len(word)):
        index = word.find(guess)

        if index == -1 and found_once == False:
            lives -= 1
            return display_word

        elif index == -1 and found_once:
            return display_word

        found_once = True
        word = word.replace(word[index], "9", 1)
        display_word = display_word[:index] + guess + display_word[index + 1:]

    return display_word


def output(display_word):

    string = ""

    for c in display_word:
        string += c + " "

    string += "   "

    # print out lives
    for _ in range(lives):
        string += "❤️  "

    return string

if __name__ == "__main__":
    main()
