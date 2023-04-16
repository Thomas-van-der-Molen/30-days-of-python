
from countries import countries

count = 0
while count <= 10:
    print(count)
    count+=1

print()
for x in range(11):
    print(x)

print()
count = 10
while count >= 0:
    print(count)
    count-=1

print()
for x in range(10,-1,-1):
    print(x)

for x in range(7):
    print('#' * x)

for x in range(5):
    for y in range(5):
        print("# ",end = '')
    print()

for x in range(10):
    print(f'{x} x {x} = {x * x}')

my_list = ['Python', 'Numpy','Pandas','Django', 'Flask']
for item in my_list:
    print(item)

for x in range(101):
    if x%2 == 0:
        print(x,end=",")
print()

for x in range(101):
    if x%2 != 0:
        print(x,end=",")
print()

my_sum = 0
for x in range(101):
    my_sum += x
print("The sum of all numbers is ", my_sum)

sum_of_even = 0
sum_of_odd = 0
for x in range(101):
    if x%2 ==0:
        sum_of_even += x
    else:
        sum_of_odd +=x
else:
    print(f'sum of even is {sum_of_even} and sum of odd is {sum_of_odd}')

fruits = ['banana', 'orange', 'mango', 'lemon']
rev_fruits = []
for fruit in fruits:
    rev_fruits.insert(0, fruit)
print(rev_fruits)

for country in countries:
    if "land" in country["name"]:
        print(country["name"],end=",")
else:
    print("\n\n")

language_count = {}
languages = 0

for country in countries:
    for language in country["languages"]:
        if language not in language_count:
            language_count[language] = 0
            languages+=1
        else:
            language_count[language] = language_count[language] + 1
else:
    print("number of languages: ",languages)


print("\n\n")

top_languages = list(language_count)

for i in range(len(language_count)-1):
    for j in range(len(language_count)-1):
        if language_count[top_languages[j]] < language_count[top_languages[j+1]]:
            temp = top_languages[j+1]
            top_languages[j+1] = top_languages[j]
            top_languages[j] = temp

print(f'language one: {top_languages[0]} is {language_count[top_languages[0]]}')
print(f'language two: {top_languages[1]} is {language_count[top_languages[1]]}')
print(f'language three: {top_languages[2]} is {language_count[top_languages[2]]}')

#no extra space was needed to determine the top languages either, it could have been done in-place
for i in range(len(countries)-1):
    for j in range(len(countries)-1):
        if countries[j]["population"] < countries[j+1]["population"]:
            temp = countries[j+1]
            countries[j+1] = countries[j]
            countries[j] = temp


print(f'Population one: {countries[0]["name"]} is population {countries[0]["population"]}')
print(f'Population two: {countries[1]["name"]} is population {countries[1]["population"]}')
print(f'Population three: {countries[2]["name"]} is population {countries[2]["population"]}')