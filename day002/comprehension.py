
#Looping thru list 

# my_list = []
# for n in num:
#     my_list.append(n)
# print(my_list)


#OR --> The above can be achieved with a comprehension
'''
NOTE : In a comprehensuon --> The appended value comes first, followed by the outer loop, then the inner loop
'''
#Comprehension
# my_list = [n for n in num]
# print(my_list)



# List multiplication  with a loop
# my_list = []
# for n in num:
#     my_list.append(n*n)
# print(my_list)

# List multiplication  with a loop and comprehension
# my_list = [n*n for n in num]
# print(my_list)


# I want 'n' for each 'n' in num if 'n' is even
# my_list = []

# for n in num:
#     if n % 2 == 0:
#         my_list.append(n)
# print(my_list)

# # Using Comprehension
# my_list = [n for n in num if n % 2 == 0 ]
# print(my_list)


# print('.............................................................')
# #A program for the user to enter a (letter, num) pair for each letter in the alphabet range and each value innnumber
# alphas = input('Enter Your alphabet within a - f: ')
# nums = int(input('Enter your number: '))


# my_list = []
# for alpha in alphas:
#     for num in range(nums):
#         my_list.append((alpha,num))
# print(my_list)

# print()


# # Using a list comprehension

# my_list = [(alpha,num) for alpha in alphas for num in range(nums)]
# print(my_list)


#Dictionary Comprehension
children_position = ['Fchild', 'Schild', 'Tchild', 'Frtchild', 'Fifchild', 'Lchild']
names = ['Ugo', 'Aham', 'Iyke', 'Chioma', 'Nneka', 'Uchenna']

#Zip() --> Helps create a list of tuples that matches the string in the first list with that of the second list
print(list(zip(children_position, names)))

# The zip object yields n-length tuples, where n is the number of iterables passed as positional arguments to zip()
n = list(zip('abcdefg', range(6), range(6)))
print(n)


# Program that creates a dict{'children_position': 'Names'} for each children position, name in zip(children_position, names)
'''
myList = {}
for child in children_position:
    for name in names:
        myList[child] = name
 print(myList)
 '''

 # OR using the zip() Function
 myList = {}
 for child, name in zip(children_position, names):
 myList[child] = name
 print(myList)

 #Print a space
 print()

 #Or --> Using a dictionary comprehension
 my_dict = {child:name for child, name in zip(children_position, names) if child != 'Fchild'  and child!= 'Lchild'}
print(my_dict)

# Set comprehension
num = [0, 0,  1,  1, 2,  3,  4,  5, 5,  6,  7,  8,  9, 9]
my_set = set()
for sets in num:
    my_set.add(sets)
print(my_set)

#OR -->  Using Comprehension
my_set = set(sets for sets in num)
print(my_set)
