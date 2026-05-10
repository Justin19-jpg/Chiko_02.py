Solina_menu.py
"""
DALUBHASAAN NG LUNGSOD NG LUCENA (formerly City College of Lucena)
ITCS102: FUNDAMENTALS OF COMPUTER PROGRAMMING

Finals Project: Interactive Python Fundamentals Menu Program
Author: Ken Gimelson Bernal Solo

Instructions:
- Start the program and navigate using number keys.
- Select topics to view examples and explanations.
- Try your own Python code in 'Run Your Own Program'.
- Return to main menu from submenus anytime.
"""

def clear_screen():
    print("\n" * 60)

def wait():
    input("\nPress ENTER to continue...")

def print_statements_menu():
    clear_screen()
    print("=== PRINT STATEMENTS ===")
    print("1. Basic print")
    print("2. Using end and sep")
    print("3. Return to Main Menu")
    choice = input("Choose option: ")
    if choice == "1":
        print("\nCode: print('Hello, world!')\nOutput:")
        print('Hello, world!')
        print("\nExplanation: The print() function displays output to the console.")
    elif choice == "2":
        print("\nCode: print('A', 'B', 'C', sep='-', end='!')\nOutput:")
        print('A', 'B', 'C', sep='-', end='!')
        print("\nExplanation: sep specifies separator, end changes what appears at end of line.")
    wait()

def variables_menu():
    clear_screen()
    print("=== VARIABLES ===")
    print("1. Assigning values")
    print("2. Changing values")
    print("3. Multiple assignment")
    print("4. Return to Main Menu")
    choice = input("Choose option: ")
    if choice == "1":
        print("\nCode: x = 10\nprint(x)\nOutput:")
        x = 10
        print(x)
        print("\nExplanation: Variables store data. Use = to assign.")
    elif choice == "2":
        print("\nCode: a = 5\na = a + 3\nprint(a)\nOutput:")
        a = 5
        a = a + 3
        print(a)
        print("\nExplanation: Variables can be updated; here, a becomes 8.")
    elif choice == "3":
        print("\nCode: a, b = 1, 2\nprint(a, b)\nOutput:")
        a, b = 1, 2
        print(a, b)
        print("\nExplanation: Multiple variables can be assigned at once.")
    wait()

def operators_menu():
    clear_screen()
    print("=== OPERATORS ===")
    print("1. Arithmetic (+ - * /)")
    print("2. Comparison (== != < >)")
    print("3. Logical (and, or, not)")
    print("4. Return to Main Menu")
    choice = input("Choose option: ")
    if choice == "1":
        print("\nCode: print(5+2, 5-2, 5*2, 5/2)\nOutput:")
        print(5+2, 5-2, 5*2, 5/2)
        print("\nExplanation: + adds, - subtracts, * multiplies, / divides.")
    elif choice == "2":
        print("\nCode: print(5 == 2, 5 != 2, 5 > 2, 5 < 2)\nOutput:")
        print(5 == 2, 5 != 2, 5 > 2, 5 < 2)
        print("\nExplanation: Comparison operators return True/False.")
    elif choice == "3":
        print("\nCode: print(True and False, True or False, not True)\nOutput:")
        print(True and False, True or False, not True)
        print("\nExplanation: Logical operators combine boolean values.")
    wait()

def conditionals_menu():
    clear_screen()
    print("=== CONDITIONALS (if/else) ===")
    print("1. Simple if")
    print("2. if-else")
    print("3. if-elif-else")
    print("4. Return to Main Menu")
    choice = input("Choose option: ")
    if choice == "1":
        print("\nCode: age = 18\nif age >= 18:\n    print('Adult')\nOutput:")
        age = 18
        if age >= 18:
            print('Adult')
        print("\nExplanation: if runs code only if the condition is true.")
    elif choice == "2":
        print("\nCode: num = 3\nif num % 2 == 0:\n    print('Even')\nelse:\n    print('Odd')\nOutput:")
        num = 3
        if num % 2 == 0:
            print('Even')
        else:
            print('Odd')
        print("\nExplanation: Use else for code if the condition is false.")
    elif choice == "3":
        print("\nCode: x = 0\nif x > 0:\n    print('Positive')\nelif x < 0:\n    print('Negative')\nelse:\n    print('Zero')\nOutput:")
        x = 0
        if x > 0:
            print("Positive")
        elif x < 0:
            print("Negative")
        else:
            print("Zero")
        print("\nExplanation: elif allows multiple conditions.")
    wait()

