str="k2jsv21nkjn8urlkmc786lm90"
ss="hgk890kn89"

def findMxN(ss):
	print(ss)
	new_int=[];c=0;nstr=''
	for i in range(0,len(ss)):
		print(i)
		j=i+1
		if ss[i].isdigit():
			#print('start')
			while ss[j].isdigit() is True:
				j+=1
			nstr=ss[i:j]
			print(nstr+"j: ",+j)
			new_int.append(int(nstr))
		i=j
		print(i)
	print(new_int)

findMxN(ss)