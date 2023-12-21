import qs

arr = [44,3,55,2,6,57,21,8]
qs.quiks(arr)
assert arr == [2,3,6,8,21,44,55,57], 'arr is not sorted, it instead has {0}'.format(arr)
arr = [-44,3,55,2,-6,57,21,-8]
qs.quiks(arr)
assert arr == [-44, -8, -6, 2, 3, 21, 55, 57], 'arr is not sorted, it instead has {0}'.format(arr)
print("qs test complete")