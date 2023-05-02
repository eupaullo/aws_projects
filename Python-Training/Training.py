# import datetime
# # PRINT
# # ==========
# # print("Greeting to you all")
# # print("Hello Salami!")
# # print(6 + 7)
# # print("I hope all is well?")



# # COMMENT 
# # ========
# # a. Single  line comment
# # ============================
# # Define parameter      / This is an example if a single line comment
# X = 5
# Y = 10 


# # b. Multi line comment /documentation string / docstring
# # ===================================
# """
#     Stops an EC2 instance that has been idle for 5 minutes or more.

#     Parameters:
#     event (dict): AWS Lambda event data.
#     context (object): AWS Lambda context object.

#     Returns:
#     None

#     Raises:
#     None
# """

# # Finding the sum of X and Y 
# # Z = X + Y
# # print(Z)
# # Z = X - Y + Y


# # VARIABLE 
# # ==============

# # 1. Variable names must start with a letter or an underscore character (_)
# # x = 10
# # y = 16
# # fruit = "Orange"
# # color = "Red"
# # _car = "Honda"

# # 2. Variable names are case-sensitive

# # 3. You can assign a value to a variable using the assignment operator (=)
# # x = 9
# # fruit = "Orange"

# # 4. Variables can be reassigned to a new value
# # x = 9
# # x = 18
# # x = "Dog"

# # print(x)
# # 5. Python is dynamically typed meaning a variable can be initialized as sting and then assigned an integer
# # 6. Print the value with print()
# # 7. There are some reserved keywords that can not be used as variables.
# # Location = "Texas"
# # if = 
# # print = ""
# # Max

# # How to assign value to a variable
# # print(Location )
# # a. Single assignment e.g x = 5
# # b. Many Values to Multiple Variables e.g fruit, animal, location = "Orange", "Dog", "Texas"
# # c. One Value to Multiple Variables e.g boy=man=father= "male"
# # d. Unpack a Collection male = 


# # Data Type 
# # ====================

# """
# Strings: 
#     A string is a sequence of characters, and it is also immutable. 
#     Strings can be manipulated using a variety of built-in functions and operators.

# Numbers: 
#     There are several numeric data types in Python, including:
#         - integers:  Integers are whole numbers
#         - floats: floats are numbers with a decimal point
#         - complex numbers: complex numbers are numbers with a real and imaginary part.
    
# Lists: A list is an ordered collection of elements, which can be of different data types. 
#     Lists are mutable, which means that they can be modified after creation.

# A tuple 
#     A Tuple is similar to a list, but it is immutable, meaning that once it is created, it cannot be changed. 
#     Tuples are often used to group related data together.
    
# Sets: 
#     A set is an unordered collection of unique elements. 
#     Sets are useful when you want to remove duplicates from a collection of data.

# Dictionaries: 
#     A dictionary is a collection of key-value pairs. 
#     Each key in the dictionary maps to a value, which can be of any data type.

# Booleans: 
#     A boolean is a data type that can have one of two values: True or False. 
#     Booleans are often used in conditional statements to control program flow.

# None:
#     It is often used to indicate that a variable or function argument has not been assigned a value, or that a function does not return a value.
# """
# # 1. String:  This is a text in python or any other programming language e.g "Hello" or "Today is a beautiful day"
# # 2. Number
# #   a. Integer: This is a number such as 2, 5l, 9, 5
# #   b. Float:  This is a number with a decimal point such as 12.4, 5.0 or 11.29
# # 3. Bool/ Boolean: This is a two value keyword such as Yes or No / True or False
#     # Name = "Kola"
#     # age = 88
#     # isMarried = True or False 
#     # Bank-Balance = 55,000.99
#     # Data Structure or sequence type =
# # a. List 
# # Fruits = ["Orange", "Apple", "Banana"]
# # Fruits = ["Eba", "Fufu", "Banana"]

# # print(type(Fruits))

# # # b. 
# # food = ("Orange", "Apple", "Banana")
# # print(type(food))
# # # # b. 
# # food = ("Eba", "Fufu", "Banana")
# # print(food)

# # person = {
# #     "Name" : "Kenneth",
# #     "Age": 99,
# #     "IsMarried": True
# # }