def loops_menu():
    clear_screen()
    print("=== LOOPS ===")
    print("1. for loop: counting 1 to 5")
    print("2. while loop: counting down from 3")
    print("3. Return to Main Menu")
    choice = input("Choose option: ")
    if choice == "1":
        print("\nCode: for i in range(1,6): print(i)\nOutput:")
        for i in range(1,6):
            print(i, end=' ')
        print("\nExplanation: for loop repeats code for each value in range.")
    elif choice == "2":
        print("\nCode: count = 3\nwhile count > 0:\n    print(count)\n    count -= 1\nOutput:")
        count = 3
        while count > 0:
            print(count, end=' ')
            count -= 1
        print("\nExplanation: while loop repeats as long as condition is true.")
    wait()

def lists_menu():
    clear_screen()
    print("=== LISTS ===")
    print("1. Create and access list")
    print("2. List methods: append, remove")
    print("3. Iterating over a list")
    print("4. Return to Main Menu")
    choice = input("Choose option: ")
    if choice == "1":
        print("\nCode: fruits = ['apple','banana','cherry']\nprint(fruits[1])\nOutput:")
        fruits = ['apple','banana','cherry']
        print(fruits[1])
        print("\nExplanation: lists store multiple values; indexing starts at 0.")
    elif choice == "2":
        print("\nCode: nums = [1,2,3]\nnums.append(4)\nnums.remove(2)\nprint(nums)\nOutput:")
        nums = [1,2,3]
        nums.append(4)
        nums.remove(2)
        print(nums)
        print("\nExplanation: append adds, remove deletes specified value.")
    elif choice == "3":
        print("\nCode: for x in [7,8,9]: print(x)\nOutput:")
        for x in [7,8,9]:
            print(x, end=' ')
        print("\nExplanation: for loop can be used to process list items.")
    wait()

def functions_menu():
    clear_screen()
    print("=== FUNCTIONS ===")
    print("1. Defining and using a function")
    print("2. Function with arguments")
    print("3. Return to Main Menu")
    choice = input("Choose option: ")
    if choice == "1":
        print("\nCode:\ndef greet():\n    print('Hello!')\ngreet()\nOutput:")
        def greet():
            print('Hello!')
        greet()
        print("\nExplanation: Functions organize code into reusable blocks.")
    elif choice == "2":
        print("\nCode:\ndef add(a, b):\n    return a + b\nprint(add(3,4))\nOutput:")
        def add(a,b):
            return a + b
        print(add(3,4))
        print("\nExplanation: Functions can receive inputs (arguments) and return values.")
    wait()

def run_user_code():
    clear_screen()
    print("--- RUN YOUR OWN PYTHON PROGRAM ---")
    print("Type your Python code below. When finished, enter a single line with 'END' (without quotes) to execute it.")
    lines = []
    while True:
        line = input()
        if line.strip() == "END":
            break
        lines.append(line)
    code = "\n".join(lines)
    clear_screen()
    print("Program Output:\n")
    try:
        exec(code, {})
    except Exception as e:
        print(f"Error in your code: {e}")
    wait()

def main_menu():
    while True:
        clear_screen()
        print("====== PYTHON FUNDAMENTALS INTERACTIVE MENU ======")
        print("Dalubhasaan ng Lungsod ng Lucena".center(48))
        print("ITCS102 - Fundamentals of Computer Programming\n")
        print("1. Print Statements")
        print("2. Variables")
        print("3. Operators")
        print("4. Conditionals (if, else, elif)")
        print("5. Loops (for, while)")
        print("6. Lists")
        print("7. Functions")
        print("8. Run Your Own Python Program")
        print("9. Exit")
        choice = input("Select topic number: ")
        if choice == "1":
            print_statements_menu()
        elif choice == "2":
            variables_menu()
        elif choice == "3":
            operators_menu()
        elif choice == "4":
            conditionals_menu()
        elif choice == "5":
            loops_menu()
        elif choice == "6":
            lists_menu()
        elif choice == "7":
            functions_menu()
        elif choice == "8":
            run_user_code()
        elif choice == "9":
            print("\nThank you for using the program!\n")
            break
        else:
            print("Invalid choice! Please select a number from 1-9.")
            wait()

if __name__ == "__main__":
    main_menu()
