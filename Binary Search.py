def binary_search_iterative(sorted_list: list, element):
    start = 0
    end = len(sorted_list) - 1
    while start <= end:
        mid = (start + end) // 2
        if element == sorted_list[mid]:
            return mid
        elif element > sorted_list[mid]:
            start = mid + 1
        elif element < sorted_list[mid]:
            end = mid - 1
    else:
        return -1


def binary_search_recursive(sorted_list: list, element, start, end):
    if start <= end:
        mid = (start + end) // 2
        if element == sorted_list[mid]:
            return mid
        elif element > sorted_list[mid]:
            return binary_search_recursive(sorted_list, element, mid + 1, end)
        elif element < sorted_list[mid]:
            return binary_search_recursive(sorted_list, element, 0, mid)
    else:
        return -1


ls = [1, 2, 3, 4, 5]
print(binary_search_iterative(ls, 4))
print(binary_search_recursive(ls, 4, 0, len(ls) - 1))




