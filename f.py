a=int(input("Enter the number A: "))
b=int(input("Enter the number B: "))
op=input("Enter the operator[+,-,*,/,%]=")
result=0
if(op=='+'):
    result=(a+b)
elif(op=='-'):
    result=(a-b)
elif(op=='*'):
    result=(a*b)
elif(op=='/'):
    result=(a/b)
elif(op=='%'):
    result=(a%b)
else:
    print("Invalid value")
print(a,op,b,"=",result)

