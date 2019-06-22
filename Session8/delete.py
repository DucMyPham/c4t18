items = ['sport', 'LOL', 'BTS']
new_item = input('New item: ')
items.append(new_item)
print(items)

i = 1
items.pop(i)
print(items)

item_to_delete = 'LOL'
items.remove(item_to_delete)
print(items)

i = int(input("Enter item u want to delete: "))
items.pop(i)
print(items)

item_to_delete = input('Enter item to delete: ')
items.remove(item_to_delete)
print(items)