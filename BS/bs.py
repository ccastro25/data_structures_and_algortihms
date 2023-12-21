import math

def bs(arr,t):
	l =0
	h = len(arr)
	while l<h:
		m = math.floor(l+(h-l)/2)
		if t == arr[m]:
			return m
		elif t > arr[m]:
			l = m +1
		else:
			h = m
	return -4
