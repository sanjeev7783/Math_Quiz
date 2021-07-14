import random as r
import sys
i=9
correct=0
incorrect=0
while i>0:
    print("**********************")
    print("**A Simple Math Quiz**")
    print("**********************")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Integer Division")
    print("5.Exit")
    print("----------------------")
    choice=int(input("Enter Your choice :"))
    if choice==1:
        a=r.randint(1,30)
        b=r.randint(1,32)
        c=a+b
        print(a,"+",b)
        d=int(input(" = "))
        if d==c:
            print("Correct Answer\n")
            correct=correct+1
            print("\n")
        else:
            print("Incorrect Answer\n")
            incorrect=incorrect+1
            print("\n")
    elif choice==2:
        a=r.randint(30,40)
        b=r.randint(10,30)
        c=a-b
        print(a,"-",b)
        d=int(input(" = "))
        if d==c:
            print("Correct Answer\n")
            correct=correct+1
            print("\n")
        else:
            print("Incorrect Answer\n")
            incorrect=incorrect+1
            print("\n")
           
    elif choice==3:
        a=r.randint(1,30)
        b=r.randint(1,32)
        c=a*b
        print(a,"*",b)
        d=int(input(" = "))
        if d==c:
            print("Correct Answer\n")
            correct=correct+1
            print("\n")
        else:
            print("Incorrect Answer\n")
            incorrect=incorrect+1
            print("\n")  
    elif choice==4:
        a=r.randint(1,30)
        b=r.randint(1,32)
        c=a//b
        print(a,"/",b)
        d=int(input(" = "))
        if d==c:
            print("Correct Answer\n")
            correct=correct+1
            print("\n")
        else:
            print("Incorrect Answer\n")
            incorrect=incorrect+1
            print("\n")
    elif choice==5:
        result=correct-incorrect
        total=correct+incorrect
        percentage=result/total*100
        print("You answered ",total," questions with ",correct," correct and ",incorrect,"incorrect." )
        print("your Score is ",percentage,"% \n Thank You")
        sys.exit()
        
           
