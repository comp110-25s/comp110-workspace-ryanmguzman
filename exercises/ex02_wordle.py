"""Wordle Game"""

__author__ = "730735896"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(word: str, char: str) -> bool:
    """Checks if char is in word"""
    assert len(char) == 1, f"len('{char}') is not 1"
    i = 0
    while i < len(word):
        if word[i] == char:
            return True
        i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Picks a Color Based on Accuracy of Letter Position"""
    assert len(guess) == len(secret), "Guess must be same length as secret"
    i = 0
    emoji = ""
    while i < len(guess):
        if guess[i] == secret[i]:
            emoji += GREEN_BOX
        elif contains_char(secret, guess[i]):
            emoji += YELLOW_BOX
        else:
            emoji += WHITE_BOX
        i += 1
    return emoji


def input_guess(expected_length: int) -> str:
    """Asks for a word with a specific length"""
    guess = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn = 1
    won = False
    while turn <= 6 and not won:
        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            won = True
        else:
            turn += 1
    if won:
        print(f"You won in {turn}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
