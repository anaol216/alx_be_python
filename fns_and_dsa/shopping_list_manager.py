shopping_list = []
def add_item(item):
    shopping_list.append(item)
    return f'Item "{item}" added to the shopping list.'
def remove_item(item):
    if item in shopping_list:
        shopping_list.remove(item)
        return f'Item "{item}" removed from the shopping list.'
    else:
        return f'Item "{item}" not found in the shopping list.'
def view_list():
    if shopping_list:
        return "Shopping List:\n" + "\n".join(f"- {item}" for item in shopping_list)
    else:
        return "The shopping list is empty."
    
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            input_item = input("Enter the item to add: ")
            pass
        elif choice == '2':
            input_item = input("Enter the item to remove: ")
            pass
        elif choice == '3':
            view_list()
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()