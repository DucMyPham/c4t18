while True:
    email = input("enter your email: ")
    if "@" and "." in email:
        break
    else:
        print("Make sure your email has @ and .")
while True:
    password = input("enter your password: ")
    if len(password) < 8:
        print("Make sure your password has at least 8 letters")
    elif password.isalpha():
        print("Make sure your password has number in it")
    else:
        break
