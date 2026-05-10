from openpyxl import Workbook
from datetime import datetime


workbook = Workbook()
sheet = workbook.active

sheet.title = "Favorite People"


sheet.append(["ID", "First Name", "Last Name", "Birth Year", "Age"])

#current year (2026)
current_year = datetime.now().year

#loop to ask for THREE persons info
for i in range(1, 4):

    print("Enter information for person", i)

    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    birth_year = int(input("Birth Year: "))

    #compute age
    age = current_year - birth_year

    person_id = i

    #save data to excel
    sheet.append([person_id, first_name, last_name, birth_year, age])

    print()

#save excel file
workbook.save("favorite_people.xlsx")

print("Data saved to favorite_people.xlsx")
print()

#display all records
print("Saved Records:")
print("-----------------------------")

for row in sheet.iter_rows(min_row=2, values_only=True):
    print("ID:", row[0])
    print("First Name:", row[1])
    print("Last Name:", row[2])
    print("Birth Year:", row[3])
    print("Age:", row[4])
    print("-----------------------------")