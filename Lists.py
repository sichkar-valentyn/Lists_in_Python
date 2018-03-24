# File: Lists_in_Python.py
# Description: How to create and use lists in Python
# Environment: PyCharm and Anaconda environment
#
# MIT License
# Copyright (c) 2018 Valentyn N Sichkar
# github.com/sichkar-valentyn
#
# Reference to:
# [1] Valentyn N Sichkar. Lists in Python // GitHub platform [Electronic resource]. URL: https://github.com/sichkar-valentyn/Lists_in_Python (date of access: XX.XX.XXXX)

students = ['Ivan', 'Masha', 'Sasha']
for s in students:
    print('Hello, ' + s + '!')  # We use here + s + instead of comma in order to connect them without gaps

print(len(students))  # Showing the length of list - number of elements
print(students[-1])  # Showing the -1 element in the list
print(students[:2])  # Showing the elements from the beginning to the 2
print(students[::-1])  # Showing the elements of the list in reverse direction

teachers = ['Pavel', 'Alya']
print(students + teachers)  # Adding one list to another

print(students * 2)  # Doubling the list
print(teachers * 3)  # Trippling the list

students[2] = 'Alla'  # Re-assigning the 2nd element
print(students)

students.append('Olga')  # Adding to the end the new element with method append
print(students)

students += ['Katya']  # Adding to the end the new element with just +
print(students)

students += ['Anya', 'Asya']  # Adding two elements at the end
print(students)

students.insert(1, 'Masya')  # Inserting the element in the position 1
print(students)

students += '123'  # Without square brackets it will add 1, 2 and 3rd element as separate
print(students)

students.remove('Olga')  # Removing element if it is inside the list with method remove
print(students)

del students[4]  # Deleting the element in the position 4
print(students)

if 'Ivan' in students:  # Checking if the element is inside the list
    print('Ivan is here')

if 'Anna' not in students:  # Checking if the element is not in the list
    print('Anna is absent')

ind = students.index('Alla')  # Getting an index of the element
print(ind)

ordered_students = sorted(students)  # Sorting the list
print(ordered_students)

students.sort()  # Sorting the list with method sort
print(students)

print(min(students))  # Finding the min and max in the list
print(max(students))  # But the elements inside the list have to be comparable

students.reverse()  # Changing the positions in the list in reverse direction with method reverse
print(students)

r = reversed(students)  # Changing the positions of the elements in reverse direction
print(r)

r = students[::-1]  # Also changing the direction of the elements in the list
print(r)

a = [1, 'A', 2]  # Crating new list
b = a  # Assigning new list to another
print(a)
print(b)

a[0] = 48  # Pay attention that list b is not a real new list, it is just a reference to list a
print(a)
print(b)

b[2] = 5  # So if we change something in a or b list it will change it in both lists
print(a)
print(b)

a = [0] * 5  # Creating new list of 5 elements and all with 0 value
print(a)

a = [3 for i in range(5)]  # Another way to create list with elements of 3
print(a)

a = [i*i for i in range(5)]  # Creating list with elements that are expression of i * i
print(a)

a = [int(i) for i in input().split()]  # Creating list of integer numbers by inputting them in one string with gap
print(a)
