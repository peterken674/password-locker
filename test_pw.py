import unittest

from pw import Credentials, User


class TestAccount(unittest.TestCase):

    def setUp(self):
        self.account1 = Credentials('Twitter', 'peter@mail.com', '_peterken', 'p@$$w0rD', 'ken')
        self.account2 = Credentials('Gmail', 'peter@mail.com', 'wittey', 'l0v3_L33', 'ken')

    def tearDown(self):
        Credentials.accounts_list = []

    def test_init(self):
        self.assertEqual(self.account1.account_name, 'Twitter')
        self.assertEqual(self.account1.email, 'peter@mail.com')
        self.assertEqual(self.account1.username, '_peterken')
        self.assertEqual(self.account1.password, 'p@$$w0rD')
        self.assertEqual(self.account1.user, 'ken')

    def test_save_account(self):
        self.account1.save_account()
        self.account2.save_account()

        self.assertEqual(len(Credentials.accounts_list), 2)
        self.assertEqual(Credentials.accounts_list[0].account_name, 'Twitter')

    def test_generate_pw(self):

        self.assertEqual(len(Credentials.generate_pw(5)), 5)

    def test_set_pw(self):
        pw = Credentials.set_pw('P@$$word123')

        self.assertEqual(pw, 'P@$$word123')

    def test_display_contacts(self):
        self.account1.save_account()
        self.account2.save_account()
        
        self.assertEqual(Credentials.display_accounts('ken'), Credentials.user_accounts)

    def test_delete_account(self):
        self.account1.save_account()
        self.account2.save_account()

        self.account1.delete_account()

        self.assertEqual(len(Credentials.accounts_list), 1)

class TestUser(unittest.TestCase):
    
    def setUp(self):
        self.user1 = User('Peter', 'Kennedy','peterken', 'iloveyou')
        self.user2 = User('John', 'Doe', 'johndoe', 'dontknowyou')
    
    def tearDown(self):
        User.users_list = []

    def test_init(self):
        self.assertEqual(self.user1.fname, 'Peter')
        self.assertEqual(self.user1.lname, 'Kennedy')
        self.assertEqual(self.user1.username, 'peterken')
        self.assertEqual(self.user1.password, 'iloveyou')

    def test_save_user(self):
        self.user1.save_user()
        self.user2.save_user()

        self.assertEqual(len(User.users_list), 2)
        self.assertEqual(User.users_list[0].username, 'peterken')

    def test_user_login(self):
        self.user1.save_user()
        self.user2.save_user()
        auth_user = User.user_login('peterken', 'iloveyou')

        self.assertEqual(auth_user, self.user1)

    def test_delete_user(self):
        self.user1.save_user()
        self.user2.save_user()

        self.user2.delete_user()

        self.assertEqual(len(User.users_list), 1)
        self.assertEqual(len(Credentials.accounts_list), 0)

    def test_display_users(self):
        self.user1.save_user()
        self.user2.save_user()

        self.assertEqual(User.display_users(), User.users_list)

if __name__ == '__main__':
    unittest.main()
