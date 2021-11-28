import matplotlib.pyplot as plt
import csv

x = []
y = []
with open('cacheSize_vs_hitRatio_rt.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[1]))
plt.plot(x,y, label='real trace', color='red',linewidth=2)

x1=[]
y1=[]
with open('cacheSize_vs_hitRatio_synthetic.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x1.append(float(row[0]))
        y1.append(float(row[1]))
plt.plot(x1,y1, label='synthetic trace', color='green',linewidth=2)

plt.xlabel('Cache Size (in MB)')
plt.ylabel('Hit Ratio')
plt.title('Hit Ratio vs Cache Size. Total Ops = 500M')
file_name = 'graphs/cacheSize_vs_hitRatio_500M.png'
# plt.legend()
plt.legend(loc="lower right")

count = 0
for a,b in zip(x1,y1):
    count +=1 
    if count%30==0:
        plt.annotate(str(b), # this is the text
                    (a,b), # these are the coordinates to position the label
                    textcoords="offset points", # how to position the text
                    xytext=(0,-10), # distance from text to points (x,y)
                    ha='center') # horizontal alignment can be left, right or center
count = 0
for a,b in zip(x,y):
    count +=1 
    if count%30==0:
        plt.annotate(str(b), # this is the text
                    (a,b), # these are the coordinates to position the label
                    textcoords="offset points", # how to position the text
                    xytext=(0,3), # distance from text to points (x,y)
                    ha='center') # horizontal alignment can be left, right or center

# plt.savefig(file_name)
plt.show()