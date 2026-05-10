temp = eval(input("Input temperature--> "))

if temp == 0:
        print("Temperature is Considered Freezing Temperature")

elif temp >= 1 and temp <= 20:
        print("Temperature is Considered Extremly Cold")

elif temp >= 21 and temp <= 30:
        print("Temperature is Considered Cold")

elif temp >= 31 and temp <= 37:
        print("Temperature Considered Lukewarm")

elif temp >= 38 and temp <= 45:
        print("Temperature Considered Hot")

elif temp >= 46 and temp <= 50:
        print("Temperature Considered Boiling Hot")

elif temp >=51 or temp <= 52:
        print("Temperature is Considered Dangerous Temperature")

else:
        print("Invalid Temperature")
