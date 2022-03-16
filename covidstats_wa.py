#-*-coding:utf8;-*-
#qpy:console
import csv
import datetime
#Function converts date tp Julian date
def dates_to_julian (stddate):
    fmt='%Y-%m-%d'
    sdtdate = datetime.datetime.strptime(stddate, fmt)
    sdtdate = sdtdate.timetuple()
    jdate = sdtdate.tm_yday
    return(jdate)


def julian_to_date (jdate):
    fmt = '%Y%j'
    datestd = datetime.datetime.strptime(jdate, fmt).date()
    return(datestd)

def findthedate(startdate, numdayssince):
    monthdays = [31,28,31,30,31,30,31,31,30,31,30,31]
    monthdaysleapyr = [31,29,31,30,31,30,31,31,30,31,30,31]
    if len(startdate)<3:
        finaldate = "Input Error, date not in correct format!"
    else:
        day = startdate[0]
        month = startdate[1]
        year = startdate[2]
        
        try:
            day = int(day)
            month = int(month)
            year = int(year)
        except ValueError:
            finaldate = "Input Error, date not in correct format!"
         
        yeardays = []
        k = numdayssince/(365.25)
        k = int(k+1)
        k += 1
        
        i = year
        while i < (year + k):
            n = i/4
            if n == int(n):
                yeardays.append(366)
            else:
                yeardays.append(365)
            i += 1
        #print(yeardays)
        numyears = 0
        x = 0
        while numdayssince >= 0:
            numdayssince -= yeardays[x]
            x += 1
        
        if numdayssince < 0:
            numdayssince += yeardays[x]
            x -= 1
           
        newyear = year + x
        #print(newyear)
        #print(numdayssince)  
        
        n = newyear/4
        if n == int(n):
            montharray = monthdaysleapyr
        else:
            montharray = monthdays
        
        daysleftinmonth = montharray[month-1] - day
        #print(daysleftinmonth)
        montharray[month-1] = daysleftinmonth
        
        m = month-1
        while numdayssince >= 0:
            numdayssince -= montharray[m]
            if m == 11:
                m = 0
            else:
                m += 1
       
        if numdayssince < 0:
            numdayssince += montharray[m]
            m -= 1
     
        newmonth = m + 1
        newdate = []
        newdate.append(numdayssince)
        newdate.append(newmonth)
        newdate.append(newyear)
        
        monthnames = ['January','February','March','April','May','June','July','August','September','October','November','December']
        
        string_numericmonth = str(newdate[0]) + "/" + str(newdate[1]) + "/" + str(newdate[2])
        a = newdate[1] - 1 
        string_Englishmonth = str(newdate[0]) + " " + str(monthnames[a]) + " " + str(newdate[2])
        finaldate = string_numericmonth + ' (' + string_Englishmonth + ').'
        return finaldate
        

    

#Function reverses the order of elements in an array
def array_reverse(lst):
    new_lst = lst[::-1]
    return new_lst

#Function calculates the overall average for all data by day and prints out the result
def alltimeaverage(array):
    while i < len(array):
        i += 1
        sub = array[:i]
        avg = sum(sub)/i
        string = 'Day ' + str(i) + ' average: ' + str(avg)
        print(string)
        
#Function calculates all the (ndays) moving averages and returns them all as an array along with the array showing the day numbers with a (ndays) moving average.
def multidaymovingaverage(array,ndays):
    i = ndays - 1
    days = []
    values = []
    while i < len(array):
        days.append(i)
        sub = array[i-(ndays-1):i]
        avg = sum(sub)/len(sub)
        values.append(avg)
        i += 1
    return values, days

#Function calculates the rate of change of value y from time value x as percentage of previous value and value change of previous value    
def rate_of_change(y, x):
    a = y[x-1]
    b = y[x]
    c = b - a
    pc = b/a 
    pc -= 1
    pc *= 100
    return c, pc

#The CSV file containing data sourced from the website    
#https://www.covidaustralia.com/wa on 6 March 2022
fcsv = "/storage/emulated/0/Download/covid_au_25jan20_to_6mar22.csv"

data = []
with open(fcsv) as file_obj:
    reader_obj = csv.reader(file_obj) 
    for row in reader_obj:
        data.append(row) 

num_lines = len(data)
i = 0
wa_data = []
dates = []
for row in data:
    if (i < num_lines - 4) and (i > 0):
         dates.append(row[0])
         wa_data.append(row[4])
    i += 1


new_dates = []

yr = 2022
i = 0
for d in dates:
    nd = str(d) + ' ' + str(yr)
    if d == 'Jan 1':
        yr -= 1
    new_dates.append(nd)   

dates = array_reverse(new_dates) 
wa_data = array_reverse(wa_data) 

for row in data:
    if (i >= num_lines - 4):
         d = str(row[0]) + ' ' + str(2022)
         dates.append(d) 
         wa_data.append(row[4])
    i += 1


x = len(wa_data)
wa_data[x-1] = "2,270"
for i in range(x):
    flt = wa_data[i].replace(',','')
    val = int(flt)
    wa_data[i] = val

#Appending new daily data since data was extracted.
wa_data.append(2365)
wa_data.append(2847)
wa_data.append(3594)
wa_data.append(4535)
wa_data.append(5005)
wa_data.append(4300)
wa_data.append(3602)
wa_data.append(4037)
wa_data.append(5377)
wa_data.append(6062)

a = wa_data

#5 day moving average
v5, d5 = multidaymovingaverage(a,5)
#3 day moving average
v3, d3 = multidaymovingaverage(a,3)
#7 day moving average
v7, d7 = multidaymovingaverage(a,7) 


x5 = len(v5) - 1 
x3 = len(v3) - 1 
x7 = len(v7) - 1 

#Getting index position of last value in array
x = len(a) - 1

#Finding the daily number change from yesterday (c) and the percentage change from yesterday(pc)
c, pc = rate_of_change(a, x)
#Find the daily number change from yesterday and percentage change for all moving averages
c3, pc3 = rate_of_change(v3, x3)
c5, pc5 = rate_of_change(v5, x5)
c7, pc7 = rate_of_change(v7, x7)

#Finding the last index value for the moving average arrays
n3 = len(v3)
n5 = len(v5)
n7 = len(v7)
print('RESULTS')
print('Day ' + str(len(a)))
print('Daily cases reported: ' + str(a[x]))
print('Change from yesterday: ' + str(c))
print('3 day moving average: ' + str(v3[n3-1]))
print('Change from yesterday: ' + str(c3))
print('5 day moving average: ' + str(v5[n5-1]))
print('Change from yesterday: ' + str(c5))
print('7 day moving average: ' + str(v7[n7-1]))
print('Change from yesterday: ' + str(c7))

print('Daily Record: ')
day_of_record = -1
record = max(wa_data)
for i in range(len(wa_data)):
    if wa_data[i] == record:
        day_of_record = i+1


print(str(record) + ' cases ' + str(day_of_record) + ' days after the first ever recorded Covid case.')

date_of_record = findthedate([25,1,2020], day_of_record)            
print("Day record set: " + str(date_of_record))

current_date = findthedate([25,1,2020], len(a))            
print("Date last updated: " + str(current_date))

#Date: 25-Jan-2020
#Julian Date: 20025

#Today's date is 15-Mar-2022 (UTC).
#Today's Julian Date is 22074 .






