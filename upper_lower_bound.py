def lower_bound(arr, k):
    low = 0
    high = len(arr) - 1

    low_bound = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] >= k:
            high = mid - 1
            low_bound = mid
        else:
            low = mid + 1

    print(f"low_bound:{low_bound}")


def upper_bound(arr, k):
    low = 0
    high = len(arr) - 1

    upper_bound = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] > k:
            high = mid - 1
            upper_bound = mid
        else:
            low = mid + 1

    print(f"upper_bound:{upper_bound}")


if __name__ == "__main__":
    arr = [1, 2, 3, 3, 5, 8, 8, 10, 10, 11]
    k = 10
    lower_bound(arr, k)
    upper_bound(arr, k)
