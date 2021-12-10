import matplotlib.pyplot as plt
import csv

def plot_stats(size, num_ops, save_flag):
    num_ops = str(num_ops)
    size = str(size)
    real = num_ops+'M/real/'+size+'.txt'
    synthetic = num_ops+'M/synthetic/'+size+'.txt'
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
    # plt.legend()
    plt.legend(loc="lower right")

    count = 0
    for a,b in zip(x1,y1):
        count +=1 
        if count%3==0:
            plt.annotate(str(b), # this is the text
                        (a,b), # these are the coordinates to position the label
                        textcoords="offset points", # how to position the text
                        xytext=(0,-10), # distance from text to points (x,y)
                        ha='center') # horizontal alignment can be left, right or center
    count = 0
    for a,b in zip(x,y):
        count +=1 
        if count%3==0:
            plt.annotate(str(b), # this is the text
                        (a,b), # these are the coordinates to position the label
                        textcoords="offset points", # how to position the text
                        xytext=(0,3), # distance from text to points (x,y)
                        ha='center') # horizontal alignment can be left, right or center

    if save_flag:
        file_name = '../graphs/ops_vs_hr_'+size+'.png'
        plt.savefig(file_name)
    # plt.show()
    plt.clf()

num_ops = 50
save_flag = True
size = 1000
max_cache_size = 5000
while size <= max_cache_size:
    plot_stats(size, num_ops, save_flag)
    size += 1000