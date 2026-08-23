def selection_sort(array):
    n = len(array)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if array[min_idx] > array[j]:
                min_idx = j
            else:
                continue
        array[i], array[min_idx] = array[min_idx], array[i]
    return array



inp = [int(x) for x in input("Enter an array:\n").replace(",", " ").split()]
print("result:", selection_sort(inp))       
