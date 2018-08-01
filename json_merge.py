'''''''''''''''
The script is capable of combining the data from two separate
csv file sources into a single json-file.
    The directory of the two files is needed
'''''''''''''''
import numpy as np
import csv
import json


def Output_json(Directory=False):
    val1 = []
    val2 = []
    id1 = []
    id2 = []
    Output = [[]] * 3
    in_file_csv1 = open(Directory + "1.csv", 'rb')
    reader1 = csv.reader(in_file_csv1, delimiter=',')
    in_file_csv2 = open(Directory + "2.csv", 'rb')
    reader2 = csv.reader(in_file_csv2, delimiter=',')
    for _ in range(0, 1):
        next(reader1)
        next(reader2)
        for row1 in reader1:
            id1 = np.append(id1, int(row1[0]))
            val1 = np.append(val1, int(row1[1]))
        for row2 in reader2:
            id2 = np.append(id2, int(row2[0]))
            val2 = np.append(val2, int(row2[1]))
    data1 = (np.stack([id1, val1])).T
    data2 = (np.stack([id2, val2])).T
    for a in range(data2.shape[0]):
        for b in range(data1.shape[0]):
            if data2[a, 0] == data1[b, 0]:
                Output[b] = np.append(Output[b], data2[a, 1])
    myobject = []
    with open(Directory + 'out.json', 'w') as outfile:
        for c, value in enumerate(Output, 1):
            Output_list = Output[c - 1].tolist()
            myobject.append({'id': c, 'val1': data1[c - 1, 1].astype(int), 'val2': Output_list})
        out = json.dumps(myobject, indent=2, sort_keys=True)
        outfile.write(out)


if __name__ == "__main__":
    Output_json(Directory="/home/silab62/HEP/Scripts/DaMedic/")
