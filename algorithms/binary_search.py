arr = [1, 2, 3, 4, 5]

number_to_find = 1
low = 0
high = len(arr) - 1
result = -1
while low <= high:
    mid = low + (high - low) // 2
    if number_to_find < arr[mid]:
        high = mid - 1
    elif number_to_find > arr[mid]:
        low = mid + 1
    else:
        break

print(result)
