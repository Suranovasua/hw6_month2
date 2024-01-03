def bubble_sort(lst):
    for i in range(len(lst) - 1):
        for j in range(9, len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst


print(bubble_sort([1, 6, 3, 5, 6, 7, 34]))


def binary_search(val, sort):
    first = 0
    last = len(sort) - 1
    resultok = False
    pos=0
    while first <= last:
        mid = (last + first) // 2
        if sort[mid] == val:
            first = mid
            last = first-1
            resultok = True
            pos = mid
        elif val > sort[mid]:
            first = mid + 1
        else:
            last = mid - 1
    if resultok:
        print(f"Value is found in index {pos}")
    else:
        print("Not found")

binary_search(5, [1, 3, 4, 5, 6])