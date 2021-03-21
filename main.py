#!/bin/bash
def add_num(a,b):
    sum=a+b;
    return sum;
def main():
    import sys
    print(sys.argv)
    i=(len(sys.argv)-1)
    print("Amount of arguement:",i)

    ans=str(input("Would you want to addition  if Yes Type Yes or else no Type N: "));
    if (ans == yes):
            print("Amount of arguement:",i);
            if (i==0):
                num1=int(input("Enter the number 1:"));
                num2=int(input("Enter the number 2:"));
                x=int(num1);
                y=int(num2);
                print("The sum is ",add_num(num1,num2));
            elif (i==1):
                n1=int(input("Enter the second number: "));
                x=int(sys.argv[1]);
                y=int(num1);
                print("The sum is ",add_num(x,y));
            elif (i==2):
                x=int(sys.argv[1])
                y=int(sys.argv[2])
                print("The sum is ",add_num(x,y));
            else:
                print ("Error: Please Insert only two arguement")
    else:
        print("Thank you for choosing");
main()

