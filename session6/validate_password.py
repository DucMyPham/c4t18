while True:
    password = input('Enter your password: ')
    print(password)
    if password.isalpha():
        print("Make sure your password has number in it")
    else:
        break