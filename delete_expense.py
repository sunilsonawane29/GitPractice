
def delete_expense():
    show_expenses()

    if not expenses:
        return

    try:
        number = int(input("Enter expense number to delete: "))

        if 1 <= number <= len(expenses):
            removed = expenses.pop(number - 1)
            print(f"Deleted expense: {removed['name']}")
        else:
            print("Invalid expense number.")

    except ValueError:
        print("Please enter a valid number.")
