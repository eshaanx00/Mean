import csv
from collections import Counter

with open("Height.csv",newline ="") as f:
    r = csv.reader(f)
    data = list(r)
data.pop(0)

list = []
for i in range(len(data)):
    num = data[i][2]
    list.append(float(num))

number_in_list = len(list)
total = 0
for i in list:
    total += i

mean = total / number_in_list
print("Mean is : ",mean)

n = Counter(list)
m_range = {
    "75-85":0,
    "85-95":0,
    "95-105":0,
    "105-115":0,
    "115-125":0,
    "125-135":0,
    "135-145":0,
    "145-155":0,
    "155-165":0,
    "165-175":0,
}
for height,occurrence in n.items():
    if 75 < float(height) < 85:
        m_range["75-85"]+=occurrence
    elif 85 < float(height) < 95:
        m_range["85-95"]+=occurrence
    elif 95 < float(height) < 105:
        m_range["95-105"]+=occurrence
    elif 105 < float(height) < 115:
        m_range["105-115"]+=occurrence
    elif 115 < float(height) < 125:
        m_range["115-125"]+=occurrence
    elif 125 < float(height) < 135:
        m_range["125-135"]+=occurrence
    elif 135 < float(height) < 145:
        m_range["135-145"]+=occurrence
    elif 145 < float(height) < 155:
        m_range["145-155"]+=occurrence
    elif 155 < float(height) < 165:
        m_range["155-165"]+=occurrence
    elif 165 < float(height) < 175:
        m_range["165-175"]+=occurrence
    
m1,m2=0,0
for range,occurrence in m_range.items():
    if occurrence > m2:
        m1,m2 = [int(range.split("-")[0]),int(range.split("-")[1])],occurrence

mode = float((m1[0]+m1[1])/2)
print("Mode is : ",mode)

list.sort()

if number_in_list % 2 == 0:
    n1=float(list[number_in_list//2])
    n2=float(list[number_in_list//2-1])
    median = (n1+n2)/2
else:
    median = float(list[number_in_list//2])

print("Median is : ",median)
