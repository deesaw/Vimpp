#0,1,1,2,3,5,8,13 - fib
#write a program to print all fib numbers till 1000
a,b=0,1
while a < 1000:
	print(a)
	a,b=b,a+b
