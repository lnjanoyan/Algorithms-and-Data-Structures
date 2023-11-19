def bubble_sort(ls: list):
    for i in range(len(ls)):
        is_swapped = False
        for j in range(len(ls) - i - 1):
            if ls[j] > ls[j + 1]:
                ls[j], ls[j + 1] = ls[j + 1],ls[j]
                is_swapped = True
        if not is_swapped:
            return


ls = [5, 0, 7, 8, 11, 99, 0, -4, ]


print(ls)
bubble_sort(ls)
print(ls)











