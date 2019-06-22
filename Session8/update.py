items = ['manga', 'novel', 'music']
new_item = input('New item: ')
items.append(new_item)
print(items)

#update1
i = 0
replacing_item = 'bad genius'
items[i] = replacing_item
print(items)

#update2
i = 2
replacing_item = 'gintama'
items[i] = replacing_item
print(items)

#update3
i = int(input("Enter item u want to change: "))
replacing_item = input('Enter new item: ')
items[i] = replacing_item
print(items)

