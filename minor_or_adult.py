# Program to check whether the user is an adult or minor
name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 18:
  print(name, "is an adult")
elif age < 18 and age > 0:
  print(name, "is a minor")
else:
  print("Invalid age")
