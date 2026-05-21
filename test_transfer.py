from ledger import transfer_funds, get_balance

print(f"Balance Account 1: {get_balance(1)}")
print(f"Balance Account 2: {get_balance(2)}")

# Perform transfer
success = transfer_funds(1, 2, 50)
print(f"Transfer successful: {success}")

print(f"Balance Account 1: {get_balance(1)}")
print(f"Balance Account 2: {get_balance(2)}")
