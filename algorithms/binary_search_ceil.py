arr = [1, 20, 35, 42, 57]

number_to_find = 0
low = 0
high = len(arr) - 1
result = -1
while low <= high:
    mid = low + (high - low) // 2
    if number_to_find < arr[mid]:
        result = mid
        high = mid - 1
    elif number_to_find > arr[mid]:
        low = mid + 1
    else:
        result = mid
        break

print(result)
