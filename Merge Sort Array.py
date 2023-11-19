# def merge(arr, first, mid, last):
#     first1 = first
#     last1 = mid
#     first2 = mid + 1
#     last2 = last
#     index = first
#     tmp = list(arr)
#     while first1 <= last1 and first2 <= last2:
#         if arr[first1] <= arr[first2]:
#             tmp[index] = arr[first1]
#             first1 += 1
#             index += 1
#
#         else:
#             tmp[index] = arr[first2]
#             first2 += 1
#             index += 1
#
#     while first1 <= last1:
#         tmp[index] = arr[first1]
#         first1 += 1
#         index += 1
#     while first2 <= last2:
#         tmp[index] = arr[first2]
#         first2 += 1
#         index += 1
#     for i in range(first, index):
#         arr[i] = tmp[i]
#
#
# def merge_sort(arr, first, last):
#     if first < last:
#         mid = first + (last - first) // 2
#         merge_sort(arr, first, mid)
#         merge_sort(arr, mid + 1, last)
#         merge(arr, first, mid, last)
#
#




def merge(start, mid, end, arr):
    st1 = start
    end1 = mid
    st2 = mid + 1
    end2 = end
    tmp = arr.copy()   #karevor a vor copy-n lini
    i = start
    while st1 <= end1 and st2 <= end2:
        if arr[st1] <= arr[st2]:
            tmp[i] = arr[st1]
            st1 += 1
            i += 1
        else:
            tmp[i] = arr[st2]
            st2 += 1
            i += 1

    while st1 <= end1:
        tmp[i] = arr[st1]
        st1 += 1
        i += 1

    while st2 <= end2:
        tmp[i] = arr[st2]
        st2 += 1
        i += 1

    for j in range(start, i):
        arr[j] = tmp[j]


def merge_sort(arr, start, end):
    if start < end:
        mid = start + (end - start) // 2
        merge_sort(arr, start, mid)
        merge_sort(arr, mid + 1, end)
        merge(start, mid, end, arr)


arr = [1, 5, 3, 6, 9, 42, 46,8]
print(arr)
merge_sort(arr, 0, len(arr) - 1)
print(arr)


arr = [3, 7, 4, 6, 1, 8, 9,11]
print(arr)
merge_sort(arr, 0, len(arr) - 1)
print(arr)