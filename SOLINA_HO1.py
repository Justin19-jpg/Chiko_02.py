word = input("Enter a word:")

numbers = []

for n in range(1, 7):
    num = int(input(f"Enter number {n}:"))
    numbers.append(num)

print(numbers)

word_length = len(word)
print("The length of the word is", word_length)

average = sum(numbers) / len(numbers)
print("The average of the numbers is", average)

if word_length > average:
    print(f"The length of the word '{word}' is greater than the average.")
elif word_length < average:
    print(f"The length of the word '{word}' is less than the average.")
else:
    print(f"The length of the word '{word}' is equal to the average.")
print("thank you")
    

