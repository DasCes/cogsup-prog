from random import randint

""" Simple game where the computer "thinks" about a number between 1 and 100 and the user must guess it"""

def check_int(s):
    """ Check if string 's' represents an integer. """
    s = str(s)
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

def input_integer(prompt):
    guess = input(prompt)
    while not check_int(guess): 
        print('Please, enter a n integer number')
        guess = input(prompt)  # try again
    return int(guess)
##

target = randint(1, 100)

print("I am thinking about a number between 1 and 100. Try to find it!")
guess = input_integer("Your guess (1-100)? ")

while guess != target:
    if guess < target: print("Your guess is too low!")
    else: print("Your guess is too high!\n")
    guess = input_integer("New guess? ")

print("You win! The number was indeed " + str(target))