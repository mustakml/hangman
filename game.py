import random

HANGMAN_PICS = [
    """
     +---+
         |
         |
         |
        ===""",
    """
     +---+
     O   |
         |
         |
        ===""",
    """
     +---+
     O   |
     |   |
         |
        ===""",
    """
     +---+
     O   |
    /|   |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ==="""
]



words = ["python", "choice", "school", "university", "country"]

def choose_word(words):
    return random.choice(words)

def display_word(secret_word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in secret_word])

def play_again():
    return input("Nochmal spielen? (j/n): ").lower().startswith("j")



def make_guess(secret_word, guessed_letters):
    while True:
        guess = input("Rate einen Buchstaben: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Bitte einen Buchstaben eingeben")
            continue

        if guess in guessed_letters:
            print("Du hast den Buchstaben bereits eingegeben :( Bitte einen neuen")
            continue

        guessed_letters.append(guess)
        return guess 

def main():
    secret_word = choose_word(words)
    guessed_letters = []
    tries = len(HANGMAN_PICS) - 1

    print("Willkommen bei Hangman!")
    while tries > 0:
        print(HANGMAN_PICS[6 - tries])
        guess = make_guess(secret_word, guessed_letters)
        # display board einbauen bei schleifendurchgang 
        if guess in secret_word:
            print(f"{guess} ist im Wort")
            if all(letter in guessed_letters for letter in secret_word):
                print(f"Gewonnen! Das Wort ist '{secret_word}' ")
                antwort = play_again()
                if play_again():
                    main()
                else:
                    break
        else:
            tries -= 1
            print(f"{guess} ist nicht im Wort. Du hast noch {tries} Versuche.")
        
        if tries == 0:
            print(f"Alle Versuche aufgebraucht, du bist raus")
            print(HANGMAN_PICS[6])
            if play_again():
                main()
            else:
                break
if __name__ == "__main__":
    main()


        
