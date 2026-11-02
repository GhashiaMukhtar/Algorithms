def mrege_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array)//2
    left_arr  = array[:mid]
    right_arr = array[mid:]

    left_sorted = mrege_sort(left_arr)
    right_sorted = mrege_sort(right_arr)

    return merge(left_sorted,right_sorted)


def merge(left_arr,right_arr):
    sorted_array = []

    i = j = 0

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            sorted_array.append(left_arr[i])
            i += 1
        else:
            sorted_array.append(right_arr[j])
            j += 1

    sorted_array.extend(left_arr[i:])
    sorted_array.extend(right_arr[j:])

    return sorted_array




inp = [int(x) for x in input("Enter an array:\n").replace(",", " ").split()]
print("result:", mrege_sort(inp))