def grade_calc(maths, chemistry, physics):
    percentage = int((maths + chemistry + physics)/3)

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

    return f"Your percentage score is {percentage}%\nYou scored a grade of : {mark}"

print(grade_calc(70,80,90))