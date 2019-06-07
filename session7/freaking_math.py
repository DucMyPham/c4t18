import random
point = 0

while True:

    num1 = random.randint(-5,5)
    num2 = random.randint(-5,5)
    result = random.randint(-10,10)
    sum = 'num1' + 'num2'
    
    print(num1,'+',num2,'=',result)
    
    answer = input("True or False: ")
    if result == sum:
        if answer == 'true':
            point +=1
            print(point)
        elif answer == 'false':
            break

    elif result != sum:
        if answer == 'false':
            point +=1
            print(point)
        elif answer == 'true':
            break
        
    
