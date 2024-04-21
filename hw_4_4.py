phonebook = {}

# Розбиває вхідні данні на команду та аргументи
def parse_input(user_input):
    return user_input.lower().split() 

# Додаємо контакт до словника
def add_contact(name, phone):
    phonebook[name] = phone
    return "Contact added."

# Зміна збереженного контакту 
def change_contact(name, phone):
    if name in phonebook:
        phonebook[name] = phone
        return "Contact update."
    else:
        return "Contact not found."
    
# Знаходимо номер тел за ім‘ям
def show_phone(name):
    return phonebook.get(name, "Contact not found.")

# Виводимо у консоль усі записи, якщо існують 
def show_all():
    if not phonebook:
        return "Phonebook is empty."
    else:
        return '\n'.join(f'{name}: {phone}' for name, phone in phonebook.items())

# Головна функція (управляє основним циклом обробки команд)
def main():
    print('Welcome to the assitent bot!')
    
    while True:
        user_input = input('Enter command: ')
        command, *args = parse_input(user_input)
        
        if command == 'hello':
            print('How can I help you?')
            
        elif command == 'add' and len(args) == 2:
            name, phone = args
            print(add_contact(name, phone))
            
        elif command == 'change' and len(args) == 2:
            name, phone = args
            print(change_contact(name, phone))
            
        elif command == 'phone' and len(args) == 1:
            name = args[0]
            print(show_phone(name))
            
        elif command == 'all' and not args:
            print(show_all())
            
        elif command in ['close', 'exit']:
            print('Good bye!')
            break
        
        else:
            print('Invalid command. Please try again.')
            
if __name__ == '__main__':
    main()        