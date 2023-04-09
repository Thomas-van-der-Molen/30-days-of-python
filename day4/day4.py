
a_long_string = "Thirty " + "days " + "of " + "Python"
another_string = "Coding " + "for " + "all"


print(a_long_string)
print(another_string)
print(f'The length of a_long_string is {len(a_long_string)} and the contents is {a_long_string}')
print(f'upper() is a function which capitalizes all letters in a string, like this: {another_string.upper()}')
print(f'lower() is a similar function, {a_long_string.lower()}')

print(f'the capitalize() function is neat: {a_long_string.capitalize()}')
print(f'I\'ve never used the title() function before! - {a_long_string.title()}')
print(f'The Swapcase() function is also new to me {a_long_string.swapcase()}')

print(f'slicing can be useful - {a_long_string.split(" ")[0]}')

print(f'The index of coding in another_string is {another_string.find("Coding")}')

print(f'{another_string.replace("Coding", "Python")}')

print(f'{another_string.split(" ")}')
print(f'{another_string[0]}')
print(f'{another_string[-1]}')
print(f'{another_string[10]}')

print(f'{another_string.index("C")}')
print(f'{another_string.rfind("l")}')

a_new_string = "You cannot end a sentence with because because because is a conjunction"
print(f'{a_new_string.index("because")}')
print(f'{a_new_string.rindex("e")}')
print(f'{a_new_string[31:54]}')

print(f'{another_string.startswith("Coding")}')
print(f'{another_string.endswith("coding")}')

print(f'{"   Coding For All      ".strip(" ")}')

