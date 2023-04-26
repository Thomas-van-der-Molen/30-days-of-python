#regular expressions


import re

paragraph = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.'

points = re.findall("-?\d", paragraph)
points = list(map(int, points))
points.sort()
print(points)

distance = points[-1] - points[0]
print(distance)



def is_valid_variable(var_input):
    pattern = r'^\d|-'
    matches = re.search(pattern, var_input)
    if(matches):
        return False
    else:
        return True


print(is_valid_variable('first_name')) # True
print(is_valid_variable('first-name')) # False
print(is_valid_variable('1first_name')) # False
print(is_valid_variable('firstname')) # True

def clean_text(text):
    random_chars = r'%|\$|@|&|;|#'
    return re.sub(random_chars, "", text)

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
print(clean_text(sentence));

