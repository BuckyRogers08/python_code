#input:
A =float(input("Enter value for A:"))
B =float(input("Enter value for B:"))

#operations input:
ans= input("Enter operation(+,-,*,%,/,//,**):")

#logic, loops and output statements:
if ans=='+':
  print("ANS =",A+B)
elif ans=='-':
  print("ANS =",A-B)
elif ans=='*':
  print("ANS =",A*B)
elif ans=='/':
  print("ANS =" if B != 0 else "Error", A / B if B != 0 else "")
elif ans=='%':
  print("The remainder is" if B!= 0 else "Error: Modulo by 0",A%B if B!=0 else"")
elif ans=='//':
   print("ANS =" if B != 0 else "Error: Floor division by zero", A // B if B != 0 else "")
elif ans=='**':
  print("ANS =",A**B)
else:
  print("invalid operation")
