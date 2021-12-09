import csv
import collections
import sys
inp_file = sys.argv[1]
out_file = sys.argv[2]

string_dict = collections.defaultdict(str)
counter = 1
with open(inp_file, mode='r') as csv_file, open(out_file, 'w') as out_f:
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_writer = csv.writer(out_f)
    line_count = 0
    for row in csv_reader:
        line_count+=1
        size = int(row[2])
        if size == 0:
            continue
        csv_writer.writerow(row)
        if line_count % 1000000 == 0:
            print(line_count)
            print(row)