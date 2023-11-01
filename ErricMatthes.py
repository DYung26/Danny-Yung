import random

while True: # def main():
    a = random.randint(1, 100)
    print(a)
    b = int(input("I'm thinking of a number between 1 and 100! Try to guess the number I'm thinking of: "))
    '''while True:
        if b > int(100):
            b = int(input("Invalid! Please enter a number between 1 and 100! "))
        elif b <= 100:
            break'''
    while True:
        if b < a:
            b = int(input("Too low! Guess again: "))
        elif b > a:
            b = int(input("Too high! Guess again: "))
        elif b == a:
            c = input("That's it! Would you like to play again? (yes/no) ")
            while True:
                if c == "yes":
                    break # main()
                elif c == "no":
                    print("Thanks for playing!")
                    break
                else:
                    c = input("Enter a valid response! (yes/no) ")
            if c == "yes":
                break # main()
            if c == "no":
                break
    if c == "no":
        break

# main()