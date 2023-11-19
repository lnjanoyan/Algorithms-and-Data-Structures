def ins_sort(ls):
    for j in range(1, len(ls)):
        key = ls[j]
        i = j - 1
        while i >= 0 and ls[i] > key:
            ls[i + 1] = ls[i]
            i -= 1
        ls[i + 1] = key
    return ls


def insertion_sort(ls):
    for i in range(1, len(ls)):
        key = ls[i]
        sorted = i - 1
        while ls[sorted] >= key and sorted >= 0:
            ls[sorted + 1] = ls[sorted]
            sorted -= 1
        ls[sorted + 1] = key
    return ls


print(insertion_sort([-1, 5, 4, 0, 1, 8, 6, -5]))


