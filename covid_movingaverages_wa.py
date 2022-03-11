#!/usr/bin/env python
# coding: utf-8

# In[2]:


#-*-coding:utf8;-*-
#qpy:console
import csv
import matplotlib.pyplot as plt

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
fcsv = "C:/Users/Azzla/Documents/covid_au_25jan20_to_6mar22.csv"

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


# In[21]:
days = []
i = 0
while i < len(a):
    days.append(i)
    i += 1
plt.plot(days, a)
plt.xlabel("Days since first recorded Covid case")
plt.ylabel("Daily Covid Cases")
plt.title("Daily Covid cases in W.A. since 25/01/20")
plt.show()

folder = 'C:/Users/Azzla/Documents/'
#Plot 3 day average over all time (since 25 January 2020)
plt.plot(d3, v3)
plt.xlabel("Days since first recorded Covid case")
plt.ylabel("Moving Average")
plt.title("3 day moving average of cases in W.A. since 25/01/20")
plt.show()
#plt.savefig(folder + "3dy_ma_alltime.jpg")

#Plot 5 day average over all time (since 25 January 2020)
plt.plot(d5, v5)
plt.xlabel("Days since first recorded Covid case")
plt.ylabel("Moving Average")
plt.title("5 day moving average of cases in W.A. since 25/01/20")
plt.show()
#plt.savefig(folder + "5dy_ma_alltime.jpg")

#Plot 7 day average over all time (since 25 January 2020)
plt.plot(d7, v7)
plt.xlabel("Days since first recorded Covid case")
plt.ylabel("Moving Average")
plt.title("7 day moving average of cases in W.A. since 25/01/20")
plt.show()
#plt.savefig(folder + "7dy_ma_alltime.jpg")


# In[22]:


folder = 'C:/Users/Azzla/Documents/'
#Number of days from 1/01 to 10/03 is 69
n = 69
#Find the day number at 31 December 2021
daynumberat31dec21 = d3[-n]
#Plot 3 day average over all time (since 1 January 2022)
days3dy = d3[-n:]
for i in range(len(days3dy)):
    days3dy[i] = days3dy[i] - daynumberat31dec21
    
cases3dy = v3[-n:]
plt.plot(days3dy, cases3dy)
plt.xlabel("Days since 1 Jan 2022")
plt.ylabel("Moving Average")
plt.title("3 day moving average of cases in W.A. since 01/01/22")
plt.show()
#plt.savefig(folder + "3dy_ma_2022.jpg")

#Plot 5 day average over all time (since 1 January 2022)
days5dy = d5[-n:]
for i in range(len(days5dy)):
    days5dy[i] = days5dy[i] - daynumberat31dec21
    
cases5dy = v5[-n:]
plt.plot(days5dy, cases5dy)
plt.xlabel("Days since 1 Jan 2022")
plt.ylabel("Moving Average")
plt.title("5 day moving average of cases in W.A. since 01/01/22")
plt.show()
#plt.savefig(folder + "5dy_ma_2022.jpg")

#Plot 7 day average over all time (since 1 January 2022)
days7dy = d7[-n:]
for i in range(len(days7dy)):
    days7dy[i] = days7dy[i] - daynumberat31dec21
    
cases7dy = v7[-n:]
plt.plot(days7dy, cases7dy)
plt.xlabel("Days since 1 Jan 2022")
plt.ylabel("Moving Average")
plt.title("7 day moving average of cases in W.A. since 01/01/22")
plt.show()
#plt.savefig(folder + "7dy_ma_2022.jpg")


# In[24]:


folder = 'C:/Users/Azzla/Documents/'
#Number of days from 1/03 to 10/03 is 9
n = 9
#Find the day number at 2 March 2022
daynumberat3mar22 = d3[-n]
#Plot 3 day average over all time (since 3 March 2022)
days3dy = d3[-n:]
for i in range(len(days3dy)):
    days3dy[i] = days3dy[i] - daynumberat3mar22
    
cases3dy = v3[-n:]
plt.plot(days3dy, cases3dy)
plt.xlabel("Days since border opening day")
plt.ylabel("Moving Average")
plt.title("3 day moving average of cases in W.A. since 03/03/22")
plt.show()

#Plot 5 day average over all time (since 3 March 2022)
days5dy = d5[-n:]
for i in range(len(days5dy)):
    days5dy[i] = days5dy[i] - daynumberat3mar22
    
cases5dy = v5[-n:]
plt.plot(days5dy, cases5dy)
plt.xlabel("Days since border opening day")
plt.ylabel("Moving Average")
plt.title("5 day moving average of cases in W.A. since 03/03/22")
plt.show()

#Plot 7 day average over all time (since 3 March 2022)
days7dy = d7[-n:]
for i in range(len(days7dy)):
    days7dy[i] = days7dy[i] - daynumberat3mar22
    
cases7dy = v7[-n:]
plt.plot(days7dy, cases7dy)
plt.xlabel("Days since border opening day")
plt.ylabel("Moving Average")
plt.title("7 day moving average of cases in W.A. since 03/03/22")
plt.show()


# In[ ]:




