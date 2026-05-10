# Dreams File Manager Program

filename = "dreams.txt"

while True:
    print("\n==== DREAMS FILE MANAGER ====")
    print("1. Read inspiring messages")
    print("2. Add a new inspiring message")
    print("3. Rewrite the entire file")
    print("4. Exit")
    
    choice = input("\nEnter your choice(1-4):")
    
    if choice == "1":
        print("\n--- Inspiring Messages ---")
        file = open(filename, "r")
        print(file.read())
        file.close()

    elif choice == "2":
        new_line = input("Enter your new inspiring line: ")
        file = open(filename, "a")
        file.write(new_line + "\n")
        file.close()
        print("\nYour inspiration has been added!")
        
    elif choice == "3":
        print("Warning: This will overwrite the file.")
        conf = input("Type YES to continue: ").lower()
        
        if conf.lower() == "YES":
            new_text = input("Write your new set of inspiring messages: ")
            file = open(filename, "w")
            file.write(new_text + "\n")
            file.close()
            print("\nFile has been overwritten.")
        else:
            print("\nAction cancelled.")

    elif choice == "4":
        print("Exiting program...")

    else:
        print("Invalid option, please try again.")
      
