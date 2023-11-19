# #first element pivot
# def partition(arr, first, last):
#     key = arr[first]
#     i = first + 1
#     j = last
#     while True:
#         while i <= j and arr[j] >= key:
#             j -= 1
#         while i <= j and arr[i] < key:
#             i += 1
#         if i <= j:
#             arr[i], arr[j] = arr[j], arr[i]
#         else:
#             break
#     arr[first], arr[j] = arr[j], arr[first]
#
#     return j
#

# # last element pivot
# def partition(arr, first, last):
#     key = arr[last]
#     i = first - 1
#     for j in range(first, last):
#         if arr[j] <= key:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]
#     arr[i + 1], arr[last] = arr[last], arr[i + 1]
#     return i+1


# # random element pivot
# import random
#
#
# def partition(arr, first, last):
#     pivot = random.randrange(first, last)
#     arr[pivot], arr[last] = arr[last], arr[pivot]
#     key = arr[last]
#     i = first - 1
#     for j in range(first, last):
#         if arr[j] <= key:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]
#     arr[last], arr[i + 1] = arr[i + 1], arr[last]
#     return i + 1

def median(arr, first, last):
    mid=(first + last) // 2
    a = arr[first]
    b = arr[last]
    c = arr[mid]
    if a <= b <= c or a >= b >= c:
        return last
    elif a >= c >= b or a <= c <= b:
        return mid
    else:
        return first


def partition(arr, first, last):
    pivot = median(arr, first, last)
    key = arr[pivot]
    arr[pivot], arr[last] = arr[last], arr[pivot]
    i = first - 1
    for j in range(first, last):
        if arr[j] < key:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[last] = arr[last], arr[i + 1]
    return i + 1


def quick_sort(arr, first, last):
    if first < last:
        pivot = partition(arr, first, last)
        quick_sort(arr, first, pivot - 1)
        quick_sort(arr, pivot + 1, last)


ls = [1, 3, 4, 9, 7, 6, 8]
print(ls)
quick_sort(ls, 0, len(ls) - 1)
print(ls)
