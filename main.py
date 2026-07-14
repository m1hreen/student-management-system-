from database import create_database, add_student, view_students       
def main():
    create_database()

    while True:
        print("\n1. Add Student")
        print("2. View Students")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            course = input("Enter Course: ")

            add_student(name, age, course)

        elif choice == "2":
            view_students()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")
            
if __name__ == "__main__":
    main()