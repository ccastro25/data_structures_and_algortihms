
import math

def bs(arr,t):
    l = 0
    h = len(arr)

    while l < h:
        m = math.floor(l + (h-l)/2)

        if arr[m]==t:
            return m
        elif arr[m] < t:
            l = m+1
        else:
            h = m
            
    return -4

