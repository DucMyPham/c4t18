import random
num = random.randint(0,100)
print(num)
if num<30:
    print("rainy")
elif num>=30 and num<60:
    print("cloudy")
elif num>60:
    print("sunny")

