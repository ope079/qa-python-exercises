def front_times(str, n):
    result = ""
    list_str = list(str)
    con_list_str = list_str[0:3]
    
    if len(str) < 3:
        short = str
    else:
        short = "".join(con_list_str)


    for i in range(n):
        result += short
    return result


print(front_times('Ch', 4))