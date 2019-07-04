
x1 = int(input("Enter first number"))
x2 = int(input("Enter Secount number"))
sup = "The Answer is: "
op = input("Enter Operation")

if op =='+':
    if x1 == 56 and x2 ==9:
        print(sup, 77)
    else:
        print(sup, x1+x2)
elif op =='-':
     print(sup, x1-x2)
elif op =='*':
    if x1==45 and x2 ==3:
        print(sup, 555)
    else:
        print(sup, x1*x2)
elif op =='/':
    if x1 == 56 and x2 == 6:
        print(sup , 4)
    else:
        print(sup ,x1/x2)
else:
  print("Invalid Operator!!")



