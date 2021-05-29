class Account:
    '''
    Class to store the details of an account.
    '''
    pw_list = []
    def __init__(self, account_name, email, username, password):
        self.account_name = account_name
        self.email = email
        self.username = username
        self.password = password

        
