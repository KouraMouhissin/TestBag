#coding:utf-8

"""
Création d'une suite de fibonachi
"""
a=1
b=0
x=1
y=2
print(x)
print(y)
while a < 100000:
	b=x+y
	x=y
	y=b

	a=a+1
	print(b)