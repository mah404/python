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

print("You are going to a Restaurant and you ordered food ")
food = int(input("How much did you pay for the food? "))
tipBefore = int(input("How much tip?"))
tip = tipBefore / 100
actualTip = food * tip

finalPrice = actualTip + food
print(f'Food Amount: ${food}')
print(f'Tip Amount: ${tipBefore}')
print("$" + str(finalPrice))
