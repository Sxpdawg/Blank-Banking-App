import unittest
from ledger import register_user, create_account, get_balance

class TestBankingLogic(unittest.TestCase):
    def test_user_registration(self):
        user_id = register_user("test_user", "pass", "test@test.com")
        self.assertIsNotNone(user_id)

    def test_account_creation(self):
        user_id = register_user("test_user_2", "pass", "test2@test.com")
        acc_id = create_account(user_id, "savings")
        self.assertIsNotNone(acc_id)
        self.assertEqual(get_balance(acc_id), 0.00)

if __name__ == '__main__':
    unittest.main()
