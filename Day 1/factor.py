num = int(input("Enter the number: "))

if num > 1:
    print("Factors for the number:-")
    for i in range(2, num):
        if (num % i) == 0:
            print(i)
else:
    print("Invalid")