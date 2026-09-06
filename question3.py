def Question3():
    # Store 8 numbers
    nums = [1,2,3,4,5,6,7,8]
    
    # Ask user for a number
    search = int(input("Enter a number to search: "))
    
    found = False
    count = 0
    
    # Check each position
    for i in range(8):
        if nums[i] == search:
            print("Number found at position", i)
            found = True
            count += 1
    
    # If number never appeared
    if found == False:
        print("Number Not found")
    
    # Print total appearances
    print("The number appears", count, "times")

Question3()
