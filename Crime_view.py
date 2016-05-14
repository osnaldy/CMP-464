#Osnaldy Vasquez
import csv
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import statistics
from operator import add
year1 = []
year2 = []
year3 = []
year4 = []
with open('Louisiana.csv', 'r') as csvFile:
    reader = csv.DictReader(csvFile)
    for row in reader:
        m,d,y = row['OFFENSE DATE'].split('/')

        if int(y) >= 12 and int(y) <=13:
            if int(m) > 3 and int(y) == 13:
                pass
            else:
                year1.append(row['OFFENSE DATE'])

        if int(y) >= 13 and int(y) <= 14:
            if (int(y) == 13 and int(m) < 4) or (int(y) ==14 and int(m) > 3):
                pass
            else:
                year2.append(row['OFFENSE DATE'])

        if int(y) >= 14 and int(y) <= 15:
            if (int(y) == 14 and int(m) < 4) or (int(y) ==15 and int(m) > 3):
                pass
            else:
                year3.append(row['OFFENSE DATE'])

        if int(y) >= 15 and int(y) <= 16:
            if (int(y) == 15 and int(m) < 4) or (int(y) ==16 and int(m) > 3):
                pass
            else:
                year4.append(row['OFFENSE DATE'])

array = []
with open('Chicago.csv', 'r') as csvFile:
    reader = csv.DictReader(csvFile)
    dates = [row['Date'] for row in reader]
    rem = ' '
    for i in dates:
        time = i[:8]
        new = time.split(rem, 1)[0]
        array.append(new)

chicago_year1 = []
chicago_year2 = []
chicago_year3 = []
chicago_year4 = []

new = list(array)
for row in new:
    m,d,y = row.split('/')

    if int(y) >= 12 and int(y) <=13:
        if int(m) > 3 and int(y) == 13:
            pass
        else:
            chicago_year1.append(row)

    if int(y) >= 13 and int(y) <= 14:
        if (int(y) == 13 and int(m) < 4) or (int(y) ==14 and int(m) > 3):
            pass
        else:
            chicago_year2.append(row)

    if int(y) >= 14 and int(y) <= 15:
        if (int(y) == 14 and int(m) < 4) or (int(y) ==15 and int(m) > 3):
            pass
        else:
            chicago_year3.append(row)

    if int(y) >= 15 and int(y) <= 16:
        if (int(y) == 15 and int(m) < 4) or (int(y) ==16 and int(m) > 3):
            pass
        else:
            chicago_year4.append(row)

def total(arr):

    count = Counter()
    for i in arr:
        key = int(i[:2].replace('/', ''))
        count[key] = count.get(key,0)+1
    return count

def values(arr):
    num = []
    for month in range(1,13):
        num.append(arr[int(month)])
    return num
