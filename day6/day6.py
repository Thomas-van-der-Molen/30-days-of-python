
my_tuple = ()

my_siblings = ("my oldest sister","my second sister", "my third sister")
print(len(my_siblings))

my_siblings = list(my_siblings)
my_family = my_siblings.copy()
my_family.append("my mother")
my_family.append("my father")
my_family = tuple(my_family)

member1, member2, member3, *parents = my_family
print(member1, member2, member3, parents)

fruits = ("peaches","raspberries","blueberries","strawberries","oranges")
vegetables = ("broccoli","asparagus","cauliflower","peppers","spinach","peas","carrots")
animal_products = ("turkey","salmon","beef","chicken")
food_stuff_tp = fruits + vegetables + animal_products
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_tp)
print(food_stuff_lt[len(food_stuff_lt)//2])#middle items

print(food_stuff_lt[:3])#first three
print(food_stuff_lt[-3:])#last three
del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)

