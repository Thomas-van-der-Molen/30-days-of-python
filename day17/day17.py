
#packing and unpacking lists and dicts

def sum_of_five(a, b, c, d, e):
    return a+b+c+d+e

my_list = [1,2,3,4,5]
try:
    print(sum_of_five(*my_list))
except TypeError:
    print("that's not how you use that function")

nums = range(10,21)
print(list(nums))

my_range = [10,21]
nums = range(*my_range)
print(list(nums))

languages = ["Python", "Go", "Java", "C"]
py, go, *rest = languages
print(py, go, rest)

numbers = [1,2,3,4,5,6,7,8,9]
first, *middle, last = numbers
print(first, middle, last)

my_dict = {
    "name" : "Tom",
    "age" : 19,
    "favorite_languages" : ["python", "go"],
    "dream_company" : "Google"
}

def unpacked_info(name, age, favorite_languages, dream_company):
    return f'{name} is {age} years old. They like {favorite_languages} and want to work for {dream_company}'

print(unpacked_info(**my_dict))

def sum_of_nums(*args):
    ret = 0
    for i in args:
        ret += i
    return ret

print(sum_of_nums(1,234,234234,456456,8,1232,7,3,4,6,8,1,34,56))
print(sum_of_nums(1,2,3,4,5))

def pack_to_dict(**kwargs):
    for key in kwargs:
        print(f'{key} = {kwargs[key]}')
    return kwargs

print(pack_to_dict(name="Tom", age=19, favorite_langauges=["python","go"]))

list_one = [1,2,3]
list_two = [4,5,6]
new_list = [0, *list_one, *list_two]
print(new_list)


for index, item in enumerate([20,30,40]):
    print(index, item)
    #0 20
    #1 30
    #2 40

some_challenges = ["web exploitation", "binary exploitation", "general skills", "reverse engineering", "forensics"]
some_tools = ["Burp suite", "gnu debugger", "shell", "ghidra", "binwalk"]

for challenge, tool in zip(some_challenges, some_tools):
    print(f'{challenge} can be associated with {tool}')

names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
*nordic_countires, es, ru = names
print(nordic_countires, es, ru) 

#exception handling

try:
    print(10 + '5')
except:
    print("something went wrong")

try:
    name = input("What is your name? ")
    age = int(input("What is your age? "))
    year = int(input("What is the year? "))
    print(f'Hello, {name}, you are {age} years old. It is currently {year}')
except:
    print("There was an invalid input")

#exceptions with type

try:
    name = input("What is your name? ")
    year = (input("What year were you born? "))
    age = 2023 - year
    print(f'Hello, {name}, you are {age} years old.')
except TypeError:
    print("There was a type error!")
except ValueError:
    print("There was a value error!")


try:
    #python_is_great = true
    #some_result = 10/0
    print("The end of the try block")
except NameError:
    print("But python is great!")
except ZeroDivisionError:
    print("You tried to divide by zero")
else:
    print("There were no errors, amazing!")
finally:
    print("I definitely learned about exception handling")

