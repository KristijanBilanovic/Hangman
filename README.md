# Hangman
#### **Video Demo:**  https://youtu.be/Avp6iYbRTYg
#### **Description:** Hangman is a terminal-based game that gives the user six chances to guess a randomly chosen word from a list of 3000 English words. The game includes ASCII art and requires the Rich library. The program uses the init_dis, replace, and output functions to track player progress and lives. If the player guesses the word, they win, and if they run out of lives, they lose and the word is revealed.



## main Function
The main function of this program is responsible for running the game loop.

It randomly selects a word from a list of 3000 English words and initializes a ```display_word``` with underscores representing the letters of the word. The player then has six chances to guess letters that may be in the word. If the player guesses a letter correctly, the corresponding underscores in the ```display_word``` are replaced with the letter. If the player guesses incorrectly, a piece of hangman ASCII art is printed and the player loses a life. The game continues until either the player correctly guesses the word or they run out of lives. If the player correctly guesses the word, a congratulatory message is printed and the program exits. If the player runs out of lives, a message is printed revealing the word and the program exits.



## init_dis Function
The init_dis function takes one parameter, the randomly chosen word, and returns a string consisting of underscores (_) in the same length as the randomly chosen word. The purpose of this function is to initialize the ```display_word``` variable that keeps track of the player's progress in guessing the word.

Its importance lies in its ability to create a "hidden" version of a word, which adds an element of intrigue and challenge to the game.



## replace Function
The ```replace``` function takes three arguments: ```word```, ```display_word```, and ```guess```. It returns a modified ```display_word``` string with the guessed letter(s) added in if they were correct. It also keeps track of the player's remaining lives by decrementing the global lives variable if they guess incorrectly.

The function first initializes a boolean variable ```found_once``` to ```False``` to keep track of whether the guessed letter has been found at least once in the ```word```. Then, it iterates through the length of ```word``` and uses the ```find``` method to search for the index of the guessed letter in ```word```.

If the ```find``` method returns ```-1``` and ```found_once``` is ```False```, then the guessed letter is not in the```word```, so ```lives``` is decremented and the function returns unchanged ```display_word```.

If ```find``` returns ```-1``` but ```found_once``` is ```True```, that means the guessed letter has already been found at least once, so the function returns modified ```display_word``` and does not decrement ```lives``` variable.

If ```find``` returns a valid index, then the replace method is used to replace the letter at that index of ```word``` with a garbage value (in this case, "9") so that it can't be found again. Then, the ```display_word``` string is updated to replace the underscore at the corresponding index with the guessed letter.

Finally, the function returns the modified ```display_word``` string.



## output Function
The `output` function in the Hangman game takes `display_word` as a parameter and returns a string that represents the current state of the game. The function consists of two for loops that build the string that is ultimately returned.

The first for loop adds spaces in between each character of `display_word`. The purpose of this is to make the player's progress more clear and easier to read. The resulting string is then concatenated with a certain amount of whitespace and the current state of the Hangman ASCII art.

The second for loop adds heart emojis to the string, representing the number of lives the player has left. The number of heart emojis added is equal to the `lives` variable, which is a global variable that is initially set to 6. The purpose of this is to give the player a visual representation of how many lives they have left and to make the game more engaging.

Overall, the `output` function plays a crucial role in the Hangman game by providing the player with a clear and concise representation of their progress and current state in the game.
