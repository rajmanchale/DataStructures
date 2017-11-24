str=input("enter here :")
b=str.split()
c=[]
for i in range(0,len(b)):
	for j in range(1,len(b[i])):
		if (b[i][0] is b[i][j]):
			c.append(b[i])
			break
print(c)