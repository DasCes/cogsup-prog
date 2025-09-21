################################################################################
"""
Recommended readings: 
  Chapter on dictionaries: https://automatetheboringstuff.com/3e/chapter7.html 
  Iterating through dictionaries: https://realpython.com/iterate-through-dictionary-python/
"""
################################################################################

"""
Exercise 4.1

Task:
------
Print the sum of the values in the dictionary.
"""

dct = {'a': 3, 'b': 7, 'c': -2, 'd': 10, 'e': 5}

Dictsum = sum(dct.values())
print(f"sum: {Dictsum}")

print("Exercise 4.1")

pass

print("---")

"""
Exercise 4.2

Task:
------
Print the key that has the largest value in dct.

largestValueKey = max(dct, key=dct.get)
print(f"largest key valuee: {largestValueKey}")


"""

print("Exercise 4.2")

pass

print("---")

"""
Exercise 4.3

Task:
------
Create a new dictionary with the squares of all the values in dct.

squares_dct = {}
for k, v in dct.items():
    squares_dct[k] = v**2
print(f"sqrt values of dict are: {squares_dct}")

"""

print("Exercise 4.3")

pass

print("---")

"""
Exercise 4.4

Task:
------
Print only the keys in dct whose values are even numbers.

for i, j in dct.items():
    if j%2 == 0:
        print(i)
"""

print("Exercise 4.4")

pass

print("---")

"""
Exercise 4.5

Task:
------
Create a new dictionary that swaps the keys and values in dct.

swap_dct = {}
for i,j in dct.items():
    swap_dct[j] = i

print(f"swappped dict: {swap_dct}")
"""

print("Exercise 4.5")

pass

print("---")

"""
Exercise 4.6

Task:
------
Count the number of times each letter appears in the string 'ccctcctttttcc'
and print the resulting dictionary.

s = 'ccctcctttttcc'
counts = {}
for char in s:
    counts[char] = counts.get(char, 0) + 1
print(counts)

"""

s = 'ccctcctttttcc'



print("Exercise 4.6")

pass

print("---")

"""
Exercise 4.7

Task:
------
Given the dictionary of responses_mapping = {'j':'jazz', 'p':'pop'},
and the string responses = 'jjjpjjpppppjj',
print the list of corresponding words.


responses_mapping = {'j':'jazz','p':'pop'}
responses = 'jjjpjjpppppjj'

words = [responses_mapping[r] for r in responses]

print(words)
"""

responses_mapping = {'j':'jazz','p':'pop'}
responses = 'jjjpjjpppppjj'

print("Exercise 4.7")

pass

print("---")

"""
Exercise 4.8

Task:
------
Merge the following two dictionaries into one:
{'a': 1, 'b': 2} and {'c': 3, 'd': 4}


dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = dict1 | dict2
print(merged_dict)

"""

print("Exercise 4.8")

pass

print("---")

"""
Exercise 4.9

Task:
------
Starting from the dictionary {'zebra': 10, 'dolphin': 25, 'alligator': 3, 'monkey': 5, 'pig': 9},
create a new one whose keys are sorted alphabetically.

dct = {'zebra': 10, 'dolphin': 25, 'alligator': 3, 'monkey': 5, 'pig': 9}

sorted_dict = {}
for k in sorted(dct):
    sorted_dict[k] = dct[k]

print(sorted_dict)
"""

print("Exercise 4.9")

pass

print("---")

"""
Exercise 4.10

Task:
------
Starting from the dictionary {'zebra': 10, 'dolphin': 25, 'alligator': 3, 'monkey': 5, 'pig': 9},
create a new one whose values appear in increasing order.

sorted_items = sorted(dct.items(), key=lambda item: item[1])

new_dict = {}
for key, value in sorted_items:
    new_dict[key] = value

print(new_dict)
"""

print("Exercise 4.10")

pass

print("---")