from array import array
from sys import getsizeof

my_arr: array[int] = array('i', range(100))
my_list: list[int] = list(range(100))


if __name__ == '__main__':
    print(my_arr)
    print(my_list)

    print('Array:', getsizeof(my_arr), 'bytes')
    # it is faster than list when we store large data in it.
    # because it stores one data type in it.
    # arrays store data in much more compact manner than list.
    print('List:', getsizeof(my_list), 'bytes')
