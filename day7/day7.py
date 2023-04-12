
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add("Twitter")
it_companies.update(["Tesla","Spacex","OpenAI","Uber","ASML"])
it_companies.remove("Uber")

#A.update(B)

print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
print(A.symmetric_difference(B))

#del A
#del B

print(len(A))
print(len(list(A)))

#A string is an array of characters
#A list is an unordered collection of data, it is mutable
#A tuple is also an unordered collection of data, but it is immutable
#A set is a collection of unordered, but unique, data, and it is mutabls

a_str = "I am a teacher and I love to inspire and teach people."
a_str = a_str.split(" ")
a_str = set(a_str)
print("unique words in the sentence: ", len(a_str))