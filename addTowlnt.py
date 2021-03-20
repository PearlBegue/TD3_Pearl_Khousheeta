#!/bin/bash
def add_num(a,b):
    sum=a+b;
    return sum;
def main():
    num1= int (2);
    num2= int (3);
    num3= int (1);
    number=(num1,num2,num3);
    calculate=int(add_num(num1,num2))
    if (number != 2) :
        print("Number 1 is :",num1," Number 2 is :",num2,"Number 3 is",num3," and Sum is",calculate);
    else:
        print("Error Try again, 3 arguements");
main()
