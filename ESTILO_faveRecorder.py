from openpyxl import Workbook
from datetime import datetime


workbook = Workbook()
sheet = workbook.active

sheet.title = "Favorite People"

sheet.append(["ID", "First Name", "Last Name", "Birth Year", "Age"])

cur_year = datetime.now().year
for i in range(1, 4):

    print("Enter information for person", i)

    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    birth_year = int(input("Birth Year: "))

    
    age = cur_year - birth_year

    person_id = i

    
    sheet.append([person_id, first_name, last_name, birth_year, age])

    print()


workbook.save("favorite_people.xlsx")

print("Data saved to favorite_people.xlsx")
print()


print("Saved Records:")
print("-----------------------------")

for row in sheet.iter_rows(min_row=2, values_only=True):
    print("ID:", row[0])
    print("First Name:", row[1])
    print("Last Name:", row[2])
    print("Birth Year:", row[3])
    print("Age:", row[4])
    print("-----------------------------")