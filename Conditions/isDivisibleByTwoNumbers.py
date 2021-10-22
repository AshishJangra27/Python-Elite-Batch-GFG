try:    

    a=int(input("enter a number"))
    
    if a%5==0 and a%7==0:
        print("number is divisible by 5 and 7")
    else:
        print("number is not divisible by 5 and 7")

except:
    print("enter a valid number")
