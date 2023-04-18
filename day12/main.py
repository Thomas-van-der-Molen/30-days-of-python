from mymodule import generate_full_name, userid_gen_by_user, rgb_color_gen, list_of_hexa_colors, generate_colors as gen_colors, shuffle_list, get_random_list

print(userid_gen_by_user())
print(rgb_color_gen())
print(list_of_hexa_colors(2))

print(gen_colors('rgb', 5))
print(gen_colors('hexa', 5))
print(gen_colors('hexadecimal', 10))
print(gen_colors())

a_list = [1,2,3,4,5,6,7]
another_list = ['programming','in','python','is','fun',[1,2,3,4,5],{"tom" : "vdm"}]

print(shuffle_list(a_list))
print(shuffle_list(a_list))
print(shuffle_list(a_list))
print(shuffle_list(another_list))
print(shuffle_list(another_list))

print(get_random_list())
print(get_random_list())
print(get_random_list())
