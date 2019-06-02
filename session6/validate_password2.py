while True:
    password = input('Enter your password: ')
    print(password)
    if len(password) < 8:
        print("Make sure your password has at least 8 letters")
    elif password.isalpha():
        print("Make sure your password has number in it")
    else:
        break