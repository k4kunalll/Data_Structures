def findPeakElement(arr: [int]) -> int:
    if len(arr) == 1:
        return 0
    elif arr[0] > arr[1]:
        return 0
    elif arr[len(arr) - 1] > arr[len(arr) - 2]:
        return len(arr) - 1

    low = 1
    high = len(arr) - 2

    while low <= high:
        mid = low + high // 2

        if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
            return mid

        elif arr[mid] > arr[mid - 1]:
            low = mid + 1

        elif arr[mid] < arr[mid + 1]:
            high = mid - 1

        print(low, high, mid)


arr = [1, 2, 3, 4, 5]
findPeakElement(arr)
