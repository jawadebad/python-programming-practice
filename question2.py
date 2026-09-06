def Question2():
    # List of names
    names = ["Jawad", "Oliver", "Kris", "Amine", "Kai", "Logan"]
    
    # Replace 2nd name
    names[1] = "Tawanda"
    
    # Print first 3 names
    print("First Three Names Are", names[:3])
    
    # Print every second name
    print("Every second name:", names[::2])
    
    # Add two names
    names.append("Harry")
    names.append("Brian")
    
    # Remove a name chosen by the user
    name_remove = input("Enter a name to remove from the list: ")
    if name_remove in names:
        names.remove(name_remove)
        print("Updated: ", names)
    else:
        print("Name not found in the list")

    # Print final list length
    print("Final List Length: ", len(names))
    
Question2()
