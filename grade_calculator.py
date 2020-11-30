maths = float(input("enter maths mark:"))
chemistry = float(input("enter chemistry mark?"))
physics = float(input("enter physics mark?"))
percentage = (maths + chemistry + physics)/3

print("Your percentage score is ", percentage, "%")
mark = ""
if percentage < 40:
    mark = "You Failed"
elif percentage < 50:
    mark = "D"
elif percentage < 60:
    mark = "C"
elif percentage < 70:
    mark = "B"
else:
    mark = "A"

print("Your scored a grade of:", mark)
