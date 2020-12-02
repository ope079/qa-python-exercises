file = open("teams.txt", "w")

newline = "Arsenal \nMan U \nMan City \nChelsea \nLiverpool"
file.write(newline)
file.close()

file = open("teams.txt", "r")
for line in range(0,6):
    if line == 0 or line == 3:
        print(file.readline())

file.close()
