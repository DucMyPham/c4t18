items = ['pho', 'com', 'chao']
print(items)
while True:
    start = input('enter C, R, U, or D: ')
    if start == 'C':
        add = input('Enter new item: ')
        items.append(add)
        print('ur new list is:', items)
    elif start == 'R':
        if items == []:
            print('ur list has nothing')
        else:
            for i in items:
                print(i)
    elif start == 'U':
        i = int(input("Enter item u want to change: "))
        replacing_item = input('Enter new item: ')
        items[i] = replacing_item
        print(items)
    elif start == 'D':
        i = int(input("Enter item u want to delete: "))
        items.pop(i)
        print(items)