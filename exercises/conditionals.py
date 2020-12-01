def grades(mark):
    if mark > 85:
        return ("Distinction")
    if 65 <  mark and mark <= 85:
        return ("Pass")
    if mark < 65:
        return ("Fail")