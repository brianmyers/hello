import logging
import sys # input arguments
import argparse # input arguments
import os # working with files
from person import Person

logging.basicConfig(level=logging.DEBUG)

### 1. This is a comment (you can comment each line or a block/many lines of text)
### 1. print statement / logging
# print("Hello, World!")
""" logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message') """

### 1. Debugging errors (using print statement, logging, breakpoint)

# . Variable declarations
""" x = 2
y = .24
z = x + y
logging.debug("Z is equal to " + str(z))

r = "Rodney"
x = "Xavier"
i = "Isaiah"
m = r + ", " + x + ", " + i
print (m) """

# String methods
# https://www.w3schools.com/python/python_ref_string.asp
# txt = "hello, and welcome to my world."
# x = txt.upper()
# print (x)

### 2. Get input from user via command line arguments (Similar Java's Scanner class)
# sys.argv ... get a list of space separated inputs from the command line
# total arguments
""" n = len(sys.argv)
print("Total arguments passed:", n)
print("\nName of Python script:", sys.argv[0])
print("\nArguments passed:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")

# Space on the command line 
print("\n\n") """

# argsparse ... get a list of inputs from user using letter indicators for reference
""" parser = argparse.ArgumentParser()
# Adding optional argument
parser.add_argument("-o", "--Output", help = "Show Output")
parser.add_argument("-r", "--Report", help = "Show Report")
# Read arguments from command line
args = parser.parse_args()
if args.Output:
    print("Displaying Output as: % s" % args.Output)
if args.Output:
    print("Displaying Report as: % s" % args.Report) """

### 3. function/method definition, call reference, return value
""" def arg_type_test(*args):
    z = 0
    for i in args:
        print(i, end = " ")
        z += i
    return z
my_return_value = arg_type_test(1, 2, 5, 20)
print("\nMy return value: ", str(my_return_value)) """

""" def kwargs_iterate(**kwargs):
    for i, k in kwargs.items():
        print(i, '=', k)
print("\n")
kwargs_iterate(hello='world', roses="blue") """


### 4. Loops and Conditionals (while, if/else if/else, for, switch)
# while loop: execute a set of statements as long as a condition is true. With the 'break' statement 
# we can stop the loop even if the while condition is true. With the continue statement we can 
# stop the current iteration, and continue with the next
""" i = 1
while i < 7:
  print("I = " + str(i))
  if i == 3:
    print("continue with the while loop without printing what was incremented. but first increment i so there's no infinite loop.")
    i += 1
    continue      

  if i == 5:
    print("Breaking out of the while loop")
    break
  
  i += 1
  print("Incremented i to " + str(i)) """

# if/else if/else statement: 'if' executes if a condition is true. 'else if' is executed if 
# the prior 'if' statement wasn't true. 'else' executes if none of the 'if' statements are true.
""" Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
Equal to a == b
Not Equal to: a != b """
""" time = 22
if time < 10:
  print("Good morning.")
elif (time < 18):
  print("Good day.")
else:
  print("Good evening.") """

# for loop: execute a set of statements, once for each item in a list, tuple, set etc
# 'simple' for loop
""" fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) """
  
# 'nested' for loop
""" adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y) """
    

# switch or key/value
""" def numbers_to_strings(argument):
    switcher = {
        0: "zero",
        1: "one",
        2: "two",
    }
    # get() method of dictionary data type returns
    # value of passed argument if it is present
    # in dictionary otherwise second argument will
    # be assigned as default value of passed argument
    return switcher.get(argument, "nothing")

my_argument = 2
return_val = numbers_to_strings(my_argument)
logging.debug(return_val) """


### 5. Arrays
""" cars = ["Ford", "Volvo", "BMW", "Mazda", "Toyota"]
car = cars[0] #get the value at position 0
print("Car: " + car)
cars[0] = "Toyota" #set a value in the array at position 0
cars.append("Honda") #append and new element to the array
l = len(cars) #count the number of elements in the array
print("Array length: ", str(l))
for c in cars:
  print(c) #print each value in the array
  
cars.remove("Volvo") #remove a specific element from the array
l = len(cars)
logging.debug("Array length after remove Volvo: " + str(l))
cars.pop(1) #remove an element from the array at a position
l = len(cars)
logging.debug("Array length after pop: " + str(l)) """

### 6. Error handling
""" The try block lets you test a block of code for errors.
The except block lets you handle the error.
The else block lets you execute code when there is no error.
The finally block lets you execute code, regardless of the result of the try- and except blocks. """
""" if os.path.exists("demofile.txt"):
  logging.debug("File exists.")
  # os.remove("demofile.txt")
else:
  logging.debug("The file does not exist")
  
try:
  f = open("demofile.txt", "w") # a for append to file rather than overwrite the text
  try:
    f.write("Lorum Ipsum 001")
  except:
    logging.debug("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  logging.error("Something went wrong when opening the file") """

### 7. Classes
j = Person("John", 36)
rm = Person("Rodney", 43)
im = Person("Isaiah", 17)
xm = Person("Xaver", 14)

print("Name: " + j.name)
print("Age: " + str(j.age))
j.ssn = "111-22-1111"
print("My object: " + str(j))
print("My secret: " + j.getMySecretPersonInfo())

print("\n\nMy Rod object: " + str(rm))
print("\n\nMy Isaiah object: " + str(im))
print("\n\nMy Xavier object: " + str(xm))
