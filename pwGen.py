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
    obs = False
else:
    obs = True


def output():
    if savef == "n":
        print("[+] The generated random string --> " + str(run(N)))
    else:
        filename = input("[+] Input the Filename --> ")
        sys.stdout = open(filename, 'w',encoding = 'utf-8')
        with open(filename, mode='w') as f:
                f.write(str(run(N)))
                f.close()
                

def run(N):
    res = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase + string.punctuation, k=N))
    if obs:
        res = res.replace('a', '4').replace('e', '3').replace('i', '!').replace('l', '1').replace('t', '7').replace('s', '$').replace('o', '0')
        pyperclip.copy(res)
    else:
        pyperclip.copy(res)
    return res



output()    
