
from math import *

def inp():
	x=int(input())
	return x



print("Enter a:")
a=inp()
print("Enter b:")
b=inp()
print("Enter c:")
c=inp()


def roots(a,b,c):
	d=((b**2)-(4*a*c))
	if d>0:
		print("there are two roots\n")
		x1=((-b+sqrt(d))/(2*a))
		x2=((-b-sqrt(d))/(2*a))
		print(x1)
		print(x2)
	elif d==l:
		print("there is only one root\n")
		x1=(-b/(2*a))
		print(x1)
	else:
		print("there are two roots\n")
		x=(-b/(2*a))
		print(str(x)+"+"+str(sqrt(-1*d)/(2*a))+"i")
		print(str(x)+"-"+str(sqrt(-1*d)/(2*a))+"i")



roots(a,b,c)
