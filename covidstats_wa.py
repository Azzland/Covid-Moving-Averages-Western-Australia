#-*-coding:utf8;-*-
#qpy:console
import csv

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








