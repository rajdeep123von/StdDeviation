import csv
import math

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data

def Mean(data):    
    n = len(data)
    total = 0
   
    for x in data:
       total+=int(x)
    
    mean = total/n
    return mean

squaredList =[]

for i in data:
    
    a = int(i)-Mean(data)
    a = a**2
    sqauredList.append(a)

sum = 0

for a in squaredList:
    sum = sum+a

result  = sum/(len(data)-1)    

StandardDeviation = math.sqrt(result)

print("The standard Deviation is: "+StandardDeviation)