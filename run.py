#!/usr/bin/env python3.9

# Functions
from pw import Credentials, User

def create_account(name, email, uname, pw, user):
    """Function to create a new contact.
    """
    new_credential = Credentials(name, email, uname, pw, user)
    return new_credential

def save_account(account):
    """Function to save a credential.
    """
    account.save_account()

def generate_pw(length):
    """Function to generate a new random password.
    """
    return Credentials.generate_pw(length)

def set_pw(pw):
    """Function to set credential password.
    """
    return Credentials.set_pw(pw)

def display_accounts(user):
    """Function that returns all credentials of logged in user.
    """
    accounts = Credentials.display_accounts(user)
    return accounts

def delete_account(account):
    """Function to delete a credential.
    """
    account.delete_account()

# User functions
def create_user(fname, lname, uname, pw):
    """Function for creating new user.
    """
    new_user = User(fname, lname, uname, pw)
    return new_user

def save_user(user):
    """Save user.
    """
    user.save_user()

def user_login(uname, pw):
    """Function to handle user login.
    """
    return User.user_login(uname, pw)

def delete_user(user):
    """Function to remove user.
    """
    user.delete_user()

# def display_users():
#     return User.display_users()

# Main function
def main():
    print('Hello. Welcome to PassLock. Please log in or add new account to continue.\n\n')

    exit = False
    while not exit:
        print('What would you like to do? (enter number to select)')
        print('--'*25)
        print('1. Create new user.\n2. Log in to an existing account.\n3. Remove user.\n4. Exit.')
        choice = input('Enter choice: ')

        # Create new user.
        if choice == '1':
            print('\n\n***Create New User***\n')
            fname = input('First Name: ')
            lname = input('Last Name: ')
            username = input('Username: ')
            # Choose mode of password creation.
            while True:
                print('Password: \n\t1. Autogenerate password.\n\t2. Enter custom password.')
                pw_input_choice = input('\tEnter choice: ')
                if pw_input_choice == '1':
                    pw_length = int(input('Enter desired autogenerated password length: '))
                    password = generate_pw(pw_length)
                    print(f'Autogenerated password is {password} \nYou will need to remember this.')
                    break
                elif pw_input_choice == '2':
                    pw_input = input('Enter password: ')
                    password = set_pw(pw_input)
                    break
                else:
                    print('Invalid choice. Try again.\n\n')

            save_user(create_user(fname, lname, username, password))
            print(f'\nNew user {fname} {lname} created.\n\n')

        elif choice == '2':
            print('\n\n***Log In***\n')
            uname = input('Enter username: ')
            pw = input('Enter password: ')
            user_logged_in = user_login(uname, pw)
            if user_logged_in:
                print(f'\n\nLogin successful. Welcome {user_logged_in.fname}.\n\n')

                while True:
                    print('What would you like to do?')
                    print('--'*15)
                    print('1. Add new credentials.\n2. Store existing credentials.\n3. View stored credentials.\n4. Delete credential.\n5. Logout\n6. Exit')

                    selection = input('Enter selection: ')
                    if selection == '1':
                        print('\n\n***Add New Credential***\n\n')
                        name = input('Credential Name: ')
                        email = input('Email Address: ')
                        usrnm = input('Username: ')
                        while True:
                            print('Password: \n\t1. Autogenerate password.\n\t2. Enter custom password.')
                            pw_input_choice = input('\tEnter choice: ')
                            if pw_input_choice == '1':
                                pw_length = int(input('Enter desired autogenerated password length: '))
                                acc_pw = generate_pw(pw_length)
                                print(f'Autogenerated password is {acc_pw}')
                                break
                            elif pw_input_choice == '2':
                                pw_input = input('Enter password: ')
                                acc_pw = set_pw(pw_input)
                                break
                            else:
                                print('Invalid choice. Try again.\n\n')

                        # Create new account
                        new_account = create_account(name, email, usrnm, acc_pw, user_logged_in.username)
                        new_account.save_account()
                        print(f'\n\n{name} account created.\n\n')

                    # Existing credentials.
                    elif selection == '2':
                        print('\n\n***Add New Credential***\n\n')
                        name = input('Credential Name: ')
                        email = input('Email Address: ')
                        usrnm = input('Username: ')
                        pw_input = input('Password: ')
                        acc_pw = set_pw(pw_input)

                        new_account = create_account(name, email, usrnm, acc_pw, user_logged_in.username)
                        new_account.save_account()
                        print(f'\n\n{name} account created.\n\n')

                    elif selection == '3':
                        Credentials.user_accounts = []
                        print('\n\n***Saved Credentials***\n\n')
                        accounts = display_accounts(user_logged_in.username)
                        if accounts:
                            print('Account      \tUsername      \tPassword')
                            print('-'*40)
                            for account in accounts:
                                print(f'{account.account_name} .....\t{account.username} .....\t{account.password}')
                            Credentials.user_accounts = []
                            accounts = []
                        else:
                            print("You don't seem to have any credentials saved yet.")
                        print('\n\n')
                        continue

                    elif selection == '4':
                        accounts = display_accounts(user_logged_in.username)
                        if accounts:
                            print('\n\n***Delete Credential***\n\n')
                            acc_name = input('Enter name of credential to delete: ')
                            for account in accounts:
                                if account.account_name == acc_name:
                                    print(f'\n\n{account.account_name} credentials deleted successfully.')
                                    delete_account(account)
                            print('Credential does not exist, please check your spelling.')
                            accounts = []
                        else:
                            print("Your password locker is empty.")
                        print('\n\n')
                        continue

                    elif selection == '5':
                        user_logged_in = create_user('', '', '', '')
                        print('\n\nLogged out successfully.\n\n')
                        break
                    elif selection == '6':
                        print('\n\n***GOODBYE***\n\n')
                        exit = True
                        break
                    
            else:
                print('Invalid credentials or user does not exist.\n\n')
            continue

        elif choice == '3':
            print('\n\n***Remove User***\n\n')
            del_usrname = input('Username of user: ')
            users = User.users_list
            if users:
                done = False
                while not done:
                    for user in users:
                        if user.username == del_usrname:
                            confirm = input(f'\nAre you sure you want to delete user {user.fname} {user.lname}?(Y/n)')
                            confirm = confirm.lower()

                            if confirm == 'y':
                                del_pw = input('Enter password: ')
                                if user.password == del_pw:
                                    print(f'\n{user.fname} {user.lname} removed successfully\n\n')
                                    delete_user(user)
                                    done = True
                                else:
                                    print('Password is incorrect.')
                            elif confirm == 'n':
                                print('\n\n')
                                done = True
                            else:
                                print("I didn't quite get that. Please enter 'y' or 'n' for yes or no.\n\n")
            else:
                print('No users exist.')
            continue

        elif choice == '4':
            print('\n\n***GOODBYE***\n\n')
            exit = True

        else:
            print("\nI didn't quite get that. Try again.\n")


if __name__ == '__main__':
    main()