def main():

    #This will get the total count of crime for each month

    #count of Crimes for Louisiana
    l1 = total(year1)
    l2 = total(year2)
    l3 = total(year3)
    l4 = total(year4)

    #count of Crimes for Chicago
    c1 = total(chicago_year1)
    c2 = total(chicago_year2)
    c3 = total(chicago_year3)
    c4 = total(chicago_year4)

    chicago_1 = values(c1)
    chicago_2 = values(c2)
    chicago_3 = values(c3)
    chicago_4 = values(c4)
    print 'Chicago crime Per month'
    print chicago_1
    print chicago_2
    print chicago_3
    print chicago_4
    print
    newarr1 = map(add, chicago_1, chicago_2)
    newarr2 = map(add, chicago_3, chicago_4)
    newarr3 = map(add, newarr1, newarr2)
    print 'Sum crimes per month for all four years in Chicago'
    print newarr3
    print
    new_chicago_avg = []
    for i in newarr3:
        new_chicago_avg.append(i/4)
    print 'Average crime per month for all four years in Chicago'
    print new_chicago_avg
    print

    #Values of crimes for each month of Louisiana
    louisiana_1 = values(l1)
    louisiana_2 = values(l2)
    louisiana_3 = values(l3)
    louisiana_4 = values(l4)
    print 'Louisiana crime Per month'
    print louisiana_1
    print louisiana_2
    print louisiana_3
    print louisiana_4
    print

    newarr4 = map(add, louisiana_1, louisiana_2)
    newarr5 = map(add, louisiana_3, louisiana_4)
    newarr6 = map(add, newarr4, newarr5)
    print 'Sum crimes per month for all four years in Louisiana'
    print newarr6
    print

    new_louisiana_avg = []
    for i in newarr6:
        new_louisiana_avg.append(i/4)
    print 'Average crime per month for all four years in Louisiana'
    print new_louisiana_avg
    print

    weather_l_1 = [46, 46, 42, 59, 66, 69, 73, 73, 73, 56, 47, 48]
    weather_l_2 = [32, 44, 46, 57, 62, 72, 71, 72, 72, 61, 46, 43]
    weather_l_3 = [37, 38, 55, 56, 61, 71, 70, 72, 72, 58, 42, 48]
    weather_l_4 = [39, 41, 55, 63, 67, 71, 73, 70, 70, 58, 55, 53]
    suml = map(add, weather_l_1, weather_l_2)
    suml1 = map(add, weather_l_3, weather_l_4)
    total_l = map(add, suml, suml1)
    louisiana_weather_total = []
    for i in total_l:
        louisiana_weather_total.append(i/4)
    print 'Average weather from 2012 - 2015 for Louisiana'
    print louisiana_weather_total
    print


    weather_c_1 = [18, 19, 22, 35, 47, 53, 64, 58, 58, 40, 29, 29]
    weather_c_2 = [10, 9, 21, 33, 47, 55, 60, 59, 59, 43, 28, 18]
    weather_c_3 = [17, 8, 24, 35, 48, 59, 58, 64, 64, 43, 25, 26]
    weather_c_4 = [17, 20, 33, 34, 50, 59, 60, 59, 59, 42, 35, 33]
    sum2 = map(add, weather_c_1, weather_c_2)
    sum3 = map(add, weather_c_3, weather_c_4)
    total_c = map(add, sum2, sum3)
    chicago_weather_total = []
    for i in total_c:
        chicago_weather_total.append(i/4)
    print 'Average weather from 2012 - 2015 for Chicago'
    print chicago_weather_total
    print

    m = range(0,12)
    print 'Correlation between between all the years for Chicago and Louisiana'
    lou_chi_2012_2015 = statistics.correlation(new_chicago_avg, new_louisiana_avg)
    print lou_chi_2012_2015
    print
    print 'Correlation between the total crime of Louisiana and the Weather for the same period of time'
    louisiana_weather_correlation = statistics.correlation(new_louisiana_avg, louisiana_weather_total)
    print louisiana_weather_correlation
    print
    print 'Correlation between the total crime of Chicago and the Weather for the same period of time'
    chicago_weather_correlation = statistics.correlation(new_chicago_avg, chicago_weather_total)
    print chicago_weather_correlation

    plt.plot(m, new_louisiana_avg, marker = 'o',color='purple', label="Louisiana 2012-2015")
    plt.plot(m, new_chicago_avg, marker= 'o', color='green', label="Chicago 2012-2015")
    plt.title("Osnaldy Vasquez\nCrime Correlation between Chicago and Louisiana for 2012 - 2015\nCorrelation = 0.706490238246", fontsize= 'medium')
    plt.xticks(np.arange(12), ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov',' Dec'))
    plt.xlabel("Months")
    plt.ylabel('Crimes')
    plt.legend(loc = 4,fontsize = 'x-small')
    plt.show()
    #
    plt.plot(m, louisiana_1, marker = 'o',color='red', label="Louisiana 2012")
    plt.plot(m, louisiana_2, marker = 'o',color='purple', label="Louisiana 2013")
    plt.plot(m, louisiana_3, marker = 'o',color='pink', label="Louisiana 2014")
    plt.plot(m, louisiana_4, marker= 'o', color='green', label="Louisiana 2015")
    plt.title("Osnaldy Vasquez\nCrime for Louisiana 2012 - 2015")
    plt.xticks(np.arange(12), ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov',' Dec'))
    plt.xlabel("Months")
    plt.ylabel('Crimes')
    plt.legend(loc = 4,fontsize = 'x-small')
    plt.show()
    #
    plt.plot(m, chicago_1, marker = 'o',color='red', label="Chicago 2012")
    plt.plot(m, chicago_2, marker = 'o',color='purple', label="Chicago 2013")
    plt.plot(m, chicago_3, marker = 'o',color='pink', label="Chicago 2014")
    plt.plot(m, chicago_4, marker= 'o', color='green', label="Chicago 2015")
    plt.title("Osnaldy Vasquez\nCrime for Chicago 2012 - 2015")
    plt.xticks(np.arange(12), ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov',' Dec'))
    plt.xlabel("Months")
    plt.ylabel('Crimes')
    plt.legend(loc = 4,fontsize = 'x-small')
    plt.show()

    plt.plot(m, new_louisiana_avg, marker = 'o',color='blue', label="Crime 2012-2015")
    plt.plot(m, louisiana_weather_total, marker= 'o', color='red', label=" Weather 2012-2015")
    plt.title("Osnaldy Vasquez\nCorrelation between the weather and the crime for Louisiana\nCorrelation = 0.696352921783", fontsize= 'medium')
    plt.xticks(np.arange(12), ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov',' Dec'))
    plt.xlabel("Months")
    plt.ylabel('Crimes')
    plt.legend(loc = 2,fontsize = 'x-small')
    plt.show()

    plt.plot(m, new_chicago_avg, marker = 'o',color='green', label="Crime 2012-2015")
    plt.plot(m, chicago_weather_total, marker= 'o', color='pink', label=" Weather 2012-2015")
    plt.title("Osnaldy Vasquez\nCorrelation between the weather and the crime for Chicago\nCorrelation = 0.647656528", fontsize= 'medium')
    plt.xticks(np.arange(12), ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov',' Dec'))
    plt.xlabel("Months")
    plt.ylabel('Crimes')
    plt.legend(loc = 2,fontsize = 'x-small')
    plt.show()

main()