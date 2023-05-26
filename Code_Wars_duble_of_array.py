# Given an array of integers, return a new array with each value doubled.
#
# For example:
#
# [1, 2, 3] --> [2, 4, 6]

def duble_array(array: list[int]) -> list[int]:
    res_array = array  # equalate the lists to equal quantity of elements
    count = 0  # declare counter of bumber of elements
    for i in array:  # for i elements
        element = i * 2  # double it
        res_array[count] = element  # assigned to variables
        count += 1  # increase counter on one
    return print(res_array)  # see result


if __name__ == '__main__':
    duble_array([2, 3, 9, 234])




