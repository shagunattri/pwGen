import string
import random
import sys
import pyperclip
from math import log
from pyfiglet import Figlet

custom_ascii = Figlet(font='graffiti')
print(custom_ascii.renderText('pwGen'))

nameError = True
fileError = True

while nameError:
    try:
        N = int(input("[+] Enter size of string --> "))
        if(N <= 0):
            raise NameError
        nameError = False
    except:
        print('Please enter a valid number')

lst = []

n = int(input("Enter number of phrases --> "))

for i in range(0, n):
    phrases = input('Enter the phrase --> ')

    lst.append(phrases)

print('This is the list for your phrases -->', lst)

choice = input("[+] Obsfucate the passcode? [Y/n] ")
savef = input("[+] Do you want to save the file? [Y/n]")

test = ['pool', '44223', '00-2', 'srm']

# res = ''.join(random.choices(string.ascii_uppercase +
#                              string.digits + string.ascii_lowercase + string.punctuation, k=N))

# res = ''.join(random.choices(test[0] + test[1] + test[2] + test[3], k=N))

res = ''.join(random.choices(lst, k=N))

if choice == 'n' or choice == 'N':
    pass
else:
    res = res.replace('a', '4').replace('e', '3').replace('i', '!').replace(
        'l', '1').replace('t', '7').replace('s', '$').replace('o', '0')


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
            print('Please enter a valid file name')


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
