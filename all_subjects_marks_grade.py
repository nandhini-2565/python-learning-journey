# to print the grade of the student based on all subject marks

name = input("Enter your name: ")

sub1 = int(input("Enter your marks in English: "))

if sub1 < 35:
     print("Fail")
elif sub1 > 100 or sub1 < 0:
    print("Invalid Marks")
else:
    print("Pass")
    
sub2 = int(input("Enter your marks in Hindi: "))

if sub2 < 35:
    print("Fail")
elif sub2 > 100 or sub2 < 0:
    print("Invalid marks")
else:
    print("Pass")
    
sub3 = int(input("Enter marks in Telugu: "))

if sub3 < 35:
    print("Fail")
elif sub3 > 100 or sub3 < 0:
    print("Invalid Marks")
else:
    print("Pass")
    
sub4 = int(input("Enter your marks in Mathematics: "))

if sub4 < 35:
    print("Fail")
elif sub4 > 100 or sub4 < 0:
    print("Invalid Marks")
else:
    print("Pass")

sub5 = int(input("Enter marks in Science: "))

if sub5 < 35:
    print("Fail")
elif sub5 > 100 or sub5 < 0:
    print("Invalid Marks")
else:
    print("Pass")

sub6 = int(input("Enter marks in Social: "))

if sub6 < 35:
    print("Fail")
elif sub6 > 100 or sub6 < 0:
    print("Invalid Marks")
else:
    print("Pass")

totalmarks = sub1 + sub2 + sub3 + sub4 + sub5 + sub6
print("Total marks: ", totalmarks)

percentage = (totalmarks / 600) * 100
print("Percentage: ", percentage)

if percentage >= 75:
    print("Grade A")
elif percentage >= 60:
    print("Grade B")
elif percentage >=50:
    print("Grade C")
elif percentage >= 35:
    print("Grade D")
else: 
    print("Fail")
