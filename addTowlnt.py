#!/bin/bash
def add_num(a,b):
    sum=a+b;
    return sum;
def main():
    num1= int(input("Enter the number 1: "));
    num2= int(input("Enter the number 2: "));
    calculate=int(add_num(num1,num2));
    print("Number 1 is :",num1," Number 2 is :",num2," and Sum is",calculate);
main()
