"""
Pisano Period => length of the repeating sequence we got after getting modulo with m on fibonacci sereis

refrence : https://medium.com/competitive/huge-fibonacci-number-modulo-m-6b4926a5c836

"""
# pisano=[]
# def pp(m):
# 	a,b=0,1 # for getting fibonacci and this remains constant for every pisano period (0,1,.....)
# 	 #=> it is found that max length can be atmost of m*m
# 	for i in range(0,m*m):
# 		c=(a+b)%m
# 		a,b=b,c
# 		pisano.append(c)
# 		if a==0 and b==1:
# 			return i+1 # ie sequence is repeatinf itself

# 	 # the actual sequence
# 	 # or we can simply just have returned i+1 where we have written break



pisano=[0,1]
def pisanoPeriod(m):
    previous, current = 0, 1
    for i in range(0, m * m):
        res=(previous + current) % m
        previous, current  = current, res
        pisano.append(res)
        if (previous == 0 and current == 1):
            return i + 1



if __name__=='__main__':
	t=int(input('Enter no of cases : '))
	for i in range(t):
		m=int(input('Enter m : '))
		res=pisanoPeriod(m)
		print(res)
		print(pisano)


