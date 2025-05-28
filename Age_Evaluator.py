#input and validation:
name = input("enter your name:")
age = int(input("enter your age:"))

#age_calculation_function:
def get_age(age):
  if  0>age or age>130:
    return "invalid age"
  elif  0<=age<=12:
    return "Child"
  elif 12<age<=19:
    return "Teenager"
  elif 20<age<=59:
    return "Adult"
  else :
    return "senior citizen"

category = get_age(age)

#user info and output statements:
print("\n------- AGE REPORT -------")
print(f"name: {name}")
print(f"age: {age}")
print(f"age category: {category}")
