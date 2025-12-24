import csv
from datetime import datetime

FILE_NAME = "expenses.csv"

def add_expense(amount, category, note=""):
    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, note])

    print("Expense added successfully.")

def view_expenses():
    total = 0

    try:
        with open(FILE_NAME, mode="r") as file:
            reader = csv.reader(file)
            print("\nDate | Amount | Category | Note")
            print("-" * 40)

            for row in reader:
                date, amount, category, note = row
                print(f"{date} | {amount} | {category} | {note}")
                total += float(amount)

        print("\nTotal Expense:", total)

    except FileNotFoundError:
        print("No expenses found yet.")

def main():
    while True:
        print("\n--- Personal Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Enter amount: "))
            category = input("Enter category (Food, Travel, etc.): ")
            note = input("Enter note (optional): ")
            add_expense(amount, category, note)

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
