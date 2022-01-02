x = int(input('Height: '))
if x <= 0 and x > 9:
    x = int(input('Height: '))
else:
    for i in range (x):
        for k in range (x - 1):
            print (" ")
        for l in range (x):
            print ("#")
        print ("\n")