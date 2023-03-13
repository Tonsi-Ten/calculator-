print('''
+ ADD
- SUBTRACT
* MULTIPLY
/ DIVIDE
''')
num1= int(input("Enter the first number"))
num2= int(input("Enter the second number"))
opr=input("Enter the oprator ... (*, _, +, /)")

if opr == "+":
    print(num1+num2)
elif opr == "-":
    print(num1-num2)    
elif opr == "*":
    print(num1*num2)    
elif opr == "/":
    print(num1/num2)    
else:
    print("invalid oprator")
     
