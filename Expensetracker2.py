import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"


# Create CSV file if it doesn't exist
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Description", "Category", "Amount"])


# Add Expense
def add_expense():
    description = input("Enter expense description: ")

    while True:
        try:
            amount = float(input("Enter amount: ₹"))
            break
        except ValueError:
            print("Please enter a valid amount.")

    category = input("Enter category (Food/Travel/Shopping/etc): ")

    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, description, category, amount])

    print("Expense added successfully!\n")


# View All Expenses
def view_expenses():
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        rows = list(reader)

        if len(rows) <= 1:
            print("No expenses found.\n")
            return

        print("\n------ All Expenses ------")
        print("{:<12} {:<20} {:<15} {:>10}".format(
            "Date", "Description", "Category", "Amount"))

        print("-" * 60)

        for row in rows[1:]:
            print("{:<12} {:<20} {:<15} ₹{:>8}".format(
                row[0], row[1], row[2], row[3]))

        print()


# View Total Spending
def total_spent():
    total = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            total += float(row["Amount"])

    print(f"\nTotal Amount Spent = ₹{total:.2f}\n")


# Search by Category
def search_category():
    category = input("Enter category to search: ").strip().lower()

    found = False

    print("\nMatching Expenses\n")

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["Category"].lower() == category:
                print(
                    f"{row['Date']} | {row['Description']} | ₹{row['Amount']}")
                found = True

    if not found:
        print("No expenses found in this category.")

    print()


# Total per Category
def total_per_category():
    totals = {}

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            category = row["Category"]
            amount = float(row["Amount"])

            totals[category] = totals.get(category, 0) + amount

    if not totals:
        print("No expenses found.\n")
        return

    print("\nTotal Spending Per Category")

    for category, total in totals.items():
        print(f"{category:<15} ₹{total:.2f}")

    print()


# Monthly Spending
def monthly_total():
    monthly = {}

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            month = row["Date"][:7]  # YYYY-MM
            amount = float(row["Amount"])

            monthly[month] = monthly.get(month, 0) + amount

    if not monthly:
        print("No expenses found.\n")
        return

    print("\nMonthly Spending")

    for month, total in monthly.items():
        print(f"{month} : ₹{total:.2f}")

    print()


# Main Menu
def menu():
    initialize_file()

    while True:
        print("========== Expense Tracker ==========")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Spent")
        print("4. Search by Category")
        print("5. Total Spent Per Category")
        print("6. View Monthly Spending")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            total_spent()

        elif choice == "4":
            search_category()

        elif choice == "5":
            total_per_category()

        elif choice == "6":
            monthly_total()

        elif choice == "7":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice! Try again.\n")


if __name__ == "__main__":
    menu()
