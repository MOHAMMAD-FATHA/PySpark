"""
@Author: Mohammad Fatha
@Date: 2021-11-24
@Last Modified by: Mohammad Fatha
@Title : Twitter Analysis using spark in python
"""
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd


def animate(i):
    data = pd.read_csv('/home/fatha/Documents/Spark/TwitterAnalysisSpark/data.csv')
    x1 = data['pos']
    x2 = data['neg']

    y1 = data['pos_count']
    y2 = data['neg_count']
    plt.cla()
    plt.bar(x1,y1,label="positive")
    plt.bar(x2,y2,label="negative")
    plt.xlabel("Sentiments")
    plt.ylabel("Count")
    plt.legend()
    plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()