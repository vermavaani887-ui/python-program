# Contact Book Program

contacts = {}

while True:
    print("\n===== Contact Book =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        contacts[name] = phone
        print("Contact added successfully!")

    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts found.")
        else:
            print("\n----- Contact List -----")
            for name, phone in contacts.items():
                print(f"Name : {name}")
                print(f"Phone: {phone}")
                print("-" * 20)

    elif choice == "3":
        name = input("Enter Name to Search: ")
        if name in contacts:
            print(f"Phone Number: {contacts[name]}")
        else:
            print("Contact not found!")

    elif choice == "4":
        name = input("Enter Name to Delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")

    elif choice == "5":
        print("Thank you for using Contact Book!")
        break

    else:
        print("Invalid choice! Please try again.")
