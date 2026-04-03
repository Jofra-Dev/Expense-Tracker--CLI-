import functions

# Global state variable to control the navigation flow
global state
state = "menu"

def main_menu():
    global state
    
    functions.clear()
    
    print("\n┌────────────────────────────────────────┐")
    print("│         FINANCIAL MANAGEMENT           │")
    print("├────────────────────────────────────────┤")
    print("│  [1] View Dashboard                    │")
    print("│  [2] Edit Entry                        │")
    print("│  [3] Agent AI                          │")
    print("│  [4] Sort by Date/Category             │")
    print("│  [0] Exit                              │")
    print("└────────────────────────────────────────┘")
    
    choice = input(" >> Action: ")

    match(choice):
        case "1":
            functions.show_relatory()
            input("Press ENTER to continue...")
        case "2":
            state = "editor_menu" # Switches state to access the editor sub-menu
            return
        case "3":
            functions.agent_ia() # Direct call to AI function (blocking execution)
            return
        case "4":
            state = "sort_menu"
            return
        case "0":
            functions.clear()
            exit()
        case _:
            print("WRONG ACTION")

def editor_menu():
    global state
    functions.clear()
    
    print("--- CURRENT FINANCIAL RECORDS ---")
    functions.show_relatory()
    print("-" * 33)
    
    print("\nEDITOR MENU")
    print("1. Add new entry")
    print("2. Remove entry")
    print("3. Edit entry")
    print("0. Back")
    
    response = input("\nChoose an option: ")
    
    match(response):
        case "1":
            state = "editor_add"
            return
        case "2":
            state = "editor_remove"
            return
        case "3":
            state = "editor_edit"
            return
        case "0":
            state = "menu" # Returns to the main application level
            return
        case _:
            print("INVALID OPTION")
    input("\n Press Enter to continue...")
    
def editor_add():
    global state
    functions.clear()
    print("┌────────────────────────────────────────┐")
    print("│          NEW REGISTRATION              │")
    print("└────────────────────────────────────────┘")
    
    print("\n Please fill in the details below:\n")
    
    name     = input("NAME        : ")
    category = input("CATEGORY    : ")
    type_in  = input("TYPE (G/E)  : ") 
    value    = float(input("VALUE       : ")) 
    date     = input("DATE (M-D-Y): ")

    # Basic logic to standardize 'Gain' or 'Expense' labels
    launch_type = "Gain" if type_in.lower() == 'g' else "Expense"

    functions.add_launch(name, value, launch_type, category, date)
    
    functions.clear()
    print("\n Successfully added!")
    input("\n Press Enter to continue...")
    state = "editor_menu"

def editor_remove():
    functions.clear()
    global state
    
    print(f"{' CURRENT RECORDS ':-^40}")
    functions.show_relatory()
    print("-" * 40)

    print("\n┌────────────────────────────────────────┐")
    print("│          REMOVE REGISTRATION           │")
    print("└────────────────────────────────────────┘")
    
    target_id = input("\n  ➤ INFORM THE ID TO DELETE: ")
    
    functions.clear()
    print(f"\n  [!] ATTENTION: You are about to delete ID {target_id}")
    confirm = input("  ➤ ARE YOU SURE? (Y/N): ").strip().upper()

    if confirm == 'Y':
        functions.remove_launch(int(target_id))
        print("\n  ✔ Registry removed successfully!")
    else:
        print("\n  ✖ Operation canceled.")
    
    functions.clear()
    input("\n Press ENTER to continue...")
    state = "editor_menu"

def editor_edit():
    global state
    functions.clear()
    
    print(f"{' CURRENT RECORDS ':-^40}")
    functions.show_relatory()
    print("-" * 40)

    print("\n┌────────────────────────────────────────┐")
    print("│           EDIT REGISTRATION            │")
    print("└────────────────────────────────────────┘")

    target_id = input("\n  ➤ ID TO EDIT: ")
    print("\n  Enter the NEW information below:\n")

    new_name     = input("NEW NAME     : ")
    new_category = input("NEW CATEGORY : ")
    new_type_in  = input("NEW TYPE(G/E): ") 
    new_value    = float(input("NEW VALUE    : ")) 
    new_date     = input("NEW DATE     : ")

    new_launch_type = "Gain" if new_type_in.lower() == 'g' else "Expense"

    functions.clear()
    print(f"\n  [!] WARNING: Overwriting data for ID {target_id}")
    confirm = input("  ➤ CONFIRM CHANGES? (Y/N): ").strip().upper()

    if confirm == 'Y':
        functions.edit_launch(int(target_id), new_name, new_launch_type, new_value, new_category, new_date)
        print("\n  ✔ Registry updated successfully!")
    else:
        print("\n  ✖ Edit canceled.")

    functions.clear()
    input("\n Press ENTER to continue...")
    state = "editor_menu"

def sort_menu():
    global state
    functions.clear()

    print(f"{' CURRENT RECORDS ':-^40}")
    functions.show_relatory()
    print("-" * 40)

    print("\n┌────────────────────────────────────────┐")
    print("│            SORTING OPTIONS             │")
    print("└────────────────────────────────────────┘")

    print("\n  How would you like to organize the data?")
    print("  [1] By Category (A-Z)")
    print("  [2] By Date (Oldest First)")
    print("  [0] Back")

    result = input("\n  ➤ Selection: ")

    match result:
        case "1":
            functions.reorder_by_category()
            functions.clear()
            print("\n  ✔ Sorted by Category successfully!")
            input("\n  Press ENTER to view...")
        case "2":
            functions.reorder_by_date()
            functions.clear()
            print("\n  ✔ Sorted by Date successfully!")
            input("\n  Press ENTER to view...")
        case "0":
            state = "menu" 
            return
        case _:
            functions.clear()
            print("\n  INVALID OPTION")
            input("\n  Press ENTER to try again...")

# Main application loop: constantly checks the 'state' to render the correct menu
while(True):
    match state:
        case "menu":
            main_menu()
        case "editor_menu":
            editor_menu()
        case "editor_add":
            editor_add()
        case "editor_remove":
            editor_remove()
        case "editor_edit":
            editor_edit()
        case "sort_menu":
            sort_menu()