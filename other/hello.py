#!/usr/bin/env python3.7

#my_name = "Memo"
#print("Hello, world" + my_name)

# while
from turtle import color
import sys

count = 1
while count <= 4:
    print(f"looping : {count}")
    count += 1

#for
colors = ['blue', 'green']
for color in colors:
    print(color)

ages = {'kevin':59, 'bob':40,'kayla' : 21}
for key in ages:
    print(f"{key} is {ages[key]}")


for letter in "ages":
    print(letter)


list_of_points = [(1,2),(2,3),(3,4)]
for x, y in list_of_points:
        print(f"x:{x}, y:{y}")

a,b,c = (1,2,3)

for name, age in ages.items():
     print(f"Person named: {name}")
     print(f"Age of {age}")


#dict items([('kevon', 59)])

def hello_world():
     print("Hello, world")

def print_name(name):
     print(f"Name is {name}")

print_name(name="some name")
print_name("some name")

def can_drive(age,driving_age=16):
     return age >= driving_age

can_drive(15)
can_drive(15, 14)

# exception
file_name = "recipes.txt"
try:
    my_file = open(file_name, 'x')
    my_file.write('Meatballs\n')
    my_file.close()
except FileExistsError as err:
    print(f"The {file_name} file already exists")
    #sys.exit(1)
except:
    print("Unable to write to the file")
    #sys.exit(1)
else:
    print(f"Wrote {file_name}")
finally:
     print("Execution completed")

