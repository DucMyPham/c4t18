n = int(input("Enter a month: "))
if n in [1,3,5,7,8,10,12]:
    print("31 days")
elif n in [2]:
    print("28 or 29 days")
elif n in [4,6,9,11]:
    print("30 days")