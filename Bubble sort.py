def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n - 1):
        swapped = False
        
        for j in range(n - 1 - i):  #-i потому что последние i элементов уже на месте
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        if not swapped:
            break
    
    return arr
    
arr1 = [60, 4, 25, 2, 22, 11, 90]
print("До:", arr1)
print("После:", bubble_sort(arr1.copy()))
