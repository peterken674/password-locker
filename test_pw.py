import unittest

from pw import Credentials, User


class TestCredentials(unittest.TestCase):
    """Test class that defines test cases for the credentials class behaviours.

    Args:
        unittest (TestCase): TestCase class that helps in creating test cases.
    """

    def setUp(self):
        """setUp method to run before each test cases.
        """
        self.account1 = Credentials('Twitter', 'peter@mail.com', '_peterken', 'p@$$w0rD', 'ken')
        self.account2 = Credentials('Gmail', 'peter@mail.com', 'wittey', 'l0v3_L33', 'ken')

    def tearDown(self):
        """tearDown method that does clean up after each test case has run.
        """
        Credentials.accounts_list = []

    def test_init(self):
        """test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.account1.account_name, 'Twitter')
        self.assertEqual(self.account1.email, 'peter@mail.com')
        self.assertEqual(self.account1.username, '_peterken')
        self.assertEqual(self.account1.password, 'p@$$w0rD')
        self.assertEqual(self.account1.user, 'ken')

    def test_save_account(self):
        """test_save_account test case to test if the credential object is saved into the credentials list
        """
        self.account1.save_account()
        self.account2.save_account()

        self.assertEqual(len(Credentials.accounts_list), 2)
        self.assertEqual(Credentials.accounts_list[0].account_name, 'Twitter')

    def test_generate_pw(self):
        """test_generate_pw test case to test whether we can generate a random password given a desired length.
        """
        self.assertEqual(len(Credentials.generate_pw(5)), 5)

    def test_set_pw(self):
        """test_set_pw test case to test whether we can set a password for an object (both credentials and users) when creating one.
        """
        pw = Credentials.set_pw('P@$$word123')

        self.assertEqual(pw, 'P@$$word123')

    def test_display_contacts(self):
        """Method returns a list of all credentials whose owner is the currently logged in user, passed as an argument.
        """
        self.account1.save_account()
        self.account2.save_account()
        
        self.assertEqual(Credentials.display_accounts('ken'), Credentials.user_accounts)

    def test_delete_account(self):
        """test_delete_account to test if we can remove a credential from our credentials list.
        """
        self.account1.save_account()
        self.account2.save_account()

        self.account1.delete_account()

        self.assertEqual(len(Credentials.accounts_list), 3)

class TestUser(unittest.TestCase):
    """Test class that defines test cases for the user class behaviours.

    Args:
        unittest (TestCase): TestCase class that helps in creating test cases.
    """
    
    def setUp(self):
        """setUp method to run before each test cases.
        """
        self.user1 = User('Peter', 'Kennedy','peterken', 'iloveyou')
        self.user2 = User('John', 'Doe', 'johndoe', 'dontknowyou')
    
    def tearDown(self):
        """tearDown method that does clean up after each test case has run.
        """
        User.users_list = []

    def test_init(self):
        """test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.user1.fname, 'Peter')
        self.assertEqual(self.user1.lname, 'Kennedy')
        self.assertEqual(self.user1.username, 'peterken')
        self.assertEqual(self.user1.password, 'iloveyou')

    def test_save_user(self):
        """test_save_user test case to test if the user object is saved into the users list
        """
        self.user1.save_user()
        self.user2.save_user()

        self.assertEqual(len(User.users_list), 2)
        self.assertEqual(User.users_list[0].username, 'peterken')

    def test_user_login(self):
        """test_save_user test case to test if a user can log in with their username and password.
        """
        self.user1.save_user()
        self.user2.save_user()
        auth_user = User.user_login('peterken', 'iloveyou')

        self.assertEqual(auth_user, self.user1)

    def test_delete_user(self):
        """test_delete_user to test if we can remove a user from our users list
        """
        self.user1.save_user()
        self.user2.save_user()

        self.user2.delete_user()

        self.assertEqual(len(User.users_list), 2)

    # def test_display_users(self):
    #     self.user1.save_user()
    #     self.user2.save_user()

    #     self.assertEqual(User.display_users(), User.users_list)

if __name__ == '__main__':
    unittest.main()
