def add_menu_item(menu, item):
   
    if item not in menu:
        menu.append(item)
        print(f"{item} has been added to menu.")
    else:
        print(f"{item} is already on the menu.")

def remove_menu_item(menu, item):
   
    if item in menu:
        menu.remove(item)
        print(f"{item} has been removed from the menu.")
    else:
        print(f"{item} does not exist in the menu.")

def check_menu_item(menu, item):
    
    if item in menu:
        return f"{item} is available."
    else:
        return f"{item} is not available."


initial_menu = ["Pizza", "Burger", "Pasta", "Salad"]
add_item = "Tacos"
remove_item = "Salad"
check_item = "Pizza"


add_menu_item(initial_menu, add_item)
remove_menu_item(initial_menu, remove_item)
availability = check_menu_item(initial_menu, check_item)


print(f"Updated menu: {initial_menu}")
print(f"Availability: {availability}")
