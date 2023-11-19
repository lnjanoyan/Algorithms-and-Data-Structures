def selection_sort_min(ls):
    for i in range(len(ls)):
        min_ind = i
        for j in range(i, len(ls)):
            if ls[j] < ls[min_ind]:
                min_ind = j
        ls[i], ls[min_ind] = ls[min_ind], ls[i]


def selection_sort_max(arr):
    for i in range(len(arr) - 1):
        max = len(arr) - i - 1
        for j in range(len(arr) - i):
            if arr[j] > arr[max]:
                max = j
        arr[len(arr) - i - 1], arr[max] = arr[max], arr[len(arr) - i - 1]


# another version
# def selection_sort_max(ls):
#     for i in range(len(ls) - 1, -1, -1):
#         max = i
#         for j in range(i):
#             if ls[j] > ls[max]:
#                 max = j
#         ls[i], ls[max] = ls[max], ls[i]
#     return ls


ls = [7, 12, 0, 4, 6, 3, 2, 1, -22]
print(ls)
# selection_sort_min(ls)
selection_sort_max(ls)
print(ls)
