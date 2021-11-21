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
        if line_count % 1000000 == 0:
            print(line_count)
            print(row)
        # if line_count > 200000000:
        #     break
        object_id = row[1]
        int_id = 0
        if object_id in string_dict:
            int_id = string_dict[object_id]
        else:
            int_id = counter
            counter +=1
            string_dict[object_id] = int_id
        row[1] = str(int_id)
        csv_writer.writerow(row)
        # print(row)