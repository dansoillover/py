x = int(input("Enter a number: "))  # only integer!

if x > 1:
    for i in range(2, int(math.sqrt(x)) + 1):
        if (x % i) == 0:
            print(x, "is not a prime number")
            break
    else:
        print(x, "is a prime number")
else:
    print(x, "is not a prime number")
