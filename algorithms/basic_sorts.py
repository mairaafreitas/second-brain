from typing import List


def bubble_sort(list: List) -> List:
    for i in range(len(list) - 1, 0, -1):
        for j in range(i):
            if list[j] > list[j + 1]:
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp
    return list


print(bubble_sort([4, 2, 6, 5, 1, 3]))


def selection_sort(my_list: List):
    for i in range(len(my_list) - 1):
        minimum_index = i
        for j in range(i + 1, len(my_list)):
            if my_list[j] < my_list[minimum_index]:
                minimum_index = j
        if i != minimum_index:
            temp = my_list[i]
            my_list[i] = my_list[minimum_index]
            my_list[minimum_index] = temp
    return my_list


print(selection_sort([3, 4, 6, 2, 1, 5]))
