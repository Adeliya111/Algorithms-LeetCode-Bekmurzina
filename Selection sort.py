def selection_sort(arr):
    n = len(arr)
    
    for i in range(n - 1):
        mn = i
        
        for j in range(i + 1, n):
            if arr[j] < arr[mn]:
                mn = j
        
        if mn != i:
            arr[i], arr[mn] = arr[mn], arr[i]
    
    return arr
    
arr1 = [64, 25, 12, 22, 11]
print("До:", arr1)
print("После:", selection_sort(arr1.copy()))
