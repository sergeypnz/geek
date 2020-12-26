my_str = input("Введите строку")
my_world = []
num = 1
for el in range(my_str.count(' ') + 1):
    my_world = my_str.split()
    if len(str(my_world)) <=  10:
        print(f" {num} {my_world [el]}")
        num += 1
    else:
        print(f" {num} {my_world [el] [0:10]}")
        num += 1