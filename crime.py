import csv

year = []
with open('Louisiana.csv', 'rU') as csvFile:
    reader = csv.DictReader(csvFile)
    for row in reader:
        m,d,y = row['OFFENSE DATE'].split('/')
        if int(y) >= 13 and int(y) <= 14:
            if (int(y) == 13 and int(m) < 4) or (int(y) ==14 and int(m) > 3):
                pass
            else:
                year.append(row['OFFENSE DATE'])

    count = 0
    for years in year:
        count +=1
        print count, years


 #plt.hist(x=m, bins=range(0,14), weights=louisiana_1, color='red')
    #plt.show()
    #plt.hist(x=m, bins=range(0,14), weights=louisiana_year2, color='blue')
    # plt.plot(m, louisiana_1, marker = 'o',color='blue', label="2012")
    #plt.plot(m, louisiana_2, marker = 'o', color='red', label="2013")

     #
    # plt.plot(m, chicago_1, marker = 'o',color='blue', label="2012")
    # plt.plot(m, chicago_2, marker = 'o', color='red', label="2013")
    # plt.plot(m, chicago_3, marker = 'o',color='purple', label="2014")
    # plt.plot(m, chicago_4, marker= 'o', color='green', label="2015")
    # plt.title("Osnaldy Vasquez\nChicago Crime between 2012 - 2015")
    # plt.xticks(np.arange(12), ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov',' Dec'))
    # plt.xlabel("Months")
    # plt.ylabel('Crimes')
    # plt.legend(loc = 2,fontsize = 'x-small')
    #plt.show()