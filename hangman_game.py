import random 

lives=6

choosen_word = ["anjali","gayathri","durgaprasad","swathi","nagaraju"]

print(choosen_word)
diplay = ['__' for _ in  choosen_word]



while  range(len(choosen_word)):
    display = '__'
    print(display)
game_over = False

while not game_over:
    guessed_letter = input("Enter the guessed letter: ").lower()

    for position in range(len(choosen_word)):
      letter =  choosen_word[position]
    if letter == guessed_letter:
        display[position] = guessed_letter

    print(display)
    if guessed_letter not in choosen_word:
        lives-= 1
    if lives == 0:
        game_over =True
        print("YOU LOSE!")
    if "__" not in display:
        game_over = True
        print("YOU WIN!!!")

