import math


def max_sum(arr):
    max_sum = arr[0]
    current_sum = arr[0]
    for num in arr[1:]:
        current_sum = current_sum + num
        if current_sum < num:
            current_sum = num
        max_sum = math.max(max_sum,current_sum)
    return max_sum
                    