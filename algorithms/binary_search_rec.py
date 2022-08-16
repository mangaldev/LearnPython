arr = [1, 2, 3, 4, 5]

number_to_find = 4
low = 0
high = len(arr) - 1
result = -1


def binarySearch(arr, x, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if x == arr[mid]:
            return mid
        elif x > arr[mid]:
            return binarySearch(arr, x, mid + 1, high)
        else:
            return binarySearch(arr, x, low, mid - 1)


print(binarySearch(arr, number_to_find, low, high))
