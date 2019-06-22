dishes = ['com', 'pho', 'chao']
print(*dishes, sep =' | ')
new_dish = input('New dish: ')
dishes.append(new_dish)

print(*dishes, sep =' | ')

print(dishes[0].upper())

print(dishes[3].upper())

print(dishes[2].upper())