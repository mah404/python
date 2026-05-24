# this is the comment

# print('Mah variyani')

# name='Mah variynai'
# age = 34
# print(name,age)

# full_name='this is allowed'
# print(full_name)

# width , height = 300 , 400

# print(width,height)
# yourName=input('what is your name?')
# print('hi ' + yourName)


# num1 = int(input('Write a number'))
# num2 = int(input('Write a number'))
# print(num1+num2)


# Data types
# string
# numbers
# Lists
# Dictionaries


# string and Numbers

# print("You are going to a Restaurant and you ordered food ")
# food = int(input("How much did you pay for the food? "))
# tipBefore = int(input("How much tip?"))
# tip = tipBefore / 100
# actualTip = food * tip

# finalPrice = actualTip + food
# print(f'Food Amount: ${food}')
# print(f'Tip Amount: ${tipBefore}')
# print("$" + str(finalPrice))

# #boolean
# weather = input("what is the weather like?")

# if weather == "rain ,snow , cloudy ,stormy":
#     print("take an umbrella")
# elif weather == "sunny and hot":
#     print("wear sunglasses")
# else:
#     print("enjoy the day")

# grade = int(input("what is your grade?"))

# if grade >= 90 or grade == 100:
#     print("A")
# elif grade >= 80 or grade == 89:
#     print("B")
# elif grade >= 70 and grade == 79:
#     print("C")
# elif 60 <= grade <= 69:
#     print("D")
# else:
#     print("F")

# myName = input("what is your name?")


# def say_my_name():
#     print("your name is  " + myName)


# say_my_name()


# def add_numbers(num1, num2=3):
#     """
#     So here we have the triple-quote comment that explains the default argument in Python.
#     If we give a default number and do not pass a parameter,
#     it uses the default value. And if you give a number,
#     it shows the parameter you passed.
#     """
#      #print(f"we have 2 numbers and they are {num1} and {num2}")
#     print(f"arguments and the default arguments {num1} and {num2}")

# add_numbers(num1=4, num2=67)


# def sum(a, b):
#     return a + b


# print(sum(3, 4))


# print("You are going to a Restaurant and you ordered food ")
# food = int(input("How much did you pay for the food? "))
# tipBefore = int(input("How much tip?"))
# tip = tipBefore / 100
# actualTip = food * tip

# finalPrice = actualTip + food
# print(f'Food Amount: ${food}')
# print(f'Tip Amount: ${tipBefore}')
# print("$" + str(finalPrice))


# def calculateFoodTotal(foodAmount, tipPercentage):
#     """
#     This function calculates the total amount of food including the tip.
#     def means we are defining a function and the name of the function is calculateFoodTotal
#     foodAmount and tipPercentage are the parameters of the function.
#     The function takes in the food amount and the tip percentage,
#     calculates the actual tip, and then returns the final price which is the sum of
#     the food amount and the actual tip.
#     """
#     tip = tipPercentage / 100
#     actualTip = foodAmount * tip
#     finalPrice = actualTip + foodAmount
#     return finalPrice
# """
# foodAmount is the amount of money you paid for the food and tipPercentage
# is the percentage of tip you want to give.
# """

# foodAmount = int(input("How much did you pay for the food? "))
# tipPercentage = int(input("How much tip?"))

# total = calculateFoodTotal(foodAmount, tipPercentage)
# print(f"Food Amount: ${foodAmount}")
# print(f"Tip Amount: ${tipPercentage}")
# print(f"Total Amount: ${total}")

# Exercise: Write a function that takes in a list of numbers and returns the average of those numbers.


# """
# Write a function bigger_guy that takes in
# two numbers and returns the bigger one.

# MAKE SURE to use RETURN and not PRINT in your function.
# """


# def bigger_guy(a, b):
#     if a > b:
#         print(a)
#     elif b > a:
#         print(b)
#     else:
#         print("both numbers are equal")


# bigger_guy(23, 3)


# sum = lambda x ,y : y *x
# print(sum(3, 4))

# greet = lambda greet, name: f"{greet} {name}"
# # print(greet("hi", "mah variyani"))
# """ 
# shift alt a to get the triple-quote

# so assert is used to check if the function is working properly or not.
# It checks if the output of the function is equal to the expected output. If it is not, it raises an error. If it is, it does nothing and the program continues to run.
# """

# assert greet("hi", "mah variyani") == "hi mah variyani"




##Lists

""" 
Lists are a collection of items that are ordered and changeable. They are defined by using square brackets [] and can contain any type of data, including other lists. Lists are mutable, which means you can change their content without changing their identity. You can add, remove, or modify items in a list after it has been created. Lists also support indexing and slicing, allowing you to access specific elements or subsets of the list.
"""

myList = [1, 2, 3, 4, 5]
print(myList[0])  # Accessing the first element of the list

#methods 
""" 
methods are functions that are associated with a particular object. In the case of lists, there are several built-in methods that allow you to manipulate and interact with the list. Some common list methods include:

list.append(x): Adds an item x to the end of the list.
print(myList) is function 
"""
print(myList[2])
print(myList[-1])
print(myList[2:5])

print(len(myList))

print('Hi This is Mah variyani'[3:10])

#ساعت 2 و 15 دقیقه هست که  ویدیو رو دادم 
#https://www.youtube.com/watch?v=B9nFMZIYQl0&t=2048s