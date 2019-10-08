import math

def nth_fibo_term(n):
	c=math.sqrt(5)

	exp= int((((1+c)**n) - ((1-c)**n))// ((2**n)*c))

	return exp


def sum_upto_nth_fibo(n):
	
	"""
	The sum till nth fibonacci number can be found as :  F(n+2) - F(2) ie. F(n+2) - 1 

	the nth term can be found as  (  (1+root(5))^n - (1-root(5))^n    ) // (2^n  * root(5))

	hence we have to just find n+2th number and substract 1 from it.

	However this technique of finding nth term can fail over extreemly large values of n

	"""

	final_term=nth_fibo_term(n+2)

	return final_term-1


if __name__ == '__main__':
	n=int(input('Enter the nth term '))
	print(sum_upto_nth_fibo(n))

