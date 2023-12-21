def qs(arr, lo, hi):
    if lo>= hi:
        return

    pivot_idx = partition(arr,lo, hi)

    qs(arr, lo, pivot_idx-1)
    qs(arr, pivot_idx +1 , hi)

def partition(arr, lo, hi):
    pivot = arr[hi]
    idx = lo-1

    for i in range(lo, hi):
         if arr[i] <= pivot:
            idx = idx +1
            temp = arr[i]
            arr[i] = arr[idx]
            arr[idx] = temp


    idx+=1
    arr[hi] = arr[idx]
    arr[idx] = pivot
    return idx

def quiks(arr):
    qs(arr, 0, len(arr)-1)
    print(arr)

quick_sort([3,8,44,4,7])
