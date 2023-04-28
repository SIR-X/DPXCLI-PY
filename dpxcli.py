import re
import argparse
from modules import *

PROGNAME = "dpxcli.py"

def md5(value: str):
    if not re.match(r"^[a-fA-F0-9]{32}$", value):
        raise argparse.ArgumentTypeError(f"Invalid structure: {value}")

    return value

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command")

subparsers.add_parser("help", help="Shows help menu")

balance_parser = subparsers.add_parser("balance", help="Retrieves the balance of the wallet")
balance_parser.add_argument("-w", "--wallet", type=md5, required=True, help="ID of the wallet to retrieve the balance for")

transfer_parser = subparsers.add_parser("transfer", help="Transfers specified amount of DPX from departure wallet to destination wallet")
transfer_parser.add_argument("-a", "--amount", type=float, required=True, help="Amount of DPX to transfer")
transfer_parser.add_argument("-w", "--wallet", type=md5, required=True, help="ID of the departure wallet")
transfer_parser.add_argument("-s", "--secret", type=md5, required=True, help="Secret of the departure wallet")
transfer_parser.add_argument("-d", "--destination", type=md5, required=True, help="ID of the destination wallet")

transactions_parser = subparsers.add_parser("transactions", help="Retrieves transactions in descending order from specified offset (default is 0)")
transactions_parser.add_argument("-o", "--offset", type=int, default=0, help="Offset to start retrieving transactions from")
transactions_parser.add_argument("-w", "--wallet", type=md5, help="ID of the departure wallet")
transactions_parser.add_argument("-d", "--destination", type=md5, help="ID of the destination wallet")

transaction_parser = subparsers.add_parser("transaction", help="Retrieves information of the given transaction ID")
transaction_parser.add_argument("-i", "--id", type=md5, required=True, help="ID of the transaction to retrieve information for")

revoke_parser = subparsers.add_parser("revoke", help="Revokes the secret of the wallet and returns the new secret")
revoke_parser.add_argument("-w", "--wallet", type=md5, required=True, help="ID of the wallet to revoke the secret for")
revoke_parser.add_argument("-s", "--secret", type=md5, required=True, help="Secret of the wallet")

verify_parser = subparsers.add_parser("verify", help="Verifies a wallet credentials")
verify_parser.add_argument("-w", "--wallet", type=md5, required=True, help="ID of the wallet to verify")
verify_parser.add_argument("-s", "--secret", type=md5, required=True, help="Secret of the wallet")

args = parser.parse_args()

match args.command:
    case "help":
        parser.print_help()

    case "balance":
        modules.show_balance(args.wallet)

    case "transfer":
        modules.show_transfer(args.wallet, args.secret, args.destination, args.amount)

    case "transactions":
        modules.show_transactions(args.wallet, args.destination, args.offset)

    case "transaction":
        modules.show_transaction(args.id)

    case "revoke":
        modules.show_revoke(args.wallet, args.secret)

    case "verify":
        modules.show_verify(args.wallet, args.secret)