# # print(person)
# # list
# # L_numbers =  [44,22,44,66]
# # L_numbers[0] = 77
# # print(L_numbers)
# # [77,22,44,66]
# # tuple
# # T_numbers =  (44,22,44,66)
# # T_numbers[0] = 77
# # print(T_numbers)



# #             #  = (77,22,44,66)
# # ages= {33,44,22,66,33,33,222}

# # print(ages)

# # Data Types
# # ============

# # String ===> Str e.g "Hello World!"
# # Numbers ===> 
# #     a. integer = ex. 9
# #     b. float = 9.0

# # boolean ===< bool e.x True or False

# # Data Structure
# #     a. List  ex. numbers = [2,4,6.7]
#     #   b. Set e.x {44,22,11,33,11,33}
#         # c. Tuple ex. (2,4,6.7)
#         # d. dictionary/dict e.g {
#         # "Name":"Oochay",
#         #                "Age": 99 
#                             # }



# # WORKING WITH Syntax
# # ==========================
# """
# lower() and upper(): 
#     These methods return a new string with all the characters in lowercase or uppercase, respectively.

# capitalize(): 
#     This method capitalizes the first character of the string.

# strip(), rstrip(), and lstrip(): 
#     These methods remove any whitespace characters (spaces, tabs, etc.) from the beginning and/or end of the string.

# split(): 
#     This method splits a string into a list of substrings, based on a specified delimiter (e.g., space, comma, etc.).
#     Sample "1234567890,0987654321,2468013579,9876543210,0123456789,1357908642,3141592653,2718281828,9876543210,0123456789,2468013579,1357908642,3141592653,2718281828,9876543210,0123456789,1234567890,0987654321,1357908642,2468013579"
# join(): 
#     This method joins a list of strings into a single string, using a specified delimiter.

# replace(): 
#     This method replaces all occurrences of a specified substring with another substring. This will return another string

# find(): 
#     This method returns the index of the first occurrence of a specified substring in the string, or -1 if it is not found.

# startswith() and endswith(): 
#     These methods return a boolean value indicating whether the string starts or ends with a specified substring.

# len():  
#     This function returns the length of the string.

# Slice():
#     A string can be sliced to extract a portion of the string. Slice method uses square bracket to wrap the start index and the end index. End index is not included in the return value.

# """



# # lower() and upper(): 
# #     These methods return a new string with all the characters in lowercase or uppercase, respectively.

# # greetings = "Hello Everyone!"
# # greetings = greetings.lower()      
# # greetings = greetings.upper()
# # print(greetings)

# # capitalize(): 
# #     This method capitalizes the first character of the string.

# # greetings = greetings.capitalize()


# # strip(), rstrip(), and lstrip(): 
# #     These methods remove any whitespace characters (spaces, tabs, etc.) from the beginning and/or end of the string.
# # training = " Hello Class "
# # greetings = training.lstrip()
# # print(len(training)) # /13
# # print(len(greetings)) # /11

# # len():  " 912 603 38832 "
# #     This function returns the length of the string.
# # greetings = len(greetings)

# # print(greetings)


# # split(): 
# #     This method splits a string into a list of substrings, based on a specified delimiter (e.g., space, comma, etc.).
# # account_numbers = "1234567890,0987654321,2468013579,9876543210,0123456789,1357908642,3141592653,2718281828,9876543210,0123456789,2468013579,1357908642,3141592653,2718281828,9876543210,0123456789,1234567890,0987654321,1357908642,2468013579"
# # account_list  =   account_numbers.split(",")


# # join(): 
# #     This method joins a list of strings into a single string, using a specified delimiter.
# # accountWithSlash = "&".join(account_list )
# # print(accountWithSlash)
# # print(type(accountWithSlash))



# # replace(): 
# #     This method replaces all occurrences of a specified substring with another substring. This will return another string

# # greetings = "Hello Everyboard, how are you today Everyboard"
# # greetings = greetings.replace('Everyboard', "everyone")
# # print(greetings)


# # find(): 
# #     This method returns the index of the first occurrence of a specified substring in the string, or -1 if it is not found.

# # greetings = "Hello World!, Hello everyone"
# # greetings = greetings.find("zebra")
# # print(greetings)

