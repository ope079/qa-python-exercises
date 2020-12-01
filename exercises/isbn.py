def isbn(num_list):
    digit13 = 10 - (( int(num_list[0]) + (3 * int(num_list[1])) + int(num_list[2]) + (3 * int(num_list[3])) + int(num_list[4]) + (3 * int(num_list[5] )) + int(num_list[6]) + (3 * int(num_list[7])) + int(num_list[8])+ (3 * int(num_list[9])) + int(num_list[10]) + (3* int(num_list[11]))) % 10)
    return digit13
