from random import randint
def generate_full_name(firstname, lastname):
    return firstname + ' ' + lastname


def userid_gen_by_user():
    chars = int(input("What is the number of characters? "))
    ids = int(input("What is the number of IDS to generate? "))
    rtrn = []
    for i in range (ids):
        strn = []
        for j in range(chars):
            upper_lower = randint(0,1)
            if upper_lower == 0:
                strn.append(chr(randint(65,90)))
            else:
                strn.append(chr(randint(97,122)))
            
        rtrn.append(''.join(strn))
    return rtrn

def rgb_color_gen(num_colors = 1):
    colors = []
    for i in range(num_colors):
        colors.append((randint(0,255),randint(0,255),randint(0,255)))
    return colors

def list_of_hexa_colors(num_colors = 1):
    hex_colors = []
    for x in range(num_colors):
        color = ['#']
        for j in range(6):
            num = randint(0,16)
            if num >=  10:
                color.append(chr(55+num))
            else:
                color.append(str(num))
        hex_colors.append(''.join(color))
    return hex_colors

def generate_colors(type = "rgb", num_colors = 1):
    if type == "rgb":
        return rgb_color_gen(num_colors)
    else:
        return list_of_hexa_colors(num_colors)

def shuffle_list(input_list):
    for item in input_list:
        randindex = randint(0,len(input_list)-1)
        current_index = input_list.index(item)
        temp = input_list[randindex]
        input_list[randindex] = input_list[current_index]
        input_list[current_index] = temp
    return input_list

def get_random_list():
    return_list = []
    for i in range(7):
        num = randint(0,9)
        while num in return_list:
            num = randint(0,9)
        return_list.append(num)
    return return_list
