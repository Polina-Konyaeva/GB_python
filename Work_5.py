from functools import reduce
list_1 = [i for i in range(100, 1001) if i % 2 == 0]
print(list_1)
mult_num = reduce(lambda num_1, num_2: num_1 * num_2, list_1)
print(mult_num)