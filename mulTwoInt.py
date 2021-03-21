#!/bin/bash
def mul_num(a,b):
    multiply=a*b;
    return multiply;
def main():
    num1=int(input("entrez le premier numero"));
    num2=int(input("entrez le deuxieme numero"));
    print("Le produit des 2 chiffres est",mul_num(num1,num2));
main()