# # startswith() and endswith(): 
# #     These methods return a boolean value indicating whether the string starts or ends with a specified substring.

# # greetings = "Hello World!, Hello everyone"  #boolean 
# # greetings = greetings.startswith("Zebra")  
# # if greetings == True:
# #     print("Yes! we did it")
# # else: print("oh On, we missed it.")



# # greetings = "Hello World!, Hello everyone"  #boolean 
# # # slice_words = greetings["Start Index": "End Index"]
# # slice_words = greetings[3:]
# # print(slice_words)



# # ======================================================= 


# # WORKING WITH SLICE - done
# # ================================
#     # report = "Your AWS Account number is 32495862548 Your account is Active"
#     # account = report.split("")

#     # print(account[5])

#     # report = "YourAWSAccountnumberis32495862548YouraccountisActive"
#     # # slice = slice["start Index":"end Index"]
#     # account_sliced=report[22:33]
#     # print(account_sliced)
# # WORKING WITH CONCATENATION
# # ================================
# # F_name = "Yemi"
# # L_name = "Ayo"
# # age = 10
# # isMarried = True
# # Address = ""
# # full_name = F_name +" " +L_name # YemiAyo
# # print(full_name)

# # message = full_name + " is my full name"

# # message = "{} {}  is my full name.I am {} years old. Is {} that I am married".format(F_name, L_name, age, isMarried)
# # print("This is Format", message)
# # message = f"{F_name} {L_name}  is my full name.I am {age} years old. Is {isMarried} that I am married"

# # print("This is f: ", message)


# # WORKING WITH USER-INPUT
# # name = input("What is your name ? ")
# # greetings = f'Good Evening {name}'
# # print(greetings)
# # WORKING WITH FORMAT
# # WORKING WITH CAST
# # WORKING WITH OPERATOR
# # ============================================

# # F_name = input("What is your first name? ")
# # L_name = input("What is your last name? ")
# # age = input("how old are you? ")
# # message = "My first name is " + F_name +" and my last name is "+ L_name + ". I am "+ age + " years old"
# # print(message)
# # message = f'My first name is {F_name} and my last name is  {L_name}. I am {age} years old'
# # print(message)


# """
# PYTHON OPERATORS
# =====================
# 1. Arithmetic Operators
# 2. Assignment Operators
# 3. Comparison Operators
# 4. Logical Operators


# age = input("What is your age?") 

# type(age)  # str
# type(int(age))  == int

# 1. Arithmetic Operators
# =========================
# In Python, operators are special symbols or keywords 
# that perform arithmetic or logical operations on one or more operands (values, variables, or expressions).
# There are several types of operators in Python:


# Arithmetic operators: 
# =====================
# These operators are used to perform arithmetic operations like addition, subtraction, multiplication, division, modulus, exponentiation, and floor division. The arithmetic operators in Python are: + (addition), - (subtraction), * (multiplication), / (division), % (modulus), ** (exponentiation), and // (floor division).

# Addition (+): 
#     adds two operands

# """
# x= 13
# y =3
# sum = x + y
# print(sum)


# """

# Subtraction (-): 
#     subtracts one operand from another
    
# """
# Subtraction = x -y 
# print(Subtraction)

# """
# Multiplication (*): 
#     multiplies two operands

# Division (/): 
#     divides one operand by another and returns a floating-point number
# """
# Division = x / y 
# print(int(Division))
# """
# Modulus (%): 
#     returns the remainder of the division of one operand by another
# """
# Modulus = x % y 
# print(int(Modulus))
# """
# Floor division (//): 
#     performs integer division and rounds the result down to the nearest integer
# """
# Floor_division = x // y 
# print(Floor_division)

# """
# Exponentiation (**): 
#     raises one operand to the power of another

# """
# x =10
# y = 3
# Exponentiation = x**y 
# print(Exponentiation)

# """

# Comparison operators: 
# These operators are used to compare two values and return a Boolean value (True or False) based on whether the comparison is true or false. The comparison operators in Python are: == (equal to), != (not equal to), > (greater than), < (less than), >= (greater than or equal to), and <= (less than or equal to).

