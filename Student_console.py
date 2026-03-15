students_console = []

def add_student():
    id = input("Enter Student ID:")
    name = input("Enter Student Name:")
    age =int(input("Enter Age:"))
    group = input("Enter Group:")
    marks = int(input("Enter Marks:"))
    

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
def update_marks():
    student_id = input("Enter Student ID to update marks: ")
    
    for s in students_console:
        if s["ID"] == student_id:
            new_marks = input("Enter new marks: ")
            s["Marks"] = new_marks
            print("Marks updated successfully")
            return

    print("Student not found")
def menu():
    while True:
        print("\n--- Student Managment System---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Marks")
        print("4. Exit")

        choice = input("Enter the Choice:")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_marks()
        elif choice == "4":
            print("Program closed")
            break
        else:
            print("Invalid choice")
menu()
