run = True

# Add Contacts
def add_contact(contacts, run):
    '''
    NOTE : TYPE 'END' IN THE NAME FIELD TO EXIT.
    '''
    while run:
        name = input('Enter the name : ')
        if name.lower() == 'end':
            break  # Exit the loop directly

        while True: #loop to ensure number is 10 digit long.
            number = input(f'Enter {name.title()} mobile no. : ')
            try:
                number = int(number)
                if len(str(number)) >= 10:
                    break #exit loop if number is int and 10 digit long
                
            except ValueError:
                print("Invalid number. Please enter a valid integer.")
                continue
               
            if len(str(number)) < 10:
                print('Number should be 10 Digit long.')
            
        
        contacts[name.lower()] = number 
    print('')
    for names, numbers in contacts.items():
        print(f'{names.title()} : {numbers}')
    print('\nContacts are successfully added.')
    
# Search a Contact
def search_contact(contacts):
    '''\nJust type the name which you want to search.'''
    if len(contacts) == 0:  # Check if dictionary is empty
        print('\nYou have no contacts currently.')
        return  #exit function if no contacts
    
    name = input('Enter the name of contact : ').lower()
    if name in contacts:
        print(f'\nName : {name.title()} \nNo. : {contacts[name]}')
    else:
        print(f'{name} not found. Please enter correct name')
        return  #recursive call removed, replaced by loop in main

# Delete a contact  
def del_contact(contacts):
    '''\nJust type the name which you want to delete.'''
    if len(contacts) == 0:
        print('\nYou have no contacts currently.')
        return
    
    name = input('Enter the name of contact : ').lower()
    if name in contacts:
        del contacts[name]
        print(f'\n{name} is successfully deleted from your contacts.')
    else:
        print(f"{name} not found. Please enter correct name.")
        return

# Show Contacts
def show_con(contacts):
    if not contacts:
        print('\nYou have no contacts currently.')
        return

    print(f'\nYou have {len(contacts)} contacts.')
    serial = 1
    for name, number in contacts.items():
        print(f"{serial}) {name.title()} : {number}") 
        serial+=1

# Change a Contact name
def rename(contacts):
    if len(contacts) == 0:
        print('\nYou have no contacts currently.')
        return
    old_name = input('\nEnter exist name : ').lower()
    if old_name in contacts:
        new_name = input('Enter new name : ').lower()
        contacts[new_name] = contacts.pop(old_name)
        print(f'\n{new_name.title()} : {contacts[new_name]}')
    else:
        print(f'Contact not exist with name {old_name}.')
        rename(contacts)
    print('\nContact successfully updated.')
    
# Change a contact number
def change_number(contacts):
    if len(contacts) == 0:
        print('\nYou have no contacts currently.')
        return
    name = input('\nEnter exist name : ').lower()
    if name in contacts:
        while True: #loop to ensure number is 10 digit long.
            new_number = input(f'Enter new number of {name.title()} : ')
            try:
                new_number = int(new_number)
                if len(str(new_number)) >= 10:
                    break #exit loop if number is int and 10 digit long
                
            except ValueError:
                print("Invalid number. Please enter a valid integer.")
                continue
               
            if len(str(new_number)) < 10:
                print('Number should be 10 Digit long.')
        contacts[name] = new_number
        print(f'\n{name.title()} : {contacts[name]}')
    else:
        print(f'Contact not exist with name {name.title()}.')
        change_number(contacts)
    print('\nContact successfully updated')
    
 # running               
def main(run):
    '''
    Type any of the below command code. 

    CODEs : COMMANDs

        1 : ADD CONTACT
        2 : SEARCH CONTACT
        3 : DELETE CONTACT
        4 : MODIFY A CONTACT (NAME)
        5 : MODIFY A CONTACT (MOBILE NO.)
        6 : SHOW ALL CONTACTS
        0 : TO QUIT
        
     Type '1' to ADD contacts. '''
    
    contacts = dict()  # Use a dictionary directly

    while run:
        try: #error handling for invalid input
            command = int(input('\nEnter the command code : '))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue #goes to next iteration of loop

        # Commands
        if command == 1:
            print(add_contact.__doc__)
            add_contact(contacts, run)
            
        elif command == 2:
            print(search_contact.__doc__)
            search_contact(contacts)
            
        elif command == 3:
            print(del_contact.__doc__)
            del_contact(contacts)
            
        elif command == 4:
            print(del_contact.__doc__)
            rename(contacts)
            
        elif command == 5:
            change_number(contacts)
            
        elif command == 6:
             show_con(contacts)
             
        elif command == 0:
             print('Have a nice day!')
             run = False
             
        else:
             print('\nERROR : CHOOSE FROM ABOVE')
    
if __name__=='__main__':
    print(main.__doc__)
    main(run) 
