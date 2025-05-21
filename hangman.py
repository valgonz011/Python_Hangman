#(Optional): Define text formatting

BLUE = "\033[38;5;32m"
BOLD = "\033[1m"
RED = "\033[38;5;196m"
GREEN = "\033[38;5;28m"
RESET = "\033[0m"


# (0) Import the hangman art
hangman={0:'''
        ____________
         |



         ''',
        1:'''
        ____________
         |
         O


         ''',
        2:'''
        ____________
         |
         O
        /

        ''',
        3:'''
        ____________
         |
         O
        / \\

        ''',
        4:'''
        ____________
         |
         O
        / \\
         |
         ''',
        5:'''
        ____________
         |
         O
        / \\
         |
        /''',
        6:'''
        ____________
         |
         O
        / \\
         |
        / \\ '''}


# (1) Import a word from wonderwords

from wonderwords import RandomWord
rw = RandomWord()

print(f"{BOLD}LET'S PLAY: {BLUE}H A N G M A N{RESET}")


# (2) Select a random word out of the list

answer_word = rw.word().upper()


# (3) Count the word characters and assign "_" to each

hidden_word = ["_"] * len(answer_word)

#print(answer_word)  #delete this afterwards!!!!!!!


# (4) Define remaining mistakes

remaining_mistakes = 6


# (5) Looping until remaining mistakes is 0

while remaining_mistakes > 0:
    print(f"\nHidden word is: {' '.join(hidden_word)}.\n")
    picked_letter = input("If you want to play, pick a letter!🔤 \n").upper()


# (6) Verify if the letter is in the word

    if picked_letter in answer_word:
        for index, letter in enumerate(answer_word):    #enumerate() returns two outputs --> the index for each letter and the letter

            if letter == picked_letter:
                hidden_word[index] = picked_letter
        print(f'{GREEN}{BOLD}\n✅CORRECT!{RESET} The word contains the letter {BOLD}"{picked_letter}"{RESET}!\n')

        if "".join(hidden_word) == answer_word:
            print(f"{GREEN}{BOLD}\n🎉CONGRATULATIONS!{RESET} You've guessed the word: {GREEN}{BOLD}{answer_word}🏆{RESET}")
            break

    else:
        print(f"{RED}{BOLD}\n❌WRONG!{RESET} Number of mistakes left: {BOLD}{remaining_mistakes}{RESET} - Be careful 👀")
        print(hangman[(remaining_mistakes-6)*-1])
        print(f"···················································")

        remaining_mistakes = remaining_mistakes - 1


# (7) If the user runs out of mistakes --> Hanged

if remaining_mistakes == 0:
    print(f"😱You have run out of tries!\n \n The word was: {BOLD}{answer_word}{RESET}\n")
    print(f"{BOLD} 💀💀💀 HANGED! 💀💀💀{RESET}")
    print(hangman[6])
