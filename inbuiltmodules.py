#math

import math

# print(dir(math))
# print(math.pow(6,7))#it will print it as power in floating..
# 
# 6**7
# print(math.pi)
# print(math.sqrt(25))
# print(math.exp(4))
# print(math.e)
# print(2.71**2)
# # #e=2.71
# print(math.log(10))#It will take e as the base for logrithms..
# print(math.log10(10))
# print(math.factorial(6))


# import random

# print(random.random())#In between 0 and 1 it will give a random values..
# print(random.randint(3,40))#Random integer value in between specified range including th last value..
# print(random.randrange(3,40))#Random integer value in between specified range excluding th last value..
# print(random.randrange(3,40,4))#difference between each value will be 4.
# 3,7,11,15,19,23,27,31,35,39
# a=[4,5,'python','z','abc',[1,2,3,4]]

# # print(random.choice(a))#Pick a random element form the list..
# # print(random.shuffle(a))#shuffle the positions of element inside the list..
# # print(a)

# print(random.sample(a,3))#It will pick 3 value from a list a create a new list..

# #OS module

import os

# # print(dir(os))

# print(os.getcwd())#It will return the current working directory..
# os.chdir('C:/Users/Digitallync/Desktop')#for changing current working directory..
# print(os.getcwd())
# os.mkdir('Folder123')#for creating a folder
# os.rmdir('Folder123')#Removing the folder..
# os.makedirs('Folder123/Folder23/Folder3')#Creating folders inside folders at a time.
# os.removedirs('Folder123/Folder23/Folder3')#Removing folder inside folders at a time..
print(os.listdir('.'))

