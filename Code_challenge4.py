print("Welcome to ManigaManga Recommender!")
print("Pick a genre:")
print("1. Action")
print("2. Comedy")
print("3. Horror")
genre = input("Select genre (action/comedy/horror):").lower()

if genre == "action":
    print("You have chosen the Action genre.")

    duration = input("Duration of manga (Short, Medium, Long):").lower()
    if duration == "short":
        print("Decade (2010/2020):")
        decade = input("Select decade: ")
        if decade == "2010":
            print("These are the available short action manga by the year 2010:")
        elif decade == "2020":
            print("These are the available short action manga by the year 2020:")
        else:
            print("Invalid. Choose from the bracket.")
    elif duration == "medium":
        print("Decade (2010/2020):")
        decade = input("Select decade: ")
        if decade == "2010":
            print("These are the available medium action manga by the year 2010:")
        elif decade == "2020":
            print("These are the available medium action manga by the year 2020:")
        else:
            print("Invalid. Choose from the bracket.")
    elif duration == "long":
        print("Decade (2010/2020):")
        decade = input("Select decade: ")
        if decade == "2010":
            print("These are the available long action manga by the year 2010:")
        elif decade == "2020":
            print("These are the available long action manga by the year 2020:")
        else:
            print("Invalid. Choose from the bracket.")
    else:
        print("Invalid duration. Choose 'Short', 'Medium', or 'Long'.")

elif genre == "comedy":
    print("You have chosen the Comedy genre.")

    duration = input("Duration of manga (Short, Medium, Long):").lower()
    if duration == "short":
        print("Decade (2010/2020):")
        decade = input("Select decade: ")
        if decade == "2010":
            print("These are the available short comedy manga by the year 2010:")
        elif decade == "2020":
            print("These are the available short comedy manga by the year 2020:")
        else:
            print("Invalid. Choose from the bracket.")
    elif duration == "medium":
        print("Decade (2010/2020):")
        decade = input("Select decade: ")
        if decade == "2010":
            print("These are the available medium comedy manga by the year 2010:")
        elif decade == "2020":
            print("These are the available medium comedy manga by the year 2020:")
        else:
            print("Invalid. Choose from the bracket.")
    elif duration == "long":
        print("Decade (2010/2020):")
        decade = input("Select decade: ")
        if decade == "2010":
            print("These are the available long comedy manga by the year 2010:")
        elif decade == "2020":
            print("These are the available long comedy manga by the year 2020:")
        else:
            print("Invalid. Choose from the bracket.")
    else:
        print("Invalid duration. Choose 'Short', 'Medium', or 'Long'.")

elif genre == "horror":
    print("You have chosen the Horror genre.")

    duration = input("Duration of manga (Short, Medium, Long):").lower()
    if duration == "short":
        print("Decade (2010/2020):")
        decade = input("Select decade: ")
        if decade == "2010":
            print("These are the available short horror manga by the year 2010:")
        elif decade == "2020":
            print("These are the available short horror manga by the year 2020:")
        else:
            print("Invalid. Choose from the bracket.")
    elif duration == "medium":
        print("Decade (2010/2020):")
        decade = input("Select decade: ")
        if decade == "2010":
            print("These are the available medium horror manga by the year 2010:")
        elif decade == "2020":
            print("These are the available medium horror manga by the year 2020:")
        else:
            print("Invalid. Choose from the bracket.")
    elif duration == "long":
        print("Decade (2010/2020):")
        decade = input("Select decade: ")
        if decade == "2010":
            print("These are the available long horror manga by the year 2010:")
        elif decade == "2020":
            print("These are the available long horror manga by the year 2020:")
        else:
            print("Invalid. Choose from the bracket.")
    else:
        print("Invalid duration. Choose 'Short', 'Medium', or 'Long'.")

else:
    print("Invalid genre. Choose 'action', 'comedy', or 'horror'.")
