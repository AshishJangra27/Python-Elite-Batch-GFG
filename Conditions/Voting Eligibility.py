try:
    age = int(input("Enter your age: "))
    
    if (age > -1 and age < 101):

        if (age >= 18):
            print("Eligible for voting!")
        else:
            print("Not Eligible for Voting")
    else:
        print("Invalid Age!")
        
except:
    print("You've entered invalid age")




