while True:
    txt = input("Enter your name ")
    print(txt)
    if txt.isalpha():
        break
    else:
        print ("Please enter your name again")
        