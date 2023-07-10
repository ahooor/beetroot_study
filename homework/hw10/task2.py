# Functionality of Phonebook application:

# Add new entries 
# Search by first name 
# Search by last name 
# Search by full name
# Search by telephone number
# Search by city or state
# Delete a record for a given telephone number
# Update a record for a given telephone number
# An option to exit the program
 

# The first argument to the application should be the name of the phonebook. 
# Application should load JSON data, if it is present in the folder with application, 
# else raise an error. After the user exits, all data should be saved to loaded JSON.

import json
import os

# Function for opening file if it exists:
def read_phonebook(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return json.load(file)
    else:
        raise FileNotFoundError("Mentioned file does not exist.")
    
# Function for writing into a file:
def update_phonebook(file_path, data):
    if os.path.exists(file_path):
        with open(file_path, "w") as file:
           json.dump(data, file, indent=4)
    else:
        raise FileNotFoundError("Mentioned file does not exist.")    

# Adding new contacts:
def add_entry(contacts_list):
    fname = input("Enter first name: ")
    lname = input("Enter last name: ")
    number = input("Enter phone number: ")
    location = input("Enter location: ")

    data = read_phonebook(contacts_list)
    data.append({"fname": fname, "lname": lname, "number": number, "location": location})
        
    update_phonebook(contacts_list, data)

# Search by first name:
def search_by_fname(contacts_list):
    fname = input("Enter the first name of a contact you are looking for: ")
    
    data = read_phonebook(contacts_list)
    found = False
    for contact in data:
        if contact["fname"] == fname:
            found = True
            print(contact)
    
    if found == False:
        print("No items found.")

# Search by last name:
def search_by_lname(contacts_list):
    lname = input("Enter the last name of a contact you are looking for: ")
    
    data = read_phonebook(contacts_list)
    found = False
    for contact in data:
        if contact["lname"] == lname:
            found = True
            print(contact)

    if found == False:
        print("No items found.")

# Search by full name:
def search_by_fullname(contacts_list):
    fname = input("Enter the first name of a contact you are looking for: ")
    lname = input("Enter the last name of a contact you are looking for: ")
    
    data = read_phonebook(contacts_list)
    found = False
    for contact in data:
        if contact["fname"] == fname and contact["lname"] == lname:
            found = True
            print(contact)

    if found == False:
        print("No items found.")

# Search by phone number:
def search_by_phone(contacts_list):
    number = input("Enter the phone number of a contact you are looking for: ")
    
    data = read_phonebook(contacts_list)
    found = False
    for contact in data:
        if contact["number"] == number:
            found = True
            print(contact)

    if found == False:
        print("No items found.")

# Search by location:
def search_by_location(contacts_list):
    location = input("Enter the location of a contact you are looking for: ")
    
    data = read_phonebook(contacts_list)
    found = False
    for contact in data:
        if contact["location"] == location:
            found = True
            print(contact)

    if found == False:
        print("No items found.")

# Deleting the contact:
def delete_entry(contacts_list):
    number = input("Enter phone number of the contact you want to delete: ")
    
    data = read_phonebook(contacts_list)
    found = False
    for contact in data:
        if contact["number"] == number:
            found = True
            i = data.index(contact)
            data.pop(i)
    
    if found == True:
        update_phonebook(contacts_list, data)
    else:
        print("Nothing to delete.")

# Updating the contact:
def update_entry(contacts_list):
    number = input("Enter phone number of the contact you want to edit: ")
    data = read_phonebook(contacts_list)
    found = False
    for contact in data:
        if contact["number"] == number:
            found = True
            i = data.index(contact)
            
            fname = input("Enter first name: ")
            lname = input("Enter last name: ")
            number = input("Enter phone number: ")
            location = input("Enter location: ")
            
            data[i] = {"fname": fname, "lname": lname, "number": number, "location": location}
    
    if found == True:
        update_phonebook(contacts_list, data)
    else:
        print("Nothing to delete.")


path = "/Users/alisiyanosenko/Python/beetroot_study/hw10/contacts.json"
# add_entry(path)
# search_by_fname(path)
# search_by_lname(path)
# search_by_fullname(path)
# search_by_phone(path)
# search_by_location(path)
# update_entry(path)
# delete_entry(path)

def phonebook_ui(path):

    while True:
        print("\nWhat do you want to do?",
        "1. Add contact.",
        "2. Search by name.",
        "3. Search by surname.",
        "4. Search by full name.",
        "5. Search by phone number.", 
        "6. Search by location.",
        "7. Edit contact.",
        "8. Delete contact.",
        "Enter 'q' to quit",
        sep="\n")
        operation = input("Enter the code: ")
        if operation == "1":
            add_entry(path)
        elif operation == "2":
            search_by_fname(path)
        elif operation == "3":
            search_by_lname(path)
        elif operation == "4":
            search_by_fullname(path)
        elif operation == "5":
            search_by_phone(path)
        elif operation == "6":
            search_by_location(path)
        elif operation == "7":
            update_entry(path)
        elif operation == "8":
            delete_entry(path)
        else:
            print("You've quitted.")
            break

phonebook_ui(path)


