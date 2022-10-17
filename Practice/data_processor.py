import csv
import pandas as pd

csv_reader = csv.reader(open("origin_sum.csv"))

def convertToOneLine():
    sum = []
    count = 0
    for line in csv_reader:
        if count == 0:
            count = 1
            continue
        sum.append(line[3])
    print(sum)
    sum1 = pd.DataFrame(data=sum)
    sum1.to_csv('origin_avg.csv', encoding='gbk')

def convertOneLineTo100():
    data = [[]]
    for i in range(100):
        data[0].append('input' + str(i))
    data[0].append('label')
    csv_reader = csv.reader(open('origin_avg.csv'))

    count = 0
    for i in range(12):
        data.append([])

    for line in csv_reader:
        data[1 + count % 12].append(line[1])
        count += 1

    for i in range(12):
        data[i + 1].append(0)
    data2 = pd.DataFrame(data=data)
    data2.to_csv('data.csv', encoding='gbk')

convertOneLineTo100()