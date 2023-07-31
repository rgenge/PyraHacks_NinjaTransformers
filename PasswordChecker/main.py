
import sys
import secrets
import string

def checker(password):
    s, c, d, sp = 0, 0, 0, 0
    capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    small = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    special="$#@!*_"
    if (len(password) >= 10):
        for i in password:
            if(i in small):
                s+=1
            if(i in capital):
                c+=1
            if(i in digits):
                d+=1
            if(i in special):
                sp+=1
    else:
        print ("Invalid Password, your password must be have more than 10 chars")
        sys.exit()

    if (s >= 1  & c >= 1 & d >= 1& sp >= 1):
        print("Valid Password:Don't forget to not to use personal info")
    else:
        print ("Invalid Password You must have one small, one digit, one capital and one special char")

if __name__ == "__main__":
    print("For security purposes never uses personal info in your password\n like name, mom, birth date")
    generator = input("If you want me to generate a password for you type 'yes', if not just press Enter")
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    alphabet = letters+digits+special_chars
    if (generator == "yes"):
        pass_size = input("Type how long is the password you want")
        generated = ''
        for i in range(int(pass_size)):
             generated += ''.join(secrets.choice(alphabet))
        print( generated)
        sys.exit()
    password = input("Type the password you want to check: \n")
    checker(password)
