# program to print the grade of the student based on the marks he/she scored in an exam
marks = int(input("Enter your marks out of 100: "))

if marks >= 90:
  print("Grade A")
elif marks >= 75:
  print("Grade B")
elif marks >= 50:
  print("Grade C")
else:
  print("Fail")
