count = 0
counts = 0
with open('my_file.txt','r') as file:
    for string in file:
        string_list = string.split(' ')
        for symbol in string_list:
            count = count + int(symbol)
print(count)
count = 0
with open('my_file.txt','r') as file:
    for string in file:
        string_list = string.split(' ')
        string_list = list(map(int, string_list))
        count += max(string_list)
print(count)




    # list_1 = lines[3]
    # list_2 = lines[6]
    # list_3 = lines[9]
    # list_4 = lines[12]
    # print(list_1+list_2+list_3+list_4)

            