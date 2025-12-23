"""
In Python, data types are classifications that specify the kind of values a variable can hold 
and the operations that can be performed on them
"""

#1. int data type

money = 500

print(money)

print(money,type(money)) # it shows the type of data type and its says int means Integer → 500 <class 'int'>

#2. float

time = 12.23

print(time)

print(time,type(time))   # it shows the type of data type and its says int means float  → 12.23 <class 'float'>

#3. complex 

d = 2+5j

print(d,type(d))         # it shows the type of data type and its says int means complex  → (2+5j) <class 'complex'>

# str: Strings 
"""
Strings (sequence of characters, e.g., "Hello World", 'Python'). 
Strings are immutable, meaning they cannot be changed after creation.
""" 

name = 'svj'
brand = "lamborghini"
model = "lamborghini svj roadster"

print(name,type(name))    #svj <class 'str'>
print(brand,type(brand))  #lamborghini <class 'str'>
print(model,type(model))  #lamborghini svj roadster <class 'str'>

# bool: Represents truth values, which can be either True or False. They are vital for logical operations.

we_win = False
they_win = True

print(we_win)