import unittest
from pw import Account

class TestAccount(unittest.TestCase):

    def setUp(self):
        self.account1 = Account('Twitter', 'peter@mail.com', '_peterken', 'p@$$w0rD')
        self.account2 = Account('Gmail', 'peter@mail.com', 'wittey', 'l0v3_L33')

    def tearDown(self):
        Account.pw_list = []


if __name__ == '__main__':
    unittest.main()