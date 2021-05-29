import random
import string
class Account:
    '''
    Class to store the details of an account.
    '''
    accounts_list = []
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
    def display_accounts(cls):
        return Account.accounts_list

    def delete_account(self):
        Account.accounts_list.remove(self)

class User:
    '''
    Class to manage user accounts.
    '''

    def __init__(self, username, password) :
        pass
