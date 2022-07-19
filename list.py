"""
my_list = ["banana", "cherry", "apple"]
print(my_list)

my_list.append("lemon")
print(my_list)

my_list.insert(1, "blueberry")
print(my_list)

item = my_list.pop()
print(item)

item = my_list.remove("cherry")
print(my_list)

item = my_list.reverse()
print(my_list)

item = my_list.clear()
print(my_list)

my_numbers = [1, 9, 5, 6, 3, 2]
my_numbers.sort()

print(my_numbers)
"""
new_list = [0] * 5
print(new_list)

new_list2 = [1, 2, 3, 4, 5]

join_list = new_list + new_list2
print(join_list)

a = new_list2[::-1]
print(a)

"""
if "lemon" in my_list:
    print("yes")
else:
    print("no")
"""

mylist = [1, 2, 3, 4, 5, 6, 7]
b = [i*i for i in mylist]

print(mylist)
print(b)











