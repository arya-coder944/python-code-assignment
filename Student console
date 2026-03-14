students_console = []

def add_student():
    id = input("Enter Student ID:")
    name = input("Enter Student Name:")
    age = input("Enter Age:")
    group = input("Enter Group:")
    marks = input("Enter Marks:")
    

    student = {
        "ID": id,
        "Name": name,
        "Age": age,
        "Group": group,
        "Marks": marks


    }
        
    students_console.append(student)
    print("Student added Successfully")

def view_students():
    if not students_console:
        print("No Student found")
        return
    print("\nStudent Records")
    for s in students_console:
        print(f"ID: {s['ID']} | Name: {s['Name']} | Age: {s['Age']} | Group: {s['Group']} | Marks: {s['Marks']}")
def menu():
    while True:
        print("\n--- Student Managment System---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")

        choice = input("Enter the Choice:")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            print("Program closed")
            break
        else:
            print("Invalid choice")
menu()
