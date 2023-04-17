from countries import countries

def add_two_numbers(num1, num2):
    return num1 + num2

def area_of_circle(radius):
    return 3.14 * (radius ** 2)

def add_all_nums(*nums):
    my_sum = 0
    for num in nums:
        #check for valid datatype
        if(type(num)== type(1)):
            my_sum += num
        else:
            print("one of this inputs is not an int")
            break
            #or return 0
    return my_sum

def convert_celsius_to_fahrenheit(celsius):
    return (celsius * (9/5)) + 32

print(convert_celsius_to_fahrenheit(0))
print(convert_celsius_to_fahrenheit(100))

def check_season(month):
    if month == "December" or month == "January" or month == "February":
        season = "Winter"
    elif month == "March" or month == "April" or month == "May":
        season = "Spring"
    elif month == "June" or month == "July" or month == "August":
        season = "Summer"
    elif month == "September" or month == "October" or month == "November":
        season = "Autumn"
    else:
        season = "invalid input"
    return season

print(check_season("April"))

def print_list(input_list):
    for item in input_list:
        print(item)

print_list(["item1","item2","item3"])

def reverse_list(input_list):
    #using comprehensions would be easier! [::-1]
    output_list = []
    for item in input_list:
        output_list.insert(0,item)
    return output_list

print(reverse_list(['First item', "second item", "third item", 4, 5]))

def capitalize_items(input_list):
    output_list = []
    for item in input_list:
        output_list.append(item.upper())
    return output_list

print(capitalize_items(["lowercase one", "lowercase two", "lowercase three"]))

def add_item(input_list, input_item):
    input_list.append(input_item)
    return input_list

print(add_item([1,2,3],4))

def remove_item(input_list, input_item):
    input_list.remove(input_item)
    return input_list

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9];
print(remove_item(numbers, 3))  # [2, 7, 9]

def sum_of_numbers(input_range):
    my_sum = 0
    for x in range(input_range+1):
        my_sum += x
    return my_sum

print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050


def evens_and_odds(num):
    evens = 0
    odds = 0
    for x in range(num+1):
        if x % 2 == 0:
            evens+=1
        else:
            odds+=1
    return evens, odds

print(evens_and_odds(100))

def factorial(integer):
    factorial = 1
    for x in range(integer):
        factorial *= x+1
    return factorial

print(factorial(5))

def unique_list(input_list):
    tracking_list = []
    unique = True
    for item in input_list:
        if item in tracking_list:
            unique = False
            break
        else:
            tracking_list.append(item)
    return unique

print(unique_list([1,2,3,4,5]))
print(unique_list([1,2,3,4,5,5,4,4,3]))

def same_type(input_list):
    same_type = True
    check_type = type(input_list[0])
    for item in input_list:
        if type(item) != check_type:
            same_type = False
            break
    return same_type

print(same_type([1,2,3,4,5]))
print(same_type([1,2,3,4,5,"test",[1,2,3]]))

def most_populated_countries():
    for i in range(len(countries)-1):
        for j in range(len(countries)-1):
            if countries[j]["population"] < countries[j+1]["population"]:
                temp = countries[j+1]
                countries[j+1] = countries[j]
                countries[j] = temp
    return [countries[x]["name"] for x in range(20)]#hey comprehensions are cool

print(most_populated_countries())
print("\n\n")
def most_spoken_languages():
    language_count = {}
    for country in countries:
        for language in country["languages"]:
            if language in language_count:
                language_count[language] = language_count[language] + 1
            else:
                language_count[language] = 1
    language_list = list(language_count)
    for i in range(len(language_list)-1):
        for j in range(len(language_list)-1):
            if language_count[language_list[j]] < language_count[language_list[j+1]]:
                temp = language_list[j+1]
                language_list[j+1] = language_list[j]
                language_list[j] = temp
    return language_list[:20]#just the 20 most spoken languages

print(most_spoken_languages())