
# ==========================================
# STUDENT EXPENSE TRACKER
# Bennett University
# Computational Thinking and Programming
# ==========================================

# Expense storage
expenses = []

# Available categories
categories = [
    "Food",
    "Travel",
    "Education",
    "Entertainment",
    "Shopping",
    "Other"
]


# ==========================================
# PRIYANSHU: INPUT VALIDATION
# ==========================================

def get_amount():
    try:
        amount = float(input("Enter expense amount: "))

        if amount <= 0:
            print("Amount must be greater than zero!")
            return None

        return amount

    except ValueError:
        print("Invalid input! Please enter a number.")
        return None


def get_choice():
    choice = input("Enter your choice: ")

    if choice not in ["1", "2", "3", "4", "5"]:
        print("Invalid menu choice!")
        return None

    return choice


# ==========================================
# GANESH: ADD EXPENSE
# ==========================================

def add_expense():
    print("\nSelect Expense Category:")

    for i, category in enumerate(categories, 1):
        print(i, category)

    try:
        choice = int(input("Enter category number: "))

        if choice < 1 or choice > len(categories):
            print("Invalid category!")
            return

    except ValueError:
        print("Please enter a valid category number!")
        return

    amount = get_amount()

    if amount is not None:
        expense = {
            "category": categories[choice - 1],
            "amount": amount
        }

        expenses.append(expense)
        print("Expense added successfully!")


# ==========================================
# GANESH: VIEW EXPENSES
# ==========================================

def view_expenses():
    if len(expenses) == 0:
        print("No expenses recorded.")
        return

    print("\n========== ALL EXPENSES ==========")

    for i, expense in enumerate(expenses, 1):
        print(
            i,
            expense["category"],
            "- Rs.",
            expense["amount"]
        )


# ==========================================
# SAI: CALCULATE TOTAL EXPENSE
# ==========================================

def calculate_total():
    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    print("\nTotal Expense: Rs.", total)


# ==========================================
# SAI: CATEGORY-WISE SUMMARY
# ==========================================

def category_summary():
    summary = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in summary:
            summary[category] = summary[category] + amount
        else:
            summary[category] = amount

    if len(summary) == 0:
        print("No expenses recorded.")
        return

    print("\n====== CATEGORY-WISE SUMMARY ======")

    for category, amount in summary.items():
        print(category, ": Rs.", amount)


# ==========================================
# JAIVARDHAN: MAIN MENU AND INTEGRATION
# ==========================================

def main():
    while True:
        print("\n================================")
        print("      STUDENT EXPENSE TRACKER")
        print("================================")

        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total Expense")
        print("4. Category-wise Summary")
        print("5. Exit")

        choice = get_choice()

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            calculate_total()

        elif choice == "4":
            category_summary()

        elif choice == "5":
            print("\nThank you for using Student Expense Tracker!")
            print("Program ended successfully.")
            break


# ==========================================
# PROGRAM STARTING POINT
# ==========================================

if __name__ == "__main__":
    main()
