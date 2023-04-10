my_list = []
list_with_items = [5, "rain", "cafe", "simple", 4.0]
print(len(list_with_items))

print(list_with_items[0], list_with_items[2], list_with_items[4])

mixed_data_types =["Tom", 21, "5'10", "single", "United States"]

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies)
print(len(it_companies))
print(it_companies[0])
print(it_companies[3])
print(it_companies[6])

it_companies[0] = "ASML"
print(it_companies)
it_companies.append("OpenAI")
it_companies.insert(3, "Kudu dynamics")
print(it_companies)

it_companies[-1] = it_companies[-1].upper()

print("; ".join(it_companies))
print("Tesla" in it_companies)

it_companies.sort()
it_companies.reverse()
print(it_companies)

print(it_companies[3:])
print(it_companies[:6])

it_companies.pop(0)
it_companies.pop(len(it_companies)//2)
it_companies.pop()
print(it_companies)


front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print(front_end)

full_stack = front_end.copy()

full_stack.insert(full_stack.index("Redux")+1, "Python")
full_stack.insert(full_stack.index("Redux")+1, "SQL")
print(full_stack)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages[0])
print(ages[-1])
print(ages[len(ages)//2])

print(ages[-1] - ages[0])

avg = 0
for x in ages:
    avg+=x
print(avg/len(ages))#average age

