import account
import pickle

FIND = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUITE = 5


def main(): 
    CHOICE = 0 
    
    while CHOICE != QUITE:
        CHOICE = get_menu()

        contacts = load_contacts()

        if CHOICE == FIND: 
            find_contact(contacts)
        elif CHOICE == ADD: 
            add_contact(contacts)
        elif CHOICE == CHANGE: 
            change_contact(contacts)
        elif CHOICE == DELETE: 
            delete_contact(contacts)
    
        save_contact(contacts)

#Function to return item selection from menu
def get_menu(): 
    print('What do you want to do ?: ')
    print('Find - 1\n'+
          'Add - 2\n'+
          'Change - 3\n'+
          'Delete - 4\n'+
          'Quite - 5\n')
    choice = int(input('select item : '))
    return choice

#Find contact from loaded dictionary from def load_contacts function
def find_contact(contacts):
    name = input('write name of contact: ')
    
    if name in contacts: 
       print(contacts[name])
       print()
    else: 
        print('*[INFO] Contact not found\n')

#Add contact details, if there is a bank account, then write how much money is on the account
def add_contact(contacts):
    try: 
        name = input('\nFirst and last name: ')
        if name not in contacts: 
            phone = input('Phone number: ')
            email = input('email of contact: ')

            question = input('\ndid you enter your information correctly ?\n'+
                    'If yes then press "y" if not "n" : ')

            #create an account id using a hash function
            if question.lower() == 'y':
                person_id = get_id(name, phone)
            else: 
                add_contact()

            question_bank = input('do you have a bank account ? (y/n): ') 

            if question_bank.lower() == 'y':
                money = input('how much money do you have in your account ?: ')
                #all information is written to an object instance
                add_change = account.Bank(name, phone, email, person_id, money)
                contacts[name] = add_change

                print('*[INFO] Contact was added '+
                    'with "bank account" \n')
            else: 
                add_change = account.Contact(name, phone, email)
                contacts[name] = add_change
                print('*[INFO] Contact was added \n')
        
    #if an exception occurs, we call the function again
    except Exception as err: 
        print(err)
        add_contact()
    
#We change the contact's recorded information by finding it by name
def change_contact(contacts):
    try: 
        name = input('\nFirst and last name: ')
        if name in contacts: 
            phone = input('Phone number: ')
            email = input('email of contact: ')

            question = input('\ndid you enter your information correctly ?\n'+
                    'If yes then press "y" if not "n" : ')

            if question.lower() == 'y':
                person_id = get_id(name, phone)
            else: 
                add_contact()

            question_bank = input('do you have a bank account ?:') 

            if question_bank.lower() == 'y':
                money = input('how much money do you have in your account ?: ')

                add_change = account.Bank(name, phone, email, person_id, money)
                contacts[name] = add_change

                print('*[INFO] Contact was changed '+
                    'with "bank account" \n')
            else: 
                add_change = account.Contact(name, phone, email)
                contacts[name] = add_change
                print('*[INFO] Contact was changed \n')
        

    except Exception as err: 
        print(err)
        add_contact()

#Hash function to create an account ID
def get_id(name, phone):
    person_id = hash(name + phone)
    return person_id

#Deleting a contact from the dictionary by key (name)
def delete_contact(contacts):
    name = input('write name of contact: ')

    if name in contacts: 
        del contacts[name]
        print('*[INFO] Contact successfully deleted\n')
    else: 
        print('*[INFO] contact not found\n')

#Load contacts from 'contacts.dat' if there is nothing, 
# then except returns an empty dictionary
def load_contacts(): 
    try : 
        input_file = open('contacts.dat','rb')
        contacts = pickle.load(input_file)

        input_file.close()
    except: 
        contacts = {}
    return contacts
        
#save the modified dictionary in the same 'contacts.dat' document opened earlier
def save_contact(contacts):
    output_file = open('contacts.dat','wb')
    pickle.dump(contacts,output_file)

    output_file.close()

#entry point
if __name__ == "__main__":
    main()
else: 
    print("It's a main programm")