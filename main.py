import random
def play():
    a = ['rock', 'paper', 'scissors']
    b = input("Rock, paper, or scissors?: ").lower()
    c = random.choice(a)
    while b not in a:
        print("Invalid input")
        b = input("Rock, paper, or scissors?: ").lower()
    if b == 'rock':
        if c == 'paper':
            print("You lose!")
        elif c == 'rock':
            print("It's a tie!")
        elif c == 'scissors':
            print("You win!")
    if b == 'paper':
        if c == 'rock':
            print("You win!")
        elif c == 'paper':
            print("It's a tie!")
        elif c == 'scissors':
            print('You lose!')
    if b == 'scissors':
        if c == 'rock':
            print("You lose!")
        elif c == 'scissors':
            print("It's a tie!")
        elif c == "paper":
            print("You win!")
    print()
    print(f"Computer: {c}")
    print(f"You: {b}")
    t = input("Again? Y/N: ").lower()
    y = ['y', 'n']
    while t not in y:
        print("Invalid input")
        t = input("Again? Y/N: ").lower()
    if t == 'y':
        play()
    elif t == 'n':
        print("Ok!")
play()