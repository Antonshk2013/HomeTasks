with open('media/input.txt', 'r') as file:
    listrows = file.readlines()
    text_list = []
    for row in listrows:
        text_list += reversed(row.replace('\n', '').split(' '))

with open('media/output.txt', 'w') as file2:
    for row in text_list:
        file2.write(row + '\n')
