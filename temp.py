import csv

arr1 = []
arr2 = []
arr3 = []
arr4 = []
arr5 = []
arr6 = []
arr7 = []
arr8 = []
arr9 = []
arr10 = []
arr11 = []
arr12 = []
with open('CustomHistoryChicago4.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        m,d,y = row['CDT'].split('/')
        if int(m) == 1:
            arr1.append(int(row['MeanDew PointF']))
        if int(m) == 2:
            arr2.append(int(row['MeanDew PointF']))
        if int(m) == 3:
            arr3.append(int(row['MeanDew PointF']))
        if int(m) == 4:
            arr4.append(int(row['MeanDew PointF']))
        if int(m) == 5:
            arr5.append(int(row['MeanDew PointF']))
        if int(m) == 6:
            arr6.append(int(row['MeanDew PointF']))
        if int(m) == 7:
            arr7.append(int(row['MeanDew PointF']))
        if int(m) == 8:
            arr8.append(int(row['MeanDew PointF']))
        if int(m) == 8:
            arr9.append(int(row['MeanDew PointF']))
        if int(m) == 10:
            arr10.append(int(row['MeanDew PointF']))
        if int(m) == 11:
            arr11.append(int(row['MeanDew PointF']))
        if int(m) == 12:
            arr12.append(int(row['MeanDew PointF']))
array = []
a = sum(arr1)/len(arr1)
array.append(a)
b = sum(arr2)/len(arr2)
array.append(b)
c = sum(arr3)/len(arr3)
array.append(c)
d = sum(arr4)/len(arr4)
array.append(d)
e = sum(arr5)/len(arr5)
array.append(e)
f = sum(arr6)/len(arr6)
array.append(f)
g = sum(arr7)/len(arr7)
array.append(g)
h = sum(arr8)/len(arr8)
array.append(h)
i = sum(arr9)/len(arr9)
array.append(i)
j = sum(arr10)/len(arr10)
array.append(j)
k = sum(arr11)/len(arr11)
array.append(k)
l = sum(arr12)/len(arr12)
array.append(l)
print array
