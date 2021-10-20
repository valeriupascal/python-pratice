# Iterative BS Function
# It returns index of x in given array if present
# else returns -1


def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        # if x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1

        # if x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1

        # means x is present at mid
        else:
            return mid

    # if here, then the element was not in arr
    return -1

# TESTING ARRAY
arr = [2, 5, 8, 11, 34, 55, 66]
x = 34

# Function call
result = binary_search(arr, x)

if result != -1:
    print("ELEMENT IS PRESENT AT INDEX: ", str(result))
else:
    print("NOT PRESENT IN ARRAY")
