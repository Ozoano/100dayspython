'''
Naive date & times: Does not have enough info to determine things like time zone, or daylight savings time 
Aware datetimes: Does have enough info to determine things like time zone, or daylight savings time 
'''  
import datetime


#datetime.date --> This helps work with date, month and year


#To fetch todays date
tday = datetime.date(2022, 9, 14)
print(tday)
#OR
t_day = datetime.date.today()



# For weekday() --> Monday == 0 while Sunday == 6
print(t_day.weekday())
# For isoweekday() --> Monday == 1 while Sunday == 7.
print(t_day.isoweekday())



# timedelta() --> Represent the difference between two datetime or time
#This prints todays date
t_day = datetime.date.today()

# This prints 7 days from now 
tdelda = datetime.timedelta(days = 7)

Add_days = t_day + tdelda
print(Add_days)



# date2 == date1 + timedelta --> creating a new date by adding todays date and  in the future/past date 
# timedelta == date1 + date2 --> creating a timedelta by adding two diff dates
t_day = datetime.date.today()

#printing the number of days between m birthday and today
bday = datetime.date(2023, 1, 4)
time_delta = bday - t_day
print(time_delta)

#check the number of seconds until my birthday
print(time_delta.total_seconds())


'''
#datetime.time --> This helps work with hours, minutes, seconds and micro seconds
Time = datetime.time(2, 28, 55, 100000)
print(Time)
'''


#datetime.datetime --> combines the features of both datetime.time and datetime.date
# A program that prints the number of days until my next birthday

dateTime = datetime.datetime(2022, 1, 5, 2, 32,44, 10000)


#My next biethday
bday = datetime.date(2023, 1, 5)

diff = bday - dateTime.date()
print(diff)

tdelta = datetime.timedelta(days = 7)
days = dateTime + tdelta
print(days.date())





# BELOW ARE ALTERNATIVE CONSTRUCTORS THAT datetime() has

#today() --> returns todays date with time-zone of none. has no option to type in the time zone
dt_today = datetime.datetime.today()
print(dt_today)

#now() --> returns a datetime with an option to type in time-zone
dt_now = datetime.datetime.now()
print(dt_now)

#utcnow --> returns a datetime but the time-zone is still set to none
dt_utcnow = datetime.datetime.utcnow()
print(dt_utcnow)



#Using pytz to set up time zone
#pytx imported
import pytz


#Creating Aware datetime using utc...... i.e the current utc 

dateTime = datetime.datetime(2022, 9, 14, 4, 47, 44, tzinfo=pytz.UTC)
print(dateTime)

dt_utc = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_utc)




# print(dt_now)
'''
# Printing all time zones using a for loop
for tz in pytz.all_timezones:
    print(tz)
'''

#STEPS to print country time zone
                    #1 --> Create an aware TZ. i.e with the pytz
dt_now = datetime.datetime.now(tz=pytz.UTC)

#2 --> convert it to respective country tz
                    #Using pytz to get US/moutain time zone
Us_tz = dt_now.astimezone(pytz.timezone('US/Mountain'))
print('USA time zone: ', Us_tz)
                     #Using pytz to get lagos time zone#
lagos_tz = dt_now.astimezone(pytz.timezone('Africa/Lagos'))
print('Lagos time zone: ', lagos_tz)

                     #Using pytz to get canada time zone
canada_tz = dt_now.astimezone(pytz.timezone('Canada/Eastern'))
print('Canada time zone: ', canada_tz)



#converting naive Datetime  to aware date time using localize() to localize the naive dt
naive_tz = datetime.datetime.now()      
aware_tz = pytz.timezone('Africa/Lagos')
naive_convert = aware_tz.localize(naive_tz)
print(naive_convert)

#OR
convert_naive = naive_tz.astimezone(pytz.timezone('Africa/Lagos'))
print(convert_naive)




#strftime --> Converts Datetime to string
now = datetime.datetime.now()
s = now.strftime('%B %d %Y')
print(now)

#strptime --> Converts String to datetime
dt_str = 'september 22, 2022'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)


#Another example using strftime
lagos_tz = dt_now.astimezone(pytz.timezone('Africa/Lagos'))
print('Lagos time zone: ', lagos_tz.strftime('%B %d %Y'))

#Another example using strptime
sep = 'September 14, 2022'
string_to_dt = datetime.datetime.strptime(sep,  '%B %d, %Y')
print(string_to_dt)