# Logical operators: These operators are used to perform logical operations like AND, OR, and NOT. The logical operators in Python are: and (AND), or (OR), and not (NOT).

# """

# # Assignment Operators
# # x = 7
# # ec2_client = boto3.client()


# # 3. Comparison Operators
# x = 10
# y = 3
# # equality sign    ==
# print(x == y)  # False
# # not equal   !=
# print(x != y)  # True

# # Greater Than      >
# print(x > y)  # True

# # Less Than      <
# print(x < y)  # False


# # Greater Than or Equal to      >=
# print(x >= y)  # True

# # less Than or Equal to      <=
# print(x <= y)  # False


# 4. Logical Operators

# # and    

# x = 20
# y = 3
# z =10

# if x > y and z < x:      
#     print("Positive")
# else:
#     print("Negative")

# or  

# if x < y or z > x:      
#     print("Positive")
# else:
#     print("Negative")

# if x < y or z > x:      
#     print("Positive")
# else:
#     print("Negative")



"""
WORKING WITH LIST

A list is a data structure that is used to store a collection of items, such as
    - numbers
    - strings
    - List
    - Objects
    
    List items are indexed, the first item has index [0], the second item has index [1] etc.
  
Example of a list
==================
a. Empty List e.g my_list = []
b. List with value e.g my_list = [1, 2, 3, 'a', 'b', 'c', 'a', 'b', ['apple', 'Orange'], False, {'name':'Betty', 'age': 11}]


Access List Items
====================
    List items are indexed and you can access them by referring to the index number. You can access a list using positive index value, negative index value or a range of indexes

    Example of Positive Index value
        first_Value = my_List[0]
        second_value = my_list[1]

    Example of Negative Index value
        first_Value = my_List[-1]
        second_value = my_list[-2]

    Example of Negative Index value
        firstFourValue = my_List[start:end]
        firstFourValue = my_List[0:3]

Modifying a List
================
Changing the value of a list
Add Item to a list using:
    - Append
    - insect
Remove item from a list using:
    - Remove
    - pop
    - del

Loop through a list
===================
    Looping the a list mean iterate over each item in the list using:
        - for loop
        - while loop
        - List Comprehensive: This is use for a short python code like for 2 lines of code such as:

        Instead of 
        for item in items:
            print(item)
        
        you can do:
        [print(item) for item in item]

Method of a List
    a. len such as len(my_list)
    b. sort() - This is ascending my default
    c. sort(reverse = True) to sort in descending order
    Note: Sort is case sensitive and this result in all item with upper case sort first
    d. copy
    e. join
    e. count - Return the number of times the value "cherry" appears in the fruits list such as my_list.count('a')




"""
# my_list = []
# my_list = [1, 2, 3]
# my_list = ['a', 'b', 'c', 'a', 'b',]
# my_list = [['apple', 'Orange'],[3.5, 5]]
# my_list = [{'name':'Betty', 'age': 11}]
# my_list = [False, True]
my_list = [1, 2, 3, 'a', 'b', 'c', 'a', 'b', ['apple', 'Orange'], False, {'name':'Betty', 'age': 11}]
        #  0  1  2   3    4    5    6    7          8               9                   10                                      
    #    -11 -10 -9 -8   -7   -6   -5   -4         -3              -2                   -1


# Item = my_list[0]
# Item = my_list[2]
# Item = my_list[-3]
# Item = my_list[8]
# Item = my_list[9]
# Item = my_list[3:]
# Item = my_list[3:]
# Item = my_list.append(90)
# my_list.insert(8, "dog")
# my_list[1] = 20
# my_list[-3] = ["banana", "grape"]
# my_list.remove('a')
# # del my_list[]
# print(Item)
# print(my_list)
# new_list = []
# print(f'This is old empty  {new_list}')
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# for fruit in fruits:
#     fruit = fruit.upper()  # APPLE
#     new_list.append(fruit)

# print(f'This is new  {new_list}')


# my_list = [1, 2, 3, 'a', 'b', 'c', 'a', 'b', ['apple', 'Orange'], False, {'name':'Betty', 'age': 11}, "cat"]

# my_list = [ 'a', 'b', 'c', 'a', 'b']

#     # a. len such as len(my_list)
# item = len(my_list)
#     # b. sort() - This is ascending my default
# item = my_list.sort()

