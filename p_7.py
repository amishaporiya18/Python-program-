# Menu-driven program for list operations

lst = []

while True:
    print("\n--- LIST OPERATIONS MENU ---")
    print("1. Create List")
    print("2. Display List")
    print("3. Insert Element")
    print("4. Delete Element")
    print("5. Search Element")
    print("6. Sort List")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        n = int(input("Enter number of elements: "))
        lst = []
        for i in range(n):
            element = input(f"Enter element {i+1}: ")
            lst.append(element)
        print("List created successfully.")

    elif choice == 2:
        print("List elements:", lst)

    elif choice == 3:
        element = input("Enter element to insert: ")
        pos = int(input("Enter position: "))
        lst.insert(pos, element)
        print("Element inserted.")

    elif choice == 4:
        element = input("Enter element to delete: ")
        if element in lst:
            lst.remove(element)
            print("Element deleted.")
        else:
            print("Element not found.")

    elif choice == 5:
        element = input("Enter element to search: ")
        if element in lst:
            print("Element found at index:", lst.index(element))
        else:
            print("Element not found.")

    elif choice == 6:
        lst.sort()
        print("List sorted.")

    elif choice == 7:
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Try again.")
