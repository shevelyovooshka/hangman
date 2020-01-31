import random

print(' '.join('HANGMAN'))
welcome_message = input('Type "play" to play the game, "exit" to quit: ')
while welcome_message != "exit":
    if welcome_message == "play":
        print()

        word_list = ['python', 'java', 'kotlin', 'javascript']
        random.seed()
        chosen_word = random.choice(word_list)

        hidden_word = "-" * len(chosen_word)
        live = 0
        used_letters = []
        print(hidden_word)

        while live < 8:
            if hidden_word == chosen_word:
                break
            guess = input("Input a letter: ")
    
            if len(guess) != 1:
                print("You should print a single letter")
            elif str.islower(guess) == False:
                    print("It is not an ASCII lowercase letter")
            elif guess in used_letters:
                print("You already typed this letter")
                if guess not in chosen_word:
                    if live > 7:
                        break
        
            else:
                if guess not in chosen_word:
                    print("No such letter in the word")
                    used_letters.append(guess)
                    live += 1
                    if live > 7:
                        break
                else:
                    new_letters = ""
                    for i in range(len(chosen_word)):
                        if guess == chosen_word[i]:
                            new_letters += guess
                            used_letters.append(guess)
                        else:
                            new_letters += hidden_word[i]
                    hidden_word = new_letters
            print()
            print(hidden_word)

        if hidden_word == chosen_word:
            print("You guessed the word!")
            print("You survived!")
        else:
            print("You are hanged!")
        print()
        welcome_message = input('Type "play" to play the game, "exit" to quit: ')
        
    else:
        welcome_message = input('Type "play" to play the game, "exit" to quit: ')
