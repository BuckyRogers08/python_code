A =float(input("A = "))
B =float(input("B = "))

ans= input("enter operation(+,-,*,%,/):")

if ans=='+':
  print("ANS =",A+B)
elif ans=='-':
  print("ANS =",A-B)
elif ans=='*':
  print("ANS =",A*B)
elif ans=='%':
  if B==0:
   print("error")
  else:
     print("the remainder is",A%B)
elif ans=='/':
  if B==0:
    print("error")
  else:
    print("ANS =",A/B)
else:
  print("invalid operation")
