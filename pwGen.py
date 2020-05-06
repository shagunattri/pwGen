import string 
import random 
import sys


N = int(input("Enter size of string --> "))
counter = int(input("How many password combinations do you need! --> "))


def run(N):
    choice = input("Obsfucate the passcode? [Y/n] ")
    if choice == 'n':
	    obs = False
    else:
	    obs = True
    
    res = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase + string.punctuation, k = N)) 
    if obs:
        res = res.replace('a', '4').replace('e', '3').replace('i', '!').replace('l', '1').replace('t', '7').replace('s', '$').replace('o', '0')
    else:
        pass
    return print("The generated random string : " +str(res))


for i in range(counter):
    run(N)
