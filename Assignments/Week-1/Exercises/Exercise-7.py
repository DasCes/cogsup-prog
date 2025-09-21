"""
Have a look at the script called 'human-guess-a-number.py' (in the same folder as this one).

Your task is to invert it: You should think of a number between 1 and 100, and the computer 
should be programmed to keep guessing at it until it finds the number you are thinking of.

At every step, add comments reflecting the logic of what the particular line of code is (supposed 
to be) doing. 
"""

from random import randint


def check_int(s):
    """ Check if string 's' represents an integer. """
    s = str(s)
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()


def input_integer(prompt):
    """ Asks user for an integer input. If valid, the string input is returned as an integer. """
    risposta = input(prompt)
    while not check_int(risposta):
        print('Please, enter a valid integer number')
        risposta = input(prompt)
    return int(risposta)


print("Think number 1-100")

minimo = 1
massimo = 100
tentativi = 0

while True:
    tentativi += 1
    supposizione = randint(minimo, massimo)

    print(f"Is it {supposizione}?")
    feedback = input("h/l/c: ").lower()

    if feedback == 'c':
        print(f"Got it! took {tentativi} tries")
        break
    elif feedback == 'h':
        massimo = supposizione - 1
    elif feedback == 'l':
        minimo = supposizione + 1
    else:
        continue

    if minimo > massimo:
        print("wait something wrong...")
        break