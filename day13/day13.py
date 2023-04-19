
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

negative_nums = [num for num in numbers if num <= 0]
print(negative_nums)

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

flattened_list = [number for row in list_of_lists for number in row]
print(flattened_list)


list_of_tuples = [(x, x**0, x**1, x**2, x**3, x**4, x**5) for x in range(11)]
print(list_of_tuples)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
new_countries = [[country[0][0].upper(), country[0][0][:3].upper(), country[0][1].upper()] for country in countries]
print(new_countries)

countries = [('Finland', 'Helsinki'), ('Sweden', 'Stockholm'), ('Norway', 'Oslo')]
country_dicts = [{"country" : country[0].upper(), "city": country[1].upper()} for country in countries]
print(country_dicts)

#best resource for difficult comprehensions: https://www.pythonmorsels.com/turning-loop-list-comprehension/#:~:text=Turning%20nested%20for%20loops%20into%20a%20comprehension&text=you%20can%20copy%2Dpaste%20your%20way%20into%20a%20comprehension%20in,your%20way%20into%20a%20comprehension.
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Elon', 'Musk')], [('Bill', 'Gates')]]
new_names = [" ".join(the_tuple) for the_list in names for the_tuple in the_list]
#this was a fun challenge!
print(new_names)

area_of_circle = lambda radius : 3.14 * (radius ** 2)
print(area_of_circle(5))