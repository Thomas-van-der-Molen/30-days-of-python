

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#map will apply a function to all elements of an iterable
#filter will do the same, but it will return a new iterable


def capitalize(country):
    return country.upper()

new_countries = map(capitalize, countries)
print(list(new_countries))

def square(num):
    return num ** 2

new_nums = map(square, numbers)
print(list(new_nums))

new_names = map(capitalize, names)
print(list(new_names))

def land_filter(country):
    if "land" in country:
        return True
    else:
        return False

filtered_countries = filter(land_filter, countries)
print(list(filtered_countries))

def land_filter(country):
    if len(country) == 6:
        return True
    else:
        return False

filtered_countries = filter(land_filter, countries)
print(list(filtered_countries))

def land_filter(country):
    if len(country) >= 6:
        return True
    else:
        return False

filtered_countries = filter(land_filter, countries)
print(list(filtered_countries))

def land_filter(country):
    if country.startswith("E"):
        return False
    else:
        return True

filtered_countries = filter(land_filter, countries)
print(list(filtered_countries))

def get_string_lists(input_list):
    return map(str, input_list)

def add_nums(numone, numtwo):
    return numone + numtwo

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

def split_decorator(function):
    def wrapper():
        func = function()
        split = func.split()
        return split
    return wrapper

@split_decorator
@uppercase_decorator
def greeting():
    return "Welcome to python"

print(greeting())

#wow, decorators are complex and cool
def type_check(correct_type):
    #print(correct_type)#<class 'int'>
    def outer(func):
        def wrapper(func_input):
            result = func(func_input)
            if type(result) == correct_type:
                #print("correct type")
                return func(func_input)
            else:
                print("incorrect type")
        return wrapper
    return outer
    

@type_check(int)
def times2(num):
    return num*2

print(times2(2))
times2('Not A Number')

@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
first_letter(['Not', 'A', 'String'])