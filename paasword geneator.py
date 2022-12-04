"""Create a program that takes the length of the password as input and generates a random
password of the same length. The strength of the password depends equally on the 4 properties
mentioned below. If the password generated randomly following the rules or constraints given
below, then that password is treated as good in terms of strength and accepted otherwise
ignore that password."""

import random

letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
              'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['1','2','3','4','5','6','7','8','9','0']
symbols=['!','@','#','$','%','^','&','*','(',')','-','+','=','?',':','~']
print("welcome to the passward genrator!")
nr_letters=int(input(f"how many letters would you like in your password: \n"))
nr_symbols=int(input(f"how many symbols would you like: \n"))
nr_numbers=int(input(f"how many numbers would you like :\n"))

if (nr_numbers+nr_symbols+nr_numbers)<=12:
    print("your passward must be 12 characater")

else:
    i = 0
    letters_char = ""
    while i < nr_letters:
        letters_index = random.randint(0, len(letters) - 1)
        i += 1
        a = letters[letters_index]
        letters_char += a
    p = (letters_char)
    s = (p[0].upper()) + p[1:]

    j = 0
    number_char = ""
    while j < nr_numbers:
        number_index = random.randint(0, len(numbers) - 1)
        j += 1
        b = numbers[number_index]
        number_char += b
    q = (number_char)

    k = 0
    symbol_char = ""
    while k < nr_symbols:
        symbol_index = random.randint(0, len(symbols))
        k += 1
        c = symbols[symbol_index]
        symbol_char += c
    r = (symbol_char)
    print(s + q + r)