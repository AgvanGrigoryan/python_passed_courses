##sphere volume
import math
def vol(rad):
    return 4/3*math.pi*(rad**3)

def ran_check(num, low, high):
    return low<=num<=high

def count_character_cases(string):
    counter = {'lower': 0, 'uppers': 0}
    for letter in string:
        if not letter.isalpha():
            continue
        if letter.islower():
            counter['lower']+=1
        else:
            counter['upper']+=1

    print(f"""No. of Upper case characters: {uppers}
No. of Lower case characters: {lowers}""")
    return counter



def unique_list(lst):
    return list(set(lst))

def multiply(numbers):
    total = 1
    for num in numbers:
        total*=num
    return total

def palindrome(s):
    return s==s[::-1]




import string
def ispangram(text, alphabet=string.ascii_lowercase):
    text = text.lower()
    for letter in alphabet:
        if letter not in text:
            return False
    return True


def his_ispangram(text,alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset<=set(text.lower())

