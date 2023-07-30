import pyinputplus as pyip
from random import choice
import time

def game_loop():
    start_number = input("Start Range Number")
    end_number = input("End Range Number")
    print('Round the number like this 0.66 = 0.7, or 0.3313 = 0.3')
    MathSymbols = ['+', '-', '/' , '*']
    Numbers = [num for num in range(int(start_number), int(end_number))]
    points = 0
    max_points = 6
    start_time = time.time()
    while points < max_points:
        Symbol = choice(MathSymbols)
        Equation = str(choice(Numbers)) + ' ' + Symbol + ' ' + str(choice(Numbers))
        solution = round(eval(Equation), 1)
        result = pyip.inputNum(prompt=Equation + ' = ')

        if result == solution:
            points += 1
            print("Corret! Total points: ", points)
        else:
            points -= 1
        if pyip.inputStr("Press Enter", blank = True) == "stop":
            break
        end_time = time.time()
    elapsed_time = round(end_time - start_time, 2)
    print("You reached ",max_points, " points with time: ", elapsed_time, "s")

if __name__ == "__main__":
    game_loop()
