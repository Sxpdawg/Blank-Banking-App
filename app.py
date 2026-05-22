import argparse
import ledger

def main():
    parser = argparse.ArgumentParser(description="Banking Ledger CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Transfer command
    transfer = subparsers.add_parser("transfer", help="Transfer funds")
    transfer.add_argument("--from", dest="from_acc", type=int, required=True)
    transfer.add_argument("--to", type=int, required=True)
    transfer.add_argument("--amount", type=float, required=True)
    transfer.add_argument("--memo", type=str, help="Add a description to the transfer")

    # History command
    history = subparsers.add_parser("history", help="Get transaction history")
    history.add_argument("--acc", type=int, required=True)

    # Balance command
    balance = subparsers.add_parser("balance", help="Get account balance")
    balance.add_argument("--acc", type=int, required=True)

    args = parser.parse_args()

    if args.command == "transfer":
        if ledger.transfer_funds(args.from_acc, args.to, args.amount, args.memo):
            print("Transfer successful!")
        else:
            print("Transfer failed.")
    elif args.command == "history":
        history = ledger.get_transaction_history(args.acc)
        for row in history:
            print(row)
    elif args.command == "balance":
        print(f"Balance: {ledger.get_balance(args.acc)}")

if __name__ == "__main__":
    main()
