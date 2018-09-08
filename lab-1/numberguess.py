# Number Guessing Game with Insults!
# Dr. Tom Way
import os
import random

def main():

    # set maximum number that can be picked by program
    maxnum = 100

    # check if insults file exists at path parameter, set flag and insult list
    if os.path.isfile('insults.txt'):
        insults = 'yes'
        insultfile = open('insults.txt', 'r')
        insultlist = insultfile.read().splitlines()
        insultfile.close()
    else:
        insults = "no"

    print("Welcome to guess the number\n===========================")
    print("\nI'm thinking of a number between 1 and %d, and you have to guess what it is.\n" % maxnum)

    # generate random integer between 1 and maximum inclusive
    num = random.randint(1, maxnum)
    guess = ""

    # while your guess is not the random number
    while guess != num:
        # take input from console input stream
        strguess = input("Take a guess: ")
        # exit program if user inputs "exit"
        if strguess == "exit":
            print("You gave up, eh? Then I will, too. The number I was thinking of was %d." % num);
            return
        try:
            guess = int(strguess)
        except:
            print("Seriously? Your guess of \"%s\" is not a number!" % strguess)
            continue
        # guess lower than number, insult if provided, feedback on guess
        if guess < num:
            if insults == "yes":
                print(random.choice(insultlist))
            print("Guess higher next time\n")
        # guess higher than number, insult if provided, feedback on guess
        elif guess > num:
            if insults == "yes":
                print(random.choice(insultlist))
            print("Guess lower next time\n")

    # number was guessed correctly
    print("***CONGRATULATIONS***\nYour guess of %d is correct!\n" % guess)
    input('Press Enter to quit')

main()  
