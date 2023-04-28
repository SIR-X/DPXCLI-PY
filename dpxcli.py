import argparse

PROGNAME = "dpxcli.py"

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command")

subparsers.add_parser("help", help="Shows help menu")

balance_parser = subparsers.add_parser("balance", help="Retrieves the balance of the wallet")
balance_parser.add_argument("-w", "--wallet", help="ID of the wallet to retrieve the balance for")

transfer_parser = subparsers.add_parser("transfer", help="Transfers specified amount of DPX from departure wallet to destination wallet")
transfer_parser.add_argument("-a", "--amount", type=float, help="Amount of DPX to transfer")
transfer_parser.add_argument("-w", "--wallet", help="ID of the departure wallet")
transfer_parser.add_argument("-s", "--secret", help="Secret of the departure wallet")
transfer_parser.add_argument("-d", "--destination", help="ID of the destination wallet")

transactions_parser = subparsers.add_parser("transactions", help="Retrieves transactions in descending order from specified offset (default is 0)")
transactions_parser.add_argument("-o", "--offset", type=int, default=0, help="Offset to start retrieving transactions from")
transactions_parser.add_argument("-w", "--wallet", help="ID of the departure wallet")
transactions_parser.add_argument("-d", "--destination", help="ID of the destination wallet")

transaction_parser = subparsers.add_parser("transaction", help="Retrieves information of the given transaction ID")
transaction_parser.add_argument("-i", "--id", help="ID of the transaction to retrieve information for")

revoke_parser = subparsers.add_parser("revoke", help="Revokes the secret of the wallet and returns the new secret")
revoke_parser.add_argument("-w", "--wallet", help="ID of the wallet to revoke the secret for")
revoke_parser.add_argument("-s", "--secret", help="Secret of the wallet")

verify_parser = subparsers.add_parser("verify", help="Verifies a wallet credentials")
verify_parser.add_argument("-w", "--wallet", type=int, help="ID of the wallet to verify")
verify_parser.add_argument("-s", "--secret", help="Secret of the wallet")

args = parser.parse_args()

match args.command:
    case "help":
        parser.print_help()

    case "balance":
        ...

    case "transfer":
        ...

    case "transactions":
        ...

    case "transaction":
        ...

    case "revoke":
        ...

    case "verify":
        ...


