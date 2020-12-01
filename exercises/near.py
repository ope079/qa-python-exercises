def near(string1, string2):
    answer = False
    count = 0
    string3 = string1.copy()
    while count < len(string3):
        del string3[count]
        if  string3 == string2:
            answer = True
        count += 1
        string3 = string1.copy()
    return answer
