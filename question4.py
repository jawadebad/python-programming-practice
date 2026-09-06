def Question4():
    # 7 test scores
    scores = [67, 78, 35, 50, 99, 12, 49]
    
    # Calculations
    total = sum(scores)
    highest = max(scores)
    lowest = min(scores)
    average = sum(scores) / len(scores)

    # Outputs
    print("The Total Score is: ", total)
    print("The Highest Score is: ", highest)
    print("The Lowest Score is: ", lowest)
    print("The Average is: ", average)

    # Grade classification
    if average >= 70:
        print("Distiction")
    elif average >= 60:
        print("Merit")
    elif average >= 50:
        print("Pass")
    else:
        print("Fail")

Question4()
