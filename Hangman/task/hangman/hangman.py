import random
count = 0
letters = set()
alphabet = set("abcdefghijklmnopqrstuvwxyz")
game_name = "H A N G M A N"
print(game_name)
keyword = ["python", "java", "kotlin", "javascript"]

while True:
    choice = input('Type "play" to play the game, "exit" to quit: ')
    if choice == "exit":
        break
    key = random.choice(keyword)
    hint = list("-" * (len(key)))
    while choice == "play":
        print()
        print("".join(hint))
        letter = input("Input a letter: ")
        if len(letter) != 1:
            print("You should input a single letter")
            continue
        if letter not in alphabet:
            print("Please enter a lowercase English letter")
            continue
        if letter in letters:
            print("You've already guessed this letter")
        if letter not in key and letter not in letters:
            letters.add(letter)
            count += 1
            print("That letter doesn't appear in the word")
            if count == 8:
                print("You lost!")
                break
        else:
            letters.add(letter)
            for i in range(len(key)):
                hint[i] = letter if key[i] == letter else hint[i]
        if "".join(hint) == key:
            print("You guessed the word!")
            print("You survived!")
            break
