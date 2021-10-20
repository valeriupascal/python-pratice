# Program for recursive binary search
# returns index of x if present, else is -1

def binary_search(arr, low, high, x):

    # check base case
    if high >= low:
        mid = (high + low) // 2

        # if element is present at the middle
        if arr[mid] == x:
            return mid

        # if element is smaller than mid, then it is present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

        # else the element is in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        # element is not in the list
        return -1



# TEST ARRAY
arr = [2, 5, 7, 33, 67, 89]
x = 67

# Function call
result = binary_search(arr, 0, len(arr) - 1, x)

if result != -1:
    print("ELEMENT is present at index: ", str(result))
else:
    print("NOT PRESENT")
