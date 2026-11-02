def sort_and_count(array):
    if len(array) <= 1:
        return array, 0

    mid = len(array)//2
    left_arr  = array[:mid]
    right_arr = array[mid:]

    left_sorted, left_count = sort_and_count(left_arr)
    right_sorted, right_count = sort_and_count(right_arr)
    merged, split_count = merge_and_count(left_sorted,right_sorted)

    return merged, left_count + right_count + split_count


def merge_and_count(left_arr,right_arr):
    sorted_array = []
    count = 0

    i = j = 0

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            sorted_array.append(left_arr[i])
            i += 1
        else:
            sorted_array.append(right_arr[j])
            j += 1
            # Everything left in left_arr is bigger than this right element
            count += len(left_arr) - i

    sorted_array.extend(left_arr[i:])
    sorted_array.extend(right_arr[j:])

    return sorted_array, count


inp = [int(x) for x in input("Enter an array:\n").replace(",", " ").split()]
result, inversions = sort_and_count(inp)
print("sorted:", result)
print("inversions:", inversions)
