def bubble_sort(array):
    n = len(array)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
                swapped = True
            else:
                continue
        if not swapped:
            break
    return array

inp = [int(x) for x in input("Enter an array:\n").replace(",", " ").split()]
print("result:", bubble_sort(inp))  
