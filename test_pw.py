from types import GetSetDescriptorType
import unittest
from pw import Account

class TestAccount(unittest.TestCase):

    def setUp(self):
        self.account1 = Account('Twitter', 'peter@mail.com', '_peterken', 'p@$$w0rD')
        self.account2 = Account('Gmail', 'peter@mail.com', 'wittey', 'l0v3_L33')

    def tearDown(self):
        Account.pw_list = []

    def test_init(self):
        self.assertEqual(self.account1.account_name, 'Twitter')
        self.assertEqual(self.account1.email, 'peter@mail.com')
        self.assertEqual(self.account1.username, '_peterken')
        self.assertEqual(self.account1.password, 'p@$$w0rD')

    def test_save_account(self):
        self.account1.save_account()
        self.account2.save_account()

        self.assertEqual(len(Account.accounts_list), 2)
        self.assertEqual(Account.accounts_list[0].account_name, 'Twitter')

    def test_generate_pw(self):
        account3 = Account('Facebook', 'peter@mail.com', 'peter', Account.generate_pw(5))

        self.assertEqual(len(account3.password), 5)

    def test_set_pw(self):
        pw = Account.set_pw('P@$$word123')

        self.assertEqual(pw, 'P@$$word123')

    def test_display_contacts(self):
        self.account1.save_account()
        self.account2.save_account()

        self.assertEqual(len(Account.display_accounts()), 2)
    

if __name__ == '__main__':
    unittest.main()