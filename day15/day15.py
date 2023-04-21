

#print 'hello world'
#syntax error
print('hello world')


#print(age)
#name error
age = 19
print(age)

nums = [1,2,3,4,5]
#print(nums[5])
#index error
print(nums[4])


#import maths
#module not found error
import math

#math.PI
#attribute error
print(math.pi)

my_dict = {"an awesome language" : "python", "a very cool language" : "go"}
#print(my_dict["favorite_language"])
#key error
print(my_dict["an awesome language"])

#result = 4 + "3"
#type error
result = 4 + int("3")
print(result)

#from math import power
#import error
from math import pow

#int("12a")
#value error
print(int("12"))

result = 1/0
#division by zero error / zero division error
