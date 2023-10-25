print("welcome to srujan's calculator\n")

num1=int(input("enter the 1 st number "))
num2=int(input("enter 2nd number "))

sign=input("enter the operator ")

if sign=="+":
    print(num1+num2)
elif sign=="-":
    print(num1-num2)
elif sign=="*":
    print(num1*num2)
elif sign=="/":
    print(num1/num2)
else:
    print("enter the correct operator")
