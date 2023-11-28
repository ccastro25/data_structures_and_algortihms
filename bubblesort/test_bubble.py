import bubs


arr = [2,52,44,7,18,9,0]
bubs.bubble_sort(arr)

assert arr == [0,2,7,9,18,44,52], 'array is not correct, it is {0}'.format(arr)
arr = [-2,52,44,7,18,-9,0]
bubs.bubble_sort(arr)
assert arr == [-9,-2,0,7,18,44,52], 'array is not correct, it is {0}'.format(arr)
print('buble sort done')