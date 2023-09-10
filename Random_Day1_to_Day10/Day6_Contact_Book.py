# 100 Days of Code Challenge

## Day 6: Contact Management System Challenge

### Challenge Description
"""
Design a Python class named 'ContactBook' to implement a contact management
system that allows users to perform various operations on contacts, such as adding, updating, removing, displaying, and searching.

Functionality:

1. The 'add_contact' method should allow users to add a new contact with the provided name and a list of phone numbers.
   If the contact name already exists, the method should replace the existing phone numbers.

2. The 'remove_contact' method should allow users to remove an existing contact by providing the contact name.
   If the contact does not exist, the method should not perform any action.

3. The 'update_contact' method should allow users to update an existing contact's name and/or phone numbers.
   If only the name or phone numbers are provided, the method should update the respective fields.

4. The 'display_contacts' method should display all contacts in the contact book, along with their associated phone numbers.

5. The 'search_contact' method should search for contacts using a keyword (name or phone number).
   It should display all matching contacts along with their details.
"""
### Solution Code

class ContactBook:
    def __init__(self):
        # Initialize an empty dictionary to store contacts
        self.contacts = dict()

    def add_contact(self, contact_name, phone_numbers):
        # Add a new contact to the dictionary
        self.contacts[contact_name] = phone_numbers
        print(f"Added '{contact_name}' contact with phone numbers: {phone_numbers}\n")

    def remove_contact(self, contact_name):
        if contact_name in self.contacts:
            # Remove the contact if it exists
            del self.contacts[contact_name]
            print(f"Removed '{contact_name}' contact from the Contact book\n")
        else:
            print("No such contact in Contact book\n")

    def update_contact(self, contact_name, new_name=None, phone_numbers=None):
        # Check if the contact to be updated exists
        if self.contacts.get(contact_name) is None:
            return f"Contact '{contact_name}' is not found."

        # If new_name is not provided, keep the existing name
        if new_name is None:
            new_name = contact_name

        # If phone_numbers are not provided, keep the existing phone numbers
        if phone_numbers is None:
            phone_numbers = self.contacts.get(contact_name)

        # If the new name is different from the old one, update the dictionary
        if contact_name != new_name:
            del self.contacts[contact_name]  # Delete old name entry
            print(f"Name updated: '{contact_name}' -> '{new_name}'")
        if (phone_numbers != self.contacts.get(contact_name)) or (phone_numbers != self.contacts.get(new_name)):
            self.contacts[new_name] = phone_numbers  # Add updated contact information
            print(f"Phone numbers updated for '{new_name}': {phone_numbers}")
        else:
            print("No changes made to the contact information.")
        print()

    def display_contacts(self):
        if not self.contacts:
            print("Phonebook is Empty\n")
        else:
            print("\nContacts:")
            # Iterate through contacts and print their names and phone numbers
            for contact, phone_numbers in self.contacts.items():
                contact_details = f"{contact}: {', '.join(phone_numbers)}"
                print(contact_details)
            print()

    def search_contact(self, search_word):
        if not search_word:
            print("Empty Search word")
            return ""

        matching_contacts = []
        # Iterate through contacts to find matches based on name or phone numbers
        for contact_name, phone_numbers in self.contacts.items():
            if search_word in contact_name or any(search_word in number for number in phone_numbers):
                matching_contacts.append(contact_name)

        if matching_contacts:
            print(f"Search results for keyword '{search_word}':")
            print("Contact Details:")
            # Print details of matching contacts
            for contact_name in matching_contacts:
                contact_details = f"{contact_name}: {', '.join(self.contacts[contact_name])}"
                print(contact_details)
        else:
            print(f"No results found for the search word '{search_word}'.")


# Creating a ContactBook instance
contact_book = ContactBook()

# Adding contacts to the contact_book
contact_book.add_contact("Python_Developer", ['9900000011', '6633000011'])
contact_book.add_contact("Java_Developer", ['5544009900'])
contact_book.add_contact("C_Developer", ['8811112233'])
contact_book.add_contact("Ruby_Developer", ['9778899440', '8901111233'])

# Displaying all the contacts
contact_book.display_contacts()

# Updating a contact
contact_book.update_contact("Java_Developer", new_name="Java_Fullstack_Developer", phone_numbers=['7899009900', '833330000'])

# Deleting a contact
contact_book.remove_contact("C_Developer")

# Adding a contact
contact_book.add_contact("WEB_Developer", ["9998887777"])

# Displaying all the contacts again
contact_book.display_contacts()

# Searching for a contact with name/number
contact_book.search_contact("7")


"""
Connect with me on 
[LinkedIn](https://www.linkedin.com/in/manikanta-nallam/) 
for more coding challenges, updates on my 100 days of code journey.

Stay tuned for tomorrow's coding challenge. Happy coding!
"""