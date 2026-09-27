import re


FILE_NAME = "students.txt"


# Validate email using Regex
def validate_email(email):
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    if re.match(pattern, email):
        return True

    return False


# Add Student
def add_student():
    try:
        student_id = int(input("Enter Student ID: "))

        name = input("Enter Student Name: ").strip()

        if not name:
            raise ValueError("Student name cannot be empty.")

        email = input("Enter Student Email: ").strip()

        if not validate_email(email):
            raise ValueError("Invalid email format.")

        age = int(input("Enter Student Age: "))

        if age <= 0:
            raise ValueError("Age must be greater than 0.")

        # Save student data to file
        with open(FILE_NAME, "a") as file:
            file.write(f"{student_id},{name},{email},{age}\n")

        print("Student added successfully!")
        print("Student data saved to file.")

    except ValueError as e:
        print("Error:", e)

    except IOError as e:
        print("File error:", e)


# Read Student Data
def read_students():
    try:
        with open(FILE_NAME, "r") as file:
            records = file.readlines()

        if not records:
            print("No student records found.")
            return

        print("\n===== Student Records =====")

        for record in records:
            data = record.strip().split(",")

            if len(data) == 4:
                student_id, name, email, age = data

                print(f"ID    : {student_id}")
                print(f"Name  : {name}")
                print(f"Email : {email}")
                print(f"Age   : {age}")
                print("---------------------------")

    except FileNotFoundError:
        print("No student records found.")

    except IOError as e:
        print("File error:", e)


# Main Menu
def main():
    while True:
        print("\n===== Student Record Manager =====")
        print("1. Add Student")
        print("2. Read Student Data")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                add_student()

            elif choice == 2:
                read_students()

            elif choice == 3:
                print("Program exited.")
                break

            else:
                raise ValueError("Please enter a choice between 1 and 3.")

        except ValueError as e:
            print("Error:", e)


# Start program
if __name__ == "__main__":
    main()
