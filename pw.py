import random
import string


class Account:
    '''
    Class to store the details of an account.
    '''
    accounts_list = []
    user_accounts = []
    def __init__(self, account_name, email, username, password, user):
        self.account_name = account_name
        self.email = email
        self.username = username
        self.password = password
        self.user = user


    def save_account(self):
        Account.accounts_list.append(self)
        
    @classmethod
    def generate_pw(cls, pw_length):
        pw = ''.join(random.choice(string.ascii_uppercase) for i in range(pw_length))
        return pw

    @classmethod
    def set_pw(cls,pw):
        return pw

    @classmethod
    def display_accounts(cls, user):
        for account in cls.accounts_list:
            if account.user == user:
                cls.user_accounts.append(account)
        return cls.user_accounts

    def delete_account(self):
        Account.accounts_list.remove(self)

class User:
    '''
    Class to manage user accounts.
    '''

    users_list = []
    def __init__(self, fname, lname, username, password) :
        self.fname = fname
        self.lname = lname
        self.username = username
        self.password = password

    def save_user(self):
        User.users_list.append(self)

    @classmethod
    def user_login(cls, username, pw):
        for user in User.users_list:
            if user.username == username and user.password == pw:
                return True
        return False

    def delete_user(self):
        for account in Account.accounts_list:
            if account.user == self.username:
                Account.accounts_list.remove(account)
        User.users_list.remove(self)
