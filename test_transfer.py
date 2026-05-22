import unittest
from ledger import transfer_funds, get_balance

class TestBankingTransfer(unittest.TestCase):
    def test_transfer_success(self):
        # Assuming account 1 has balance from setup_test_data
        initial_bal_1 = get_balance(1)
        initial_bal_2 = get_balance(2)
        
        success = transfer_funds(1, 2, 50)
        self.assertTrue(success)
        
        self.assertEqual(get_balance(1), initial_bal_1 - 50)
        self.assertEqual(get_balance(2), initial_bal_2 + 50)

    def test_insufficient_funds(self):
        # Attempt to transfer more than balance (assuming 1 has 100)
        success = transfer_funds(1, 2, 9999)
        self.assertFalse(success)

if __name__ == '__main__':
    unittest.main()
