import sqlite3

# Database setup
conn = sqlite3.connect("company.db")
cur = conn.cursor()

# Create a table to hold employee data
cur.execute(
    """CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        age INTEGER,
        department TEXT,
        salary REAL
    )"""
)

conn.commit()


class Employee:
    # Static list to hold all employee instances
    all_employees = []

    def __init__(self, first_name, last_name, age, department, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.department = department
        self.salary = salary

        # Add to the shared list of all employees
        Employee.all_employees.append(self)

        # Insert into the database
        self._insert_to_db()

    def _insert_to_db(self):
        cur.execute(
            "INSERT INTO employees (first_name, last_name, age, department, salary) VALUES (?, ?, ?, ?, ?)",
            (self.first_name, self.last_name, self.age, self.department, self.salary),
        )
        conn.commit()

    def transfer(self, new_department):
        # Change the department
        self.department = new_department

        # Update the database
        cur.execute(
            "UPDATE employees SET department = ? WHERE first_name = ? AND last_name = ?",
            (new_department, self.first_name, self.last_name),
        )
        conn.commit()

    def fire(self):
        # Remove from the shared list
        Employee.all_employees.remove(self)

        # Delete from the database
        cur.execute(
            "DELETE FROM employees WHERE first_name = ? AND last_name = ?",
            (self.first_name, self.last_name),
        )
        conn.commit()

    def show(self):
        print(
            f"Name: {self.first_name} {self.last_name}, Age: {self.age}, Department: {self.department}, Salary: {self.salary}"
        )

    @staticmethod
    def list_employees():
        cur.execute("SELECT * FROM employees")
        employees = cur.fetchall()

        if not employees:
            print("No employees found.")
            return

        for employee in employees:
            print(
                f"ID: {employee[0]}, Name: {employee[1]} {employee[2]}, Age: {employee[3]}, Department: {employee[4]}, Salary: {employee[5]}"
            )


class Manager(Employee):
    def __init__(self, first_name, last_name, age, department, salary, managed_department):
        super().__init__(first_name, last_name, age, department, salary)
        self.managed_department = managed_department

    def show(self):
        print(
            f"Name: {self.first_name} {self.last_name}, Age: {self.age}, Department: {self.department}, Managed Department: {self.managed_department}, Salary: Confidential"
        )


# Command-line interface
def cli():
    while True:
        print("\n=== Employee Management Menu ===")
        print("1. Add a new Employee (enter 'add')")
        print("2. List all Employees (enter 'list')")
        print("3. Transfer an Employee (enter 'transfer')")
        print("4. Fire an Employee (enter 'fire')")
        print("5. Show Employee Information (enter 'show')")
        print("6. Add a new Manager (enter 'addm')")
        print("7. Quit (enter 'q')")

        choice = input("\nEnter your choice: ").lower()

        if choice == "q":
            print("Exiting the program.")
            break
        elif choice == "add":
            print("\nAdd a New Employee")
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            age = int(input("Age: "))
            department = input("Department: ")
            salary = float(input("Salary: "))
            Employee(first_name, last_name, age, department, salary)
            print("Employee added successfully!")
        elif choice == "list":
            print("\nList of All Employees")
            Employee.list_employees()
        elif choice == "transfer":
            print("\nTransfer an Employee")
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            new_department = input("New Department: ")
            found = False
            for emp in Employee.all_employees:
                if emp.first_name == first_name and emp.last_name == last_name:
                    emp.transfer(new_department)
                    found = True
                    print(f"Employee {first_name} {last_name} transferred to {new_department}.")
                    break
            if not found:
                print("Employee not found.")
        elif choice == "fire":
            print("\nFire an Employee")
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            found = False
            for emp in Employee.all_employees:
                if emp.first_name == first_name and last_name == emp.last_name:
                    emp.fire()
                    found = True
                    print(f"Employee {first_name} {last_name} fired.")
                    break
            if not found:
                print("Employee not found.")
        elif choice == "show":
            print("\nShow Employee Information")
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            found = False
            for emp in Employee.all_employees:
                if emp.first_name == first_name and emp.last_name == last_name:
                    emp.show()
                    found = True
                    break
            if not found:
                print("Employee not found.")
        elif choice == "addm":
            print("\nAdd a New Manager")
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            age = int(input("Age: "))
            department = input("Department: ")
            salary = float(input("Salary: "))
            managed_department = input("Managed Department: ")
            Manager(first_name, last_name, age, department, salary, managed_department)
            print("Manager added successfully!")
        else:
            print("Invalid choice. Please try again.")


# Run the CLI
cli()
