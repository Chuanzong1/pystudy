import random
def guess_number():
    target=random.randint(1,100)
    print("I have a number between 1 and 100.")
    print("Can you guess my number?")
    print("Please type your first guess.")
    guess=int(input("your guess:"))
    while(guess!=target):
        if guess>target:
            print("too high,try again")
        else:
            print("too low,try again")
        guess=int(input("your guess again:"))
    print("congratulations! you guessed it correctly.")


        