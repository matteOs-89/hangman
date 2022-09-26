import random

words = []
with open('/usr/share/dict/words',) as guess:
    for line in guess:
        words.append(line.strip())


computer_choice = random.choice(words).lower()


word_length = len(computer_choice)

display = []
lives = 6
hint_lives = 3

for i in range(word_length):
    display += "_"


game_on = True

welcome = input("Do you want to play a game of HANGMAN? Type 'Y' for yes or 'Q' to quit: ").lower()

if welcome == "y":
    print("WELCOME 😎")

elif welcome == 'q':
    print("GOODBYE😢")
    quit()

else:
    print("Please choose the right choice next time")
    quit()


while game_on:

    print(f"{' '.join(display)}")

    guess = input("What's your guess letter in the hidden word? or  'H' for a hint ").lower()

    if guess in display:
        print("You already picked that letter, please try again")

    for position in range(word_length):
        letter = computer_choice[position]
        if letter == guess:
            display[position] = letter

    if guess == "h" and hint_lives > 0:
        hint_lives -= 1
        print(f"You have {hint_lives} hint chances")
        hint = display.index("_")
        display[hint] = computer_choice[hint]


    elif hint_lives == 0:
        print("You have no hint lives left")






    if guess not in computer_choice:

        lives -= 1
        print(f"Wrong guess, please try again, you have {lives} lives left")

        if lives == 0:
            game_on = False
            print("Sorry you ran out of guess lives, you lost 😢")
            print(f"The answer was {computer_choice}")




    if "_" not in display:
        game_on = False
        print(' '.join(display))
        print(f"The word was {computer_choice}")
        print("CONGRATULATIONS 🎉🎉🎉, You've completed the game 😎")



