def rotated_array(array, target):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        # left sorted
        elif array[low] <= array[mid]:
            if array[low] <= target <= array[mid]:
                high = mid - 1
            else:
                low = mid + 1
        # right sorted
        else:
            if array[mid] <= target <= array[high]:
                low = mid + 1
            else:
                high = mid - 1

    else:
        return -1


if __name__ == "__main__":
    array = [8, 9, 10, 11, 12, 1, 2, 4, 5, 6, 7]
    target = 55
    print(rotated_array(array, target))
