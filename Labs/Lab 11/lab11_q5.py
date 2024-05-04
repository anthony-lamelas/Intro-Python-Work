def add_entry(contacts, name, number):
    if name not in contacts and len(number) == 10 and number.isdigit():
        contacts[name] = number
    else:
        print("Contact is invalid.")

    
def lookup(contacts, name):
    
    if name in contacts:
        return contacts[name]
    else:
        print("Name not found in contact list.")
    
def delete_entry(contacts, name):
    if name in contacts:
        contacts.pop(name)
    else:
        print("Name not found in contact list.")
    
def print_all(contacts):
    for name, number in contacts.items():
        print(name,"\t", number)
        
        
def main():
    contacts = {}
    option = ""
    
    while option != "Q":
        option = input("Please enter an option: ")
        
        if option == "A":
            name = input("Please enter a name: ")
            number = input("Please enter a phone number: ")
            add_entry(contacts, name, number)
            
        if option == "L":
            name = input("Please enter a name: ")
            print(lookup(contacts, name))
            
        if option == "P":
            print_all(contacts)
        
        if option == "D":
            name = input("Please enter a name: ")
            delete_entry(contacts, name)
            
main()
            
            
            
            