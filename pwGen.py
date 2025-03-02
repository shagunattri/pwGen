import string
import random
import sys
import pyperclip
import pwnedpasswords
from math import log
from pyfiglet import Figlet
from functools import reduce

custom_ascii = Figlet(font='graffiti')
print(custom_ascii.renderText('pwGen'))

sizeError = True
nameError = True
fileError = True
combinedError = True

while sizeError:
    try:
        N = int(input("[+] Enter size of string --> "))
        if(N <= 0):
            raise NameError
        sizeError = False
    except:
        print('[!] Error --> Please enter a valid number')

print()

while nameError:
    try:
        n = int(input("[+] Enter number of key-word/s --> "))
        if(n <= 0):
            raise NameError
        nameError = False
    except:
        print('[!] Error --> Please enter a valid number')


lst = []

while combinedError:
    try:
        for i in range(0, n):
            key = input('[+] Enter the word --> ')
            lst.append(key)
        print('[+] Check: This is the list for your key-word/s -->', lst)
        combined = reduce(lambda acc, item: acc + "" + item, lst)
        combinedError = False
    except:
        print('[!] Error --> Please Enter atleast one key-word')

# print(combined)

choice = input("[+] Obsfucate the passcode? [Y/n] ")
savef = input("[+] Do you want to save the file? [Y/n]")


res = ''.join(random.choices(combined, k=N))

if choice == 'n' or choice == 'N':
    pass
else:
    res = res.replace('a', '4').replace('e', '3').replace('i', '!').replace('l', '1').replace('t', '7').replace('s', '$').replace('o', '0')


if savef == 'n' or savef == 'N':
    print()
    print("[+] The generated random string --> " + str(res))
    print()
else:
    while fileError:
        try:
            filename = input("[+] Input the Filename --> ")
            with open(filename, mode='w') as f:
                f.write(res)
                f.close()
            fileError = False
        except:
            print('[!] Please enter a valid file name')


print("[+] Checking gennerated password against the pwnedpassword database...")
checkpwn = pwnedpasswords.check(res,plain_text=True)
print(f'[+] {res} has {checkpwn} entries in the pwnedpassword database...')
if checkpwn == 0:
    print("[+] Hurray! Your password is unique!! Carry on!")
else:
    print("[!] {res} was found in the pwnedpassword database. You should probably change it!")
print()


ctoc = input("[+] Copy password to clipborad? [Y/n] ")
if ctoc == 'n' or ctoc == 'N':
    pass
else:
    pyperclip.copy(res)
    print("[+] Password copied to clipboard...")

entropy = ((log(82)/log(2)) * len(res))

print('')
print('+------------------------------------+---------------------+')
print('| Password                           | Entropy             |')
print('+------------------------------------+---------------------+')
print(' %s                           %s                  ' % (res, entropy))