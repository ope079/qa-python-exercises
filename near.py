string1 = list(input("input your string1: "))
string2 = list(input("input your string2: "))
looper = []


def near(string1, string2):
    answer = False
    count = 0
    string3 = string1.copy()
    print(string3)
    while count < len(string3):
        del string3[count]
        print(string3)
        if  string3 == string2:
            answer = True
        count += 1
        string3 = string1.copy()
    return answer

print(near(string1, string2))