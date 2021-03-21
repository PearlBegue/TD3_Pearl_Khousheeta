#!/bin/bash
def mul_num(a,b):
    multiply=a*b;
    return multiply;

def main():
	import sys
	print(sys.argv)
	i=(len(sys.argv)-1)
	print("le nombre d'arguments : ",i)
	
	if (i==0):
                num1=int(input("Inserer le premier argument : "))
                num2=int(input("Inserer le deuxiement argument : "))
		x = int (num1)
		y = int (num2)
		print(mul_num(x,y))
	elif (i==1):
		num1=int(input("Inserer le deuxieme argument :"))
		x = int(sys.argv[1])
		y = (num1)
		print(mul_num(x,y))
	elif (i==2):
		x = int (sys.argv[1])
		y = int (sys.argv[2])
 		print(mul_mul(x,y))
	else:
		print("erreur :  veuillz inserer que deux arguments")

main()

