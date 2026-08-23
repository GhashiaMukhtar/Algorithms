def insertion_sort(array):
    n = len(array)
    for i in range(1,n):
        key = array[i]
        j = i-1
        while j>=0 and key<array[j]:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key
        
    return array

inp = [int(x) for x in input("Enter an array:\n").replace(",", " ").split()]
print("result:", insertion_sort(inp))