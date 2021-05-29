#!/usr/bin/env python3.9

# Account functions
from pw import Credentials, User

def create_account(name, email, uname, pw, user):
    return Credentials(name, email, uname, pw, user)

def save_account(account):
    account.save_account()

def generate_pw(length):
    Credentials.generate_pw(length)

def set_pw(pw):
    Credentials.set_pw(pw)

def display_accounts(user):
    Credentials.display_accounts(user)

def delete_account(account):
    account.delete_account()

# User functions
def create_user(fname, lname, uname, pw):
    return User(fname, lname, uname, pw)

def save_user(user):
    user.save_user()

def user_login(uname, pw):
    return user_login(uname, pw)

def delete_user(user):
    user.delete_user()

def display_users():
    return User.display_users()

# Main function
def main():
    pass

if __name__ == '__main__':
    main()