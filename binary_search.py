def find_index(num, array):
    index = -1
    for i in range(len(array)):
        if array[i] == num:
            index = i
    return index

def binary_find_index(num, array):
    first = 0
    last = len(array) - 1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first + last) // 2
        if array[mid] == num:
            index = mid
        else:
            if num < array[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return index


num = 4
arr = [1, 2, 3, 4, 5, 7, 8, 10, 13, 14]
# print(find_index(num, arr))
print(binary_find_index(num, arr))
