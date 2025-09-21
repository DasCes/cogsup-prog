"""
Write a script that lists all the prime numbers between 1 and 10000.
(A prime number is an integer greater or equal to 2 which has no divisors except 1 and itself). 
Hint: Write an is_factor helper function.
"""


def is_factor(divisore, numero):
    """True iff (if and only if) d is a divisor of n."""
    return numero % divisore == 0


def is_prime(numero):
    if numero < 2:
        return False

    for fattore in range(2, int(numero ** 0.5) + 1):
        if is_factor(fattore, numero):
            return False

    return True


lista_primi = []
for num in range(1, 10001):
    if is_prime(num):
        lista_primi.append(num)

print(lista_primi)