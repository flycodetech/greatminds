successful = False
for number in range(3):
    print("Attempt")
    if successful: 
        print("successful")
        break
else:
    print("attempted three times  and failed ")

    # #nesting loop 

    for x in range (5):
        for y in range(3):
           for z in range(5):
            print(f"{x}, {y}, {z}")
