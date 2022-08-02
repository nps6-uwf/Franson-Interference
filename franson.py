'''
Franson Interference Experiment
Author: Nick Sebasco
Version: 1
'''

import matplotlib.pyplot as pt
import seaborn as sns
import numpy
from sys import argv


HEAD_LENGTH = 5 # number of rows of header data (int time, col names, ...)


def read(fpath):
    ''' Read data from extracted from the quED.  fpath is a string
    representing the file path of the data text file.
    '''
    with open(fpath, "r") as f:
        l = f.readlines()
        head = l[:HEAD_LENGTH]
        rows = [[float(j) for j in i.split(" ") if j.strip() != ""] 
            for i in l[HEAD_LENGTH:]]
        columns = [[r[i] for r in rows] for i in range(len(rows[0]))]
    return (head, columns)


def plot_data(
    showCoin=True,
    showSingleScan=True,
    showSingleStatic=True,
    darkgrid=True,
    palette="tab10"):
    ''' The parameter showCoin refers to whether or not to plot the 
    coincidence interference.  showSingleScan referes to whether or not
    to plot the single count for the scanned Michelson interferometer.  
    showSingleStatic determines whether or not to include the static
    Michelson.  If darkgrid is set to false teh plot background becomes
    white.  The color palette can be changed by passing any valid
    matplotlib color palette.
    '''
    head, data = read(argv[1])
    position = data[0]

    integration_time = head[3]
    stepsize = abs(position[1] - position[0])

    print("integration time:", integration_time)
    print("stepsize:", stepsize) # infer stepsize

    sns.set_theme(style="darkgrid" if darkgrid else "whitegrid",
        palette=palette)

    if showCoin:
        sns.lineplot(x="X", y="Y",
             data={"X":position,"Y":data[4]})
    if showSingleScan:
        sns.lineplot(x="X", y="Y",
                data={"X":position,"Y":data[1]})
    if showSingleStatic:
        sns.lineplot(x="X", y="Y",
                data={"X":position,"Y":data[3]})

    pt.show()


if __name__=="__main__": plot_data()





