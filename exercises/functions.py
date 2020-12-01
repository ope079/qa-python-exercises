def grades(name, homework, assessment, final_exam):
    mark = int((homework + assessment + final_exam)/1.75)
    grade = " "

    if mark < 40:
        grade = "F"
    elif mark < 50:
        grade = "E"
    elif mark < 60:
        grade = "D"
    elif mark < 70:
        grade = "C"
    elif mark < 80:
        grade = "B"
    else:
        grade = "A"
    return f"{name} scored {mark}% with Grade {grade}"

