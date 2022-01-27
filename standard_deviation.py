import math
import csv

with open("data.csv", newline = "") as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]

def mean(data):
    n = len(data)
    total = 0
    for i in data:
        total = total + int(i)

    mean = total/n
    return(mean)


square_list = []
for number in data:
    a = int(number)-mean(data)
    a = a**2
    square_list.append(a)

sum = 0
for i in square_list:
    sum = sum+i

result = sum/(len(data)-1)
standard_deviation = math.sqrt(result)
print(standard_deviation)