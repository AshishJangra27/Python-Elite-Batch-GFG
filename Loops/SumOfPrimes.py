sm = 0

for n in range(2,100):
    count = 0
    for i in range (2,n):
        if(n%i==0):
            count += 1

    if(count == 0):
        sm += n
        print(n,"Prime")

print(sm)
