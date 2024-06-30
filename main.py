# Step 1
import random
from hangman_art import stages, logo
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    user_guess = input("Guess a letter: ").lower()

    if user_guess in display:
        print(f"You've already guessed {user_guess}")

    # Check guessed letter:
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == user_guess:
            display[position] = letter

    # Check if user is wrong:
    if user_guess not in chosen_word:
        print(f"You guessed {user_guess}, that's not in the word. You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose!")

    # Join elements in list and turn to a string:
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You Win!!")

    print(stages[lives])
