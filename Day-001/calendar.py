# Library import
import calendar

#print("Enter Year: ", end = ' ')
try:
    yy = int(input('Enter year: '))
    print("\nEnter Month Number (1-12): ", end="")
    try:
        mm = int(input())
        if mm>=1 and mm<=12:
            print("\n", calendar.month(yy, mm))
        else:
            print("\nInvalid Month Number!")
    except ValueError:
        print("\nInvalid Input!")
except ValueError:
    print("\nInvalid Input!")
