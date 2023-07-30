import random
import pandas as pd

df = pd.read_csv("dictionary.csv")
terms = df["term"].tolist()
definitions = df["meaning"].tolist()

while True:
    definition = random.choice(definitions)
    
    answer = input("Enter the term based on the definition\n" + definition + ": ")
    a = definitions.index(definition)

    try: 
        if terms.index(answer) == a and answer in terms:
            print("Correct!")
            del terms[a]
            del definitions[a]
            exit = input("press q to quit, any other key to be tested on another definition ")
            if exit == "q":
                break
        elif terms.infex(answer) != a and answer in terms:
            print("Wrong.")
            del terms[a]
            del definitions[a]
            exit = input("press q to quit, any other key to be tested on another definition ")
            if exit == "q":
                break

    except:
        print("Wrong.")
        print("Correct answer is: " + terms[a])
        del terms[a]
        del definitions[a]
        exit = input("press q to quit, any other key to be tested on another definition ")
        if exit == "q":
            break
    
exit()