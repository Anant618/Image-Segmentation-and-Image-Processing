import os
import json

class Employee:
    def __init__(self, emp_id, name, age, department):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.department = department

    def to_dict(self):
        return {"emp_id": self.emp_id, "name": self.name, "age": self.age, "department": self.department}


class EmployeeManagementSystem:
    def __init__(self, data_file="employees.json"):
        self.data_file = data_file
        self.employees = self.load_data()

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    return []
        return []

    def save_data(self):
        with open(self.data_file, "w") as file:
            json.dump(self.employees, file, indent=4)

    def add_employee(self, emp_id, name, age, department):
        if any(emp["emp_id"] == emp_id for emp in self.employees):
            print(f"Employee ID {emp_id} already exists!")
            return
        new_employee = Employee(emp_id, name, age, department)
        self.employees.append(new_employee.to_dict())
        self.save_data()
        print(f"Employee {name} added successfully!")

    def list_employees(self):
        if not self.employees:
            print("No employees found.")
            return
        print("\nEmployee List:")
        print("ID | Name | Age | Department")
        print("-" * 30)
        for emp in self.employees:
            print(f"{emp['emp_id']} | {emp['name']} | {emp['age']} | {emp['department']}")

    def remove_employee(self, emp_id):
        if not any(emp["emp_id"] == emp_id for emp in self.employees):
            print(f"No employee found with ID {emp_id}!")
            return
        self.employees = [emp for emp in self.employees if emp["emp_id"] != emp_id]
        self.save_data()
        print(f"Employee with ID {emp_id} removed successfully!")

if __name__ == "__main__":
    system = EmployeeManagementSystem()
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. List Employees")
        print("3. Remove Employee")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            department = input("Enter Department: ")
            system.add_employee(emp_id, name, age, department)
        elif choice == "2":
            system.list_employees()
        elif choice == "3":
            emp_id = input("Enter Employee ID to remove: ")
            system.remove_employee(emp_id)
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
