def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def all_contact(args, contacts):
    for name in contacts:
        print(name, " - ", contacts[name])
    return "All contacts"
    
def phone_contact(args, contacts):
    name = args[0]
    print(name, " - ", contacts[name])
    return "Phone"

def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact change."

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    print(contacts)
    return "Contact added."

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))  
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(phone_contact(args, contacts))
        elif command == "all":
            print(all_contact(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()