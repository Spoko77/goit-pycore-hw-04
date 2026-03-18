def parse_input(user_input: str):
    """Split user input into a command and its arguments."""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args: list[str], contacts: dict[str, str]) -> str:
    """Add a new contact to the contacts dictionary."""
    if len(args) != 2:
        return "Please provide a name and phone number."

    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args: list[str], contacts: dict[str, str]) -> str:
    """Update an existing contact's phone number."""
    if len(args) != 2:
        return "Please provide a name and new phone number."

    name, phone = args
    if name not in contacts:
        return "Contact not found."

    contacts[name] = phone
    return "Contact updated."


def show_phone(args: list[str], contacts: dict[str, str]) -> str:
    """Return the phone number for the requested contact."""
    if len(args) != 1:
        return "Please provide a contact name."

    name = args[0]
    if name not in contacts:
        return "Contact not found."

    return contacts[name]


def show_all(contacts: dict[str, str]) -> str:
    """Return all saved contacts as a formatted string."""
    if not contacts:
        return "No contacts saved."

    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def main() -> None:
    """Run the assistant bot command loop."""
    contacts: dict[str, str] = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ("close", "exit"):
            print("Good bye!")
            break
        if command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
