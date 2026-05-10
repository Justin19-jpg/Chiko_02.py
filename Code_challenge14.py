Code challenge 14
x = []
y = True

while y == True:
    name = input("Enter anime title (type 'exit' to Stop)-->").lower()
    if name == "exit":
        print("\nYour list of anime:")
        break

    x.append(name)
    print(f"{name} has been added to your anime list.")

for i in x:
    print(f"- {i}")
