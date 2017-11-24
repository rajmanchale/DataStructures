def fibo(n):
	a=0;b=1
	print(a,'\n',b)
	for i in range(2,n):
		c=a+b
		print(c)
		a=b
		b=c
n=int(input("Enter no. of elements(please enter more than 2):"))
fibo(n)