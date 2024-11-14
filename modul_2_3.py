my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

list_ind = 0

while list_ind <= len(my_list):
    if my_list[list_ind] == 0:
        list_ind += 1
        continue
    if my_list[list_ind] > 0:
        print(my_list[list_ind])
        list_ind += 1
        continue
    else:
        break