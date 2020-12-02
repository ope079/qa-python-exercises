with open("teams.txt") as f:
    lines = f.readlines()

lines[0] = "This is a new line. \n"

with open("teams.txt", "w") as f:
    f.writelines(lines)

file = open("teams.txt", "r")
print(file.readlines())