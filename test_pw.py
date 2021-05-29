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

if __name__ == '__main__':
    unittest.main()