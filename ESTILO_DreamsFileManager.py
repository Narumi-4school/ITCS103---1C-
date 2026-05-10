file_name = "dream_rec.txt"

while True:

    print("\n +++++DREAMS MENU +++++")
    print("1. Read inspiring messages")
    print("2. Add a new inspiring message")
    print("3. Rewrite the entire file")
    print("4. Exit")

    choice = input("Enter your choice: ")

    
    if choice == "1":

        try:
            file = open(file_name, "r")

            content = file.read()

            print("\n--- Inspiring Messages ---")

            if content == "":
                print("The file is empty.")
            else:
                print(content)

            file.close()

        except FileNotFoundError:
            print("File not found.")

    
    elif choice == "2":

        new_message = input("Enter a new inspiring message: ")

        file = open(file_name, "a")
        file.write("\n" + new_message)
        file.close()

        print("Message added successfully!")

   
    elif choice == "3":

        confirm = input("Are you sure you want to rewrite the file? (yes/no): ")

        if confirm.lower() == "yes":

            new_content = input("Enter new content for the file: ")

            file = open(file_name, "w")
            file.write(new_content)
            file.close()

            print("File has been rewritten successfully!")

        else:
            print("Rewrite cancelled.")

    
    elif choice == "4":

        print("Program ended.")
        break

    
    else:
        print("Invalid choice. Please try again.")