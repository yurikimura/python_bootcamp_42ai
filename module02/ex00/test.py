from ft_filter import ft_filter
from ft_map import ft_map
from ft_reduce import ft_reduce
from functools import reduce


def multi(x):
    y = x*2
    return y


sample1_list = map(multi, list(range(5)))
sample2_list = ft_map(multi, list(range(5)))

print(f"original: {list(sample1_list)}")
print(f"ft: {list(sample2_list)}")

# filter


def starts_with_A(s):
    return s[0] == "A"


fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
filter_object1 = filter(starts_with_A, fruit)
filter_object2 = ft_filter(starts_with_A, fruit)

print(f"original: {list(filter_object1)}")
print(f"ft: {list(filter_object2)}")

# reduce


def add(x, y):
    return x + y


list = [2, 4, 7, 3]
print(f"original: {reduce(add, list)}")
print(f"ft: {ft_reduce(add, list)}")
