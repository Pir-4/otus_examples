def squares(max):
    for index in range(max):
        yield index ** 2


for i in squares(4):
    print(i)

print("******")

generator = squares(5)
print(next(generator))
print(next(generator))
print("******")


# списочные выражения
my_tuple = (x ** 2 for x in range(5))
print(tuple(my_tuple))

my_list = [x ** 3 for x in range(5)]
print(my_list)

my_dict = {x: x ** 2 for x in range(5)}
print(my_dict)

print("******")

my_dict_2 = {x: x ** 2 for x in range(5) if x % 2 == 0}
print(my_dict_2)
