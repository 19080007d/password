password = "wang zilai"
i = 3
while i > 0:
    i-=1
    PIN=input("enter your answer :")
    if PIN==password:
        print("welcome back", password)
        break
    else:
        print("pin is wrong")
        if i==0:
            print("you have no guesses!")
        else:
            print("you have",i, 'times')