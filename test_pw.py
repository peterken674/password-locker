from types import GetSetDescriptorType
import unittest
from pw import Account
from pw import User

class TestAccount(unittest.TestCase):

    def setUp(self):
        self.account1 = Account('Twitter', 'peter@mail.com', '_peterken', 'p@$$w0rD', 'ken')
        self.account2 = Account('Gmail', 'peter@mail.com', 'wittey', 'l0v3_L33', 'ken')

    def tearDown(self):
        Account.accounts_list = []

    def test_init(self):
        self.assertEqual(self.account1.account_name, 'Twitter')
        self.assertEqual(self.account1.email, 'peter@mail.com')
        self.assertEqual(self.account1.username, '_peterken')
        self.assertEqual(self.account1.password, 'p@$$w0rD')
        self.assertEqual(self.account1.user, 'ken')

    def test_save_account(self):
        self.account1.save_account()
        self.account2.save_account()

        self.assertEqual(len(Account.accounts_list), 2)
        self.assertEqual(Account.accounts_list[0].account_name, 'Twitter')

    def test_generate_pw(self):
        account3 = Account('Facebook', 'peter@mail.com', 'peter', Account.generate_pw(5), 'ken')

        self.assertEqual(len(account3.password), 5)

    def test_set_pw(self):
        pw = Account.set_pw('P@$$word123')

        self.assertEqual(pw, 'P@$$word123')

    def test_display_contacts(self):
        self.account1.save_account()
        self.account2.save_account()

        self.assertEqual(len(Account.display_accounts()), 2)

    def test_delete_account(self):
        self.account1.save_account()
        self.account2.save_account()

        self.account1.delete_account()

        self.assertEqual(len(Account.accounts_list), 1)

class TestUser(unittest.TestCase):
    
    def setUp(self):
        self.user1 = User('peterken', 'iloveyou')
        self.user2 = User('johndoe', 'dontknowyou')
    
    def tearDown(self):
        User.users_list = []

    def test_init(self):
        self.assertEqual(self.user1.username, 'peterken')
        self.assertEqual(self.user1.password, 'iloveyou')

    def test_save_user(self):
        self.user1.save_user()
        self.user2.save_user()

        self.assertEqual(len(User.users_list), 2)
        self.assertEqual(User.users_list[0].username, 'peterken')

if __name__ == '__main__':
    unittest.main()