#     # c. sort(reverse = True) to sort in descending order
# item = my_list.sort(reverse=True)

#     # Note: Sort is case sensitive and this result in all item with upper case sort first
#     # d. copy
# my_list = [ 'a', 'b', 'c', 'a', 'b']
# newLine = my_list
# anotherCopyfile= my_list.copy()
# print(newLine)  # [ 'a', 'b', 'c', 'a', 'b']
# print(anotherCopyfile) # [ 'a', 'b', 'c', 'a', 'b']
# my_list.append('cat')

# print(newLine)  # [ 'a', 'b', 'c', 'a', 'b']
# print(anotherCopyfile) # [ 'a', 'b', 'c', 'a', 'b']
# print(my_list)
#     # e. join
# my_list = ['a', 'b']
# your_list = [ 1,2,3]
# our_list = my_list + your_list
# print(our_list)

#     # e. count - Return the number of times the value "cherry" appears in the fruits list such as my_list.count('a')
# my_list = [ 'a', 'b', 'c', 'a', 'b']
# print(len(my_list))   # 5
# print(my_list.count('a'))  # 2
# # print(my_list)
    


# """
# WORKING WITH DICTIONARY ITEMS
# =============================
# Dictionaries are used to store data values in key:value pairs.
# 1. Access dictionary Item
#     - Using bracket
#     - Using .get() # return none if item is not found or does not exist
# 2. Change Item in a dictionary
#     - Using bracket
#     - .update({key:value}) - This take a key and value
# 3. Add Item to a dictionary
#     -Using Bracket
#     - using update
# 4. Removing Item from a Dictionary
#     - Using pop() - The pop() method removes the item with the specified key name
#     - Using popItem()  - The popitem() method removes the last inserted item
# 5. loop Dictionary
#     - For Loop
#     - While Loop
# 6. Copy Dictionary
# 7. Nested Dictionary
# 8. Dictionary Methods

# """
# properties = [{"car1":"Nissan", "car2":"Tesla", "car3":"Bentley"}, "House", 200,000, ["Bitcoin", "stocks", "golds"] ]
# car = {
# "brand": "Ford",
# "model": "explorer",
# "year": 2023,
# "Amount": 54999.99,
# "color":"Red",
# "isAmericanMade": True,
# "accessories": 
# [
#     "A/c",
#     "Radios", 
#     "Bluetooth", 
#     "Open-roof", 
#     {
#         "camera1":"rear camera", 
#         "camera2":"front camera", 
#         "camera3": {
#             "others": {"side1":"left-camera", "side2":["right_camera1","right_camera2"]}
#             }}
# ],
# "features":{"max_speed":"240mph", "after_market": "cameras"}
# }
# print(car)
# print("===================================================")
# car['color'] = "Green"     #red
# print(car)
# print("===================================================")
# car.update({"color": "Yellow"}) 
# print(car)
# print("===================================================")
# car.update({"Color": "Orange"}) 
# print(car)

# car['horn'] = "PinPin"     #red
# print(car)
# print("===================================================")
# car.update({"strobe": "Led"}) 
# print(car)


# print("===================================================")

# car.pop("color") 
# car.pop("Color") 
# car.popitem() 
# car.popitem() 
# print(car)

# for item in car:
#     print(item)

# car.update({"Color": "Yellow"}) 
# my_brand = car['brand']
# print(my_brand)

# model = car['model']
# print(model)

# year = car.get('year')
# print(year)

# accessories  = car["accessories"]
# item4_accessories = accessories[4]
# camera3 = item4_accessories.get('camera3')['others']['side2'][0]
# print(camera3)


# car.pop("brand")
# print(car)
# print(item)
# for item in car:
#     items = car.keys()
#     print(item.upper())
    
"""
WORKING WITH PYTHON CONDITIONS AND IF STATEMENTS

- if 
- if else
- if elif else
- break
- continue
- return
"""


current_time = "tomorrow"

if current_time =="Morning":
    print(f'good Morning')
elif current_time == "Afternoon": 
    print(f'good Afternoon')
elif current_time == "down": 
    print(f'good down')
else:
    print(f'good Evening')
    



function 


