import matplotlib.pyplot as plt
import csv

def plot_stats(size):
    size = str(size)
    real = '50M/real/'+size+'.txt'
    synthetic = '50M/synthetic/'+size+'.txt'
    x = []
    y = []
    with open(real,'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            x.append(float(row[0]))
            y.append(float(row[1]))
    plt.plot(x,y, label='real trace', color='red',linewidth=2)

    x1=[]
    y1=[]
    with open(synthetic,'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            x1.append(float(row[0]))
            y1.append(float(row[1]))
    plt.plot(x1,y1, label='synthetic trace', color='green',linewidth=2)

    plt.xlabel('Num Ops (in Millions)')
    plt.ylabel('Hit Ratio')
    plt.title('Hit Ratio vs Num Ops. Cache Size(in MB) = '+size)
    file_name = 'graphs/cacheSize_vs_hitRatio_500M.png'
    # plt.legend()
    plt.legend(loc="lower right")

    count = 0
    for a,b in zip(x1,y1):
        count +=1 
        if count%5==0:
            plt.annotate(str(b), # this is the text
                        (a,b), # these are the coordinates to position the label
                        textcoords="offset points", # how to position the text
                        xytext=(0,-10), # distance from text to points (x,y)
                        ha='center') # horizontal alignment can be left, right or center
    count = 0
    for a,b in zip(x,y):
        count +=1 
        if count%5==0:
            plt.annotate(str(b), # this is the text
                        (a,b), # these are the coordinates to position the label
                        textcoords="offset points", # how to position the text
                        xytext=(0,3), # distance from text to points (x,y)
                        ha='center') # horizontal alignment can be left, right or center

    # plt.savefig(file_name)
    plt.show()

plot_stats(5000)