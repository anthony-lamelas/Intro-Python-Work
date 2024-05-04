def create_grocery_inventory():
    
    grocery_owned = ""
    
    grocery_inventory = {}
    while grocery_owned != "DONE":
        grocery_owned = input("Enter the item and quantity you own separated by a comma or DONE when complete: ")
        key = ""
        value = 0
        for char in grocery_owned:
            if char.isalpha():
                key += char
            elif char.isdigit():
                value = int(char)
        
        if key != 'DONE':
            if key not in grocery_inventory:
                grocery_inventory.update({key : value})
            else:
                grocery_inventory[key] += value
            
    return grocery_inventory
        
    
def create_grocery_shopping_list(inventory):
    grocery_want = ""
    amount_needed = {}
    grocery_needs = {}
    while grocery_want != "DONE":
        grocery_want = input("Enter the item and quantity you desire separated by a comma or DONE when complete: ")
        key = ""
        value = 0
        for char in grocery_want:
            if char.isalpha():
                key += char
            elif char.isdigit():
                value = int(char)
    
        if key != 'DONE':       
            grocery_needs.update({key : value})
    
    keys_list = [key for key in inventory.keys()]
    for i in keys_list:
        if inventory[i] < grocery_needs[i]:
            amount_needed.update({i : grocery_needs[i] - inventory[i]})
        else:
            amount_needed.update({i : 0})
    return amount_needed
    
    
def main():
    fridge_inventory = create_grocery_inventory()
    print()
    grocery_list = create_grocery_shopping_list(fridge_inventory)
    print()
    print("Your shopping list, based off of what you have in your fridge, should be:")
    print(grocery_list)
    
main()