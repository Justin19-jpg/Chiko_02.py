from openpyxl import Workbook

book = Workbook()
sheet = book.active
sheet.title = "Favorite People"

sheet['A1'] = "ID"
sheet['B1'] = "First Name"
sheet['C1'] = "Last Name"
sheet['D1'] = "Birth Year"
sheet['E1'] = "Age"

current_year = 2026
print("Please enter information for 3 of your favorite people.")

for J in range(1, 4):
    print("\nPerson #", J)
    
    fname = input("Enter First Name: ")
    lname = input("Enter Last Name: ")
    year_born = int(input("Enter Birth Year: "))
    
    Age = current_year - year_born
    
    person_id = J
    sheet.append([person_id, fname, lname, year_born, Age])

filename = "favorite_people.xlsx"
book.save(filename)

print("\nSuccess! The file has been saved as favorite_people.xlsx")
print("\n--- Summary of Saved Records ---")

for row in sheet.iter_rows(min_row=1, values_only=True):
    print(row[0], "-", row[1], row[2], "| Birth Year:", row[3], "| Age:", row[4])
    
