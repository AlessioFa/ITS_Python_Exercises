class ContactManager:
    def __init__(self) -> None:
        self.contacts = {}

    def create_contact(self, name: str, phone_numbers: list[str]) -> str | dict[str, list[str]]:
        if name in self.contacts:
            return f"Error: the contact {name} already exist."

        self.contacts[name] = phone_numbers
        return {name: self.contacts[name]}

    def add_phone_number(self, contact_name: str, phone_number: str) -> str | dict[str, list[str]]:
        if contact_name not in self.contacts:
            return f"Error: the contact '{contact_name}' doesn't exist."
        
        if phone_number in self.contacts[contact_name]:
            return f"Error: phone number '{phone_number}' already exists."
 
        self.contacts[contact_name].append(phone_number)
        return {contact_name: self.contacts[contact_name]}

    def remove_phone_number(self, contact_name: str, phone_number: str):
        if contact_name not in self.contacts:
            return f"Error: the contact {contact_name} doesn't exist."
        
        if phone_number not in self.contacts[contact_name]:
            return f"Error: phone number '{phone_number}' doesn't exist."
        
        self.contacts[contact_name].remove(phone_number)
        return {contact_name: self.contacts[contact_name]}

    def update_phone_numbers(self, contact_name: str, old_phone_number: str, new_phone_number: str) -> str| dict[str, list[str]]:
        if contact_name not in self.contacts:
            return f"Error: the contact {contact_name} doesn't exist."
        
        if old_phone_number not in self.contacts[contact_name]:
            return f"Error: the phone number '{old_phone_number}' doesn't exist."
        
        self.contacts[contact_name].remove(old_phone_number)
        self.contacts[contact_name].append(new_phone_number)

        return {contact_name: self.contacts[contact_name]}

    def list_contacts(self) -> list:

        return list(self.contacts.keys())

    def list_phone_numbers(self, contact_name: str) -> str | list[str]:
        if contact_name not in self.contacts[contact_name]:
            return f"Error: the contact '{contact_name}' doesn't exist."
        
        return self.contact[contact_name]

    def search_contact_by_phone_number(self, phone_number: str):
        contacts: list = []

        for name, numbers in self.contacts.items():
            if phone_number in numbers:
                contacts.append(name)
  
        if not contacts:
            return "No contact found with this phone number."

        return contacts


manager = ContactManager()

# 2. Provo ad aggiungere qualche contatto
print(manager.create_contact("Alice", ["123", "456"]))  
# Aspettati: {'Alice': ['123', '456']}

print(manager.create_contact("Bob", ["789"]))
# Aspettati: {'Bob': ['789']}

# 3. Provo a cercare un numero di telefono presente
print(manager.search_contact_by_phone_number("456"))
# Aspettati: ['Alice']

# 4. Provo a cercare un numero che non esiste
print(manager.search_contact_by_phone_number("000"))
# Aspettati: "Nessun contatto trovato con questo numero di telefono."