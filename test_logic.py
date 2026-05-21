from ledger import register_user, create_account, get_balance

# 1. Register a user
user_id = register_user("john_doe", "hashed_password_123", "john@example.com")
print(f"Registered user ID: {user_id}")

if user_id:
    # 2. Create an account
    acc_id = create_account(user_id, "savings")
    print(f"Created account ID: {acc_id}")

    # 3. Check balance
    balance = get_balance(acc_id)
    print(f"Current balance: {balance}")
