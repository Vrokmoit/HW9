contacts = {}  # Словник для зберігання контактів

# Декоратор для обробки помилок введення користувача
def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError as e:
            return str(e)
        except IndexError as e:
            if "unpack" in str(e):
                return "Give me name and phone please"
            else:
                return "Invalid input"
    return wrapper

# Додавання нового контакту
@input_error
def add_contact(name, phone):
    if not name or not phone:
        raise ValueError("Give me both name and phone, separated by a space")
    
    contacts[name] = phone
    return "Contact added successfully"

# Зміна номера телефону для існуючого контакту
@input_error
def change_phone(name, phone):
    if name in contacts:
        if not phone:
            raise ValueError("Phone is missing")
        contacts[name] = phone
        return "Phone number updated"
    else:
        raise ValueError(f"Contact '{name}' not found")

# Пошук номера телефону за ім'ям
@input_error
def find_phone(name):
    if name in contacts:
        return contacts[name]
    else:
        raise ValueError(f"Contact '{name}' not found")

# Виведення всіх контактів
def show_all_contacts():
    if not contacts:
        return "No contacts found"
    else:
        result = "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
        return result

# Головна функція для обробки команд користувача
def main():
    print("How can I help you?")
    
    while True:
        command = input("Enter a command: ").lower()
        
        if command == "hello":
            print("How can I help you?")
        elif command.startswith("add "):
            _, *rest = command.split()
            if len(rest) != 2:
                print("Enter both name and phone")
                continue
            name, phone = rest
            response = add_contact(name, phone)
            print(response)
        elif command.startswith("change "):
            _, name, *phone = command.split()
            phone = " ".join(phone)
            response = change_phone(name, phone)
            print(response)
        elif command.startswith("phone "):
            _, name = command.split()
            try:
                response = find_phone(name)
                print(response)
            except Exception as e:
                print(e)
        elif command == "show all":
            result = show_all_contacts()
            print(result)
        elif command in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
