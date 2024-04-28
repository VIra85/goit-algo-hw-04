def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contacts(username, new_phone, contacts):
    if username in contacts:
        contacts[username] = new_phone
        return f"Phone number updated successfully for {username}."
    else:
        return f"Error: {username} does not exist in the contacts." 

def phone_user(name, contacts):
    for name in names:
        if name in contacts:
            phones = contacts[name]
            for phone in phones:
                print(f"{name}: {phone}")
        else:
            print("No user in contacts")

def show_all_contacts(contacts):
    if not contacts:
        return "No contacts available."
    else:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
        return "All contacts displayed."
  
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:  #1 Завдання
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")  #6 Завдання
        
        elif command == "add":
            print(add_contact(args, contacts))   #2 Завдання
            
        elif command == "change":
            name, new_phone = args
            print(change_contacts(name, new_phone, contacts)) #3 Завдання
         
        elif command == "phone": 
            names = args
            print(phone_user(names, contacts))   #4
                
        elif command == "all":
            print(show_all_contacts(contacts), "\t")    #5
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
