# with O(n) complexity
def max_subarray1(nums):
    current_profit = nums[0]
    current_max_profit = nums[0]

    for i in range(1, len(nums)):
        current_profit += nums[i]
        if current_profit > current_max_profit:
            current_max_profit = current_profit

        if current_profit < 0:
            current_profit = 0


    return current_max_profit


# with O(n^2) complexity
def max_subarray2(nums):
    max_profit = 0
    for i in range(len(nums)):
        profit = 0
        for j in range(i, len(nums)):
            profit += nums[j]
            if profit > max_profit:
                max_profit = profit
    return max_profit


# with O(nlog(n)) complexity
def find_max_cross_sub(arr, low, mid, high):
    left_sum = 0
    max_left_index = 0
    sum = 0
    for i in range(mid, low - 1, -1):
        sum += arr[i]
        if sum > left_sum:
            left_sum = sum
            max_left_index = i
    right_sum = 0
    max_right_index = 0
    sum = 0
    for j in range(mid + 1, high + 1):
        sum += arr[j]
        if sum > right_sum:
            max_right_index = j
            right_sum = sum
    return max_left_index, max_right_index, left_sum + right_sum


def max_subarray3(arr, low, high):
    if low == high:
        return low, high, arr[low]
    else:
        mid = low + (high - low) // 2
        left = max_subarray3(arr, low, mid)
        right = max_subarray3(arr, mid + 1, high)
        cross = find_max_cross_sub(arr, low, mid, high)
        if left[2] > right[2] and left[2] > cross[2]:
            return left
        if right[2] > left[2] and right[2] > cross[2]:
            return right
        else:
            return cross


ls = [4, -1, 7, 8, -4, 5, -1, 23, -2]
print('Max subarray (with O(n)) sum = ', max_subarray2(ls))
print('Max subarray (with O(n^2)) sum = ', max_subarray1(ls))
print('Max subarray (with O(n log n)) sum = ', max_subarray3(ls, 0, len(ls) - 1))






