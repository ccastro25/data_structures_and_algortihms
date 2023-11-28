def bubble_sort(arr):
  
    l = len(arr)
     
    for i in range(l-1):
        swapped = False
        
        for j in range(l-i-1):
            if arr[j]> arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                swapped = True
        if not swapped:
            return 