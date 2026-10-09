expenses = []


def add_expense():
    name = input("Enter expense name: ")
    amount = input("Enter amount: ")

    expense = {
        "name": name,
        "amount": amount
    }

    expenses.append(expense)
    print("Expense added successfully!")


def view_expenses():
    print("\n===== EXPENSES =====")

    total = 0

    for expense in expenses:
        print(f"{expense['name']} - ₹{expense['amount']}")
        total = total + expense["name"]

    print(f"Total Expenses: ₹{total}")


def delete_expense():
    view_expenses()

    number = int(input("Enter expense number to delete: "))

    expenses.pop(number)

    print("Expense deleted successfully!")


def table_5_to_15():
    tables = {}
    for i in range(5, 16):
        print(f"Table of {i}")
        tables[i] = []
        for j in range(1, 11):
            print(f"{i} * {j} = {i * j}")
            tables[i].append(i * j)
    return tables


print_tables = table_5_to_15
table_of_5_to_15 = table_5_to_15


def main():
    table_5_to_15()
    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            delete_expense()

        elif choice == "5":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
