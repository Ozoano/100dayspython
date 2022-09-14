#Program on different methods to access values from a dictionary and list


#String concatenation for dictionary
person = {'name': 'Uchenna', 'age': 25, 'Salary': 10000}
sentence = 'My name is ' + person['name'] + ' I am ' + str(person['age']) + ' years old.' ' I earn a monthly of ' + '$'+str(person['Salary'])
print(sentence)


# Using placeholders and passing dictionary to format()
placeholders = 'My name is {}, I am  {} years old. I earn a monthly of ${}'.format(person['name'], person['age'], person['Salary'])
print(placeholders)


#Come back to this section
'''
print()
persons = {'name': 'Uchenna', 'age': 25, 'Salary': 10000}
# Using placeholders
indexx = 'My name is {0}, I am  {1} years old. I earn a monthly of ${2}. Next year, I will be {1} years old'.format(persons['name'], persons['age'], persons['Salary'],  persons['age'+2])
print(indexx)
'''


#Alternatively, Passing dict keys drectly to the placeholders
print()
persons = {'name': 'Uchenna', 'age': 25, 'Salary': 10000}
# Using placeholders
#indexx = 'My name is {0[name]}, I am  {1[age]} years old. I earn a monthly of ${2[Salary]}'.format(persons, persons, persons)

#OR....................
#indexx = 'My name is {[name]}, I am  {[age]} years old. I earn a monthly of ${[Salary]}'.format(persons, persons, persons)
#OR....................
indexx = 'My name is {0[name]}, I am  {0[age]} years old. I earn a monthly of ${0[Salary]}'.format(persons)
print(indexx)





#Accessing values from a list thru a placeholder
lists = ['Uchenna',  25,  10000]
l_index = 'My name is {0[0]}, I am  {0[1]} years old. I earn a monthly of ${0[2]}'.format(lists)
print(l_index)



# Alternativly, accessing values from a list thru a placeholder
print()
#Accessing values from a list thru a placeholder
lists = ['Uchenna',  25,  10000]
l_index = 'My name is {0}, I am  {1} years old. I earn a monthly of ${2}'.format(lists[0], lists[1], lists[2])
print(l_index)




#Class --> accessing data from a class thru a placeholder
class person():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

#Creating an instance... Instantiation
details  = person('Uchenna', 25, 10000)

sentences = 'My name is {0.name}, I am  {0.age} years old. I earn a monthly of ${0.salary}'.format(details)
print(sentences)




# #Passing keys to a placeholder
key_words = 'My name is {name}, I am  {age} years old. I earn a monthly of ${salary}'.format(name = 'Uchenna', age = 25, salary = 10000)
print(key_words)

# key_word = 'My name is {name}, I am  {age} years old. I earn a monthly of ${salary}'.format(name = 'Uchenna', age = 25, salary = 10000)
# print(key_words)


#Unpacking a dictionary
person = {'name': 'Uchenna', 'age': 25, 'Salary': 10000}
key_w = 'My name is {name}, I am  {age} years old. I earn a monthly of ${Salary}'.format(**person) # Unpacking
print(key_w)

key_w = 'My salary is ${:,.2f}'.format(1000 ** 2)
print(key_w)




#a program for time using placeholder
import datetime
from re import S

now = datetime.datetime(2022, 9, 13, 13, 44, 50)

today = '{:%A %m, %Y, %H:%M:%S %p}'.format(now)
print(today)

print()
# t_day = 'Today Tuesday september 13, 2022 fell in the 255 days of the year'
t_day = 'Today being {0:%A %B %d, %Y} with time {0:%H:%M:%S %p} fell in the {0:%j} of the year'.format(now)
print(t_day)

