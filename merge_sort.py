#!/usr/bin/python3
import numpy as np
n=int(input('Enter no. of elements to be generated:'))
arr=list(np.random.randint(1,100,size=n))
print('Generated array is:\n{}'.format(arr))
### merge sort
def mergeme(arr):
	if len(arr)>1:
		q=len(arr)//2
		leftarr=arr[:q]
		rightarr=arr[q:]
		mergeme(leftarr)
		mergeme(rightarr)
		i=0;j=0;k=0
		while i<len(leftarr) and j<len(rightarr):
			if leftarr[i]<rightarr[j]:
				arr[k]=leftarr[i]
				i=i+1
			else:
				arr[k]=rightarr[j]
				j=j+1
			k=k+1
		while i<len(leftarr):
			arr[k]=leftarr[i]
			i=i+1
			k=k+1
		while j<len(rightarr):
			arr[k]=rightarr[j]
			j=j+1
			k=k+1
mergeme(arr)
print('Sorted array is:\n{}'.format(arr))