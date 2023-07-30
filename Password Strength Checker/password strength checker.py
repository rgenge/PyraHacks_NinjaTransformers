#password strength checker

password = ''

while True:
    password = input("\nEnter your password: ")

    points = 0

    symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(",")","_","-","+","=","{","}","[","]"]

    #checks
    if len(password) < 8:
        while len(password) < 8:
            password = input("\nYour password is too short, Enter a new password: ")

    if len(password) > 8:
        points = points + 5

    if len(password) > 12:
        points = points + 5

    if password.isalpha():
        points = points + 5

    if lambda symbols, password: any(filter(lambda x: x in password, symbols)):
        points = points + 5

    if any(char.isdigit() for char in password):
        points = points + 5

    if any(element.isupper() for element in password):
        points = points + 5

    if any(element.islower() for element in password):
        points = points + 5

    #strength determination
    if points == 5 or points == 10:
        print("\nYour password strength is weak!")
        quit = input("\nPress enter to input another password or q to quit.")
        if quit == "q":
            break
    elif points == 15:
        print("\nYour password strength is medium.")
        quit = input("\nPress enter to input another password or q to quit.")
        if quit == "q":
            break
    elif points == 20 or points == 25:
        print("\nYour password strength is good.")
        quit = input("\nPress enter to input another password or q to quit.")
        if quit == "q":
            break
    elif points == 30 or points == 35:
        print("\nYou password strength is excellent!")
        quit = input("\nPress enter to input another password or q to quit.")
        if quit == "q":
            break