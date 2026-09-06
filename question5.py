def Question5():
    # Empty list
    numbers = []

    # Ask user for 10 numbers
    for i in range(10):
        num = int(input("Enter a number: "))
        numbers.append(num)

    # Print even numbers
    print("Even numbers:")
    for n in numbers:
        if n % 2 == 0:
            print(n)

    # Print odd numbers
    print("Odd numbers:")
    for n in numbers:
        if n % 2 == 1:
            print(n)

    # Print numbers divisible by 5
    print("Numbers divisible by 5:")
    for n in numbers:
        if n % 5 == 0:
            print(n)

    # Collect numbers > 50
    greater_50 = []
    for n in numbers:
        if n > 50:
            greater_50.append(n)

    # Merge lists
    merged = numbers + greater_50

    print("Merged list:", merged)

Question5()
