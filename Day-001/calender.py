import calendar

print('Enter year....')
y = input('Enter your desired year: ')

print('Enter month...')
m = input('Enter the month:  ')


yy = int(y)
mm = int(m)

print(calendar.month(yy, mm))



# A program for a twelve month calendar
import calendar

print('Enter year....')
y = input('Enter your desired year: ')

yy = int(y)

print(calendar.calendar(yy)
