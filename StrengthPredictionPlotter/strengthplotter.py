import os
import csv
import matplotlib.pyplot as plt
import numpy as np
import datetime


#read lines from 'data.csv' file
with open('strength.csv', 'r') as f:
    reader = csv.reader(f)
    lines = list(reader)

lines_dates=np.array(lines)[:,0]
data_dict={}
for i in range(int((len(lines[0])-1)/3)):
    data_dict[str(lines[0][i*3+1])]=[]
    for j in range(len(lines)):
        data_dict[str(lines[0][i*3+1])].append([float(lines[j][i*3+2]),float(lines[j][i*3+3])])



x=[0]
for date in lines_dates[1:]:
    x.append((datetime.datetime.strptime(date,'%m/%d')-datetime.datetime.strptime('7/28','%m/%d')).days)


keys=list(data_dict.keys())
for key in keys:
    y_weights=np.array(data_dict[key])[:,0]
    y_reps=np.array(data_dict[key])[:,1]
    z_weights=np.polyfit(x,y_weights,1)
    p_weights=np.poly1d(z_weights)
    z_reps=np.polyfit(x,y_reps,1)
    p_reps=np.poly1d(z_reps)

    

    fig, ax1 = plt.subplots()
    #Plot weight
    color = 'tab:blue'
    ax1.set_xlabel('Days')
    ax1.set_ylabel('Weight', color=color)
    ax1.plot(x, y_weights, color=color)
    ax1.tick_params(axis='y', labelcolor=color)


    #Plot reps
    ax2 = ax1.twinx()
    color = 'tab:orange'
    ax2.set_ylabel('Reps', color=color)
    ax2.plot(x, y_reps, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    #get p_reps at x=30
    print(key,": Weights Equation: ",p_weights,"\nReps Equation: ",p_reps)
    print(key,": Weight in 30 days: ",p_weights(max(x)+30),", Reps in 30 days: ",p_reps(max(x)+30))
    print(key,": Weight in 60 days: ",p_weights(max(x)+60),", Reps in 60 days: ",p_reps(max(x)+60))

    fig.tight_layout()
    plt.show()
    