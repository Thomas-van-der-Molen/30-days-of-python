

age = input("What is your age?: ")
age = int(age)

if age >= 18:
    print("You are old enough to drive")
else:
    print(f'You need to wait {18-age} more years to drive')

my_age = 19
your_age = int(input("What is your age?: "))

if my_age < your_age:
    print(f'I am {your_age - my_age} years younger than you')
else:
    print(f'I am {my_age - your_age} years older than you')

num_one = int(input("What is the first number?: "))
num_two = int(input("What is the second number?: "))

if num_one < num_two:
    print(f'{num_one} is less than {num_two}')
elif num_one > num_two:
    print(f'{num_one} is greater than {num_two}')
else:
    print(f'{num_one} is equal to {num_two}')


grade = 100

if grade >= 80:
    print("Grade is A")
elif grade >= 70:
    print("Grade is B")
elif grade >= 60:
    print("Grade is C")
elif grade >= 50:
    print("Grade is D")
else:
    print("Grade is F")

season = input("What is the month?: ")
if season == "December" or season == "January" or season == "February":
    print("It is winter")
elif season == "March" or season == "April" or season == "May":
    print("It is spring")
elif season == "June" or season == "July" or season == "August":
    print("It is summer")
elif season == "September" or season == "October" or season == "November":
    print("It is Autumn")
else:
    print("That doesn't seem to be a valid month")


fruit = input("What is the fruit? ")
fruits = ['banana', 'orange', 'mango', 'lemon']
if fruit in fruits:
    print("That fruit already existed in the list")
else:
    fruits.append(fruit)
    print(fruits)


person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if "skills" in person:
    print(person["skills"][len(person["skills"])//2])#print the middle skill
    if "Python" in person["skills"]:
        print("person is skilled in python")

front_end = ["JavaScript", "React"]
back_end = ["Node", "MongoDB", "Python"]
full_stack = front_end + back_end

if person["skills"] == front_end:
    print("He is a front end developer")
elif person["skills"] == back_end:
    print("He is a back end developer")
elif person["skills"] == full_stack:
    print("He is a full stack developer")
else:
    print("Unknown title")

if person["is_married"] and person["country"] == "Finland":
    print(f'{person["first_name"]} {person["last_name"]} is married and lives in {person["country"]}')