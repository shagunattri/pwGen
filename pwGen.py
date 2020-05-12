import string
import random
import sys
import pyperclip
from pyfiglet import Figlet


custom_ascii = Figlet(font='graffiti')
print(custom_ascii.renderText('pwGen'))


N = int(input("[+] Enter size of string --> "))
choice = input("[+] Obsfucate the passcode? [Y/n] ")
savef = input("[+] Do you want to save the file? [Y/n]")

   
if choice == 'n':
    pass
else:
    res = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase + string.punctuation, k=N))
    res = res.replace('a', '4').replace('e', '3').replace('i', '!').replace('l', '1').replace('t', '7').replace('s', '$').replace('o', '0')



if savef == 'n':
    print("[+] The generated random string --> " + str(res))
else:
    filename = input("[+] Input the Filename --> ")
    with open(filename, mode='w') as f:
        f.write(res)
        f.close()


ctoc = input("[+] Copy password to clipborad? [Y/n] ")
if ctoc == 'N':
    pass
else:
    pyperclip.copy(res)
    print("[+] Password copied to clipboard...")   
