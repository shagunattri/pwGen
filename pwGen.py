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


def output():
    if savef == "n":
        print("[+] The generated random string --> " + str(run(N)))
    else:
        filename = input("[+] Input the Filename --> ")
        sys.stdout = open(filename, 'w',encoding = 'utf-8')
        with open(filename, mode='r+') as f:
                f.write(str(run(N)))
                
   

if choice == 'n':
    obs = False
else:
    obs = True
    
def run(N):
    res = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase + string.punctuation, k=N))
    if obs:
        res = res.replace('a', '4').replace('e', '3').replace('i', '!').replace('l', '1').replace('t', '7').replace('s', '$').replace('o', '0')
    else:
        pass
    return res


def ctoc():
    if ccinput == 'n':
        pass
    else:
        print("[+] Password copied to clipboard...")
        pyperclip.copy()


output()    
ctoc()
