"""
Pisano Period => length of the repeating sequence we got after getting modulo with m on fibonacci sereis

refrence : https://medium.com/competitive/huge-fibonacci-number-modulo-m-6b4926a5c836

"""
pisano=[0,1]
def pp(m):
	a,b=0,1 # for getting fibonacci and this remains constant for every pisano period (0,1,.....)
	 #=> it is found that max length can be atmost of m*m
	for i in range(3,m*m):
		c=(a+b)%m
		a,b=b,(a+b)
		pisano.append(c)
		if a==0 and b==1:
			break # ie sequence is repeatinf itself

	print(pisano) # the actual sequence
	return len(pisano) # or we can simply just have returned i+1 where we have written break


if __name__=='__main__':
	t=int(input('Enter no of cases : '))
	for i in range(t):
		m=int(input('Enter m : '))
		print(pp(m))

