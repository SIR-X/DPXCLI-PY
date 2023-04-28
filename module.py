from requests.api import get as req_get, post as req_post

from colorama import init, Fore
from typing   import Literal


DPXAPI = "https://dpx.developix.ir/api"
PROGNAME = "dxpcli"

init()


def show_error(result: dict) -> None:
    max_length = max(map(len, result)) + 1

    print("\n".join(
        f"{Fore.RED + key.title()}:{(max_length - key.__len__()) * ' '}{Fore.RESET + value}"
        for key, value in result.items()
    ))


def show_box(result: dict | list) -> None:
    max_length = 45

    def design(key: str, value: str | int):
        length = max_length - (len(key) + len(value.__str__())) - 2
        key_length = max_key_length - key.__len__()

        return f"║ {key.title()}: {key_length * ' '}{value}{(length - key_length) * ' '} ║"

    if isinstance(result, dict):
        max_key_length = max(map(len, result))

        print(
            f"╔═{max_length * '═'}═╗",
            "\n".join(design(key, value) for key, value in result.items()),
            f"╚═{max_length * '═'}═╝",
            sep="\n",
        )

    else:
        max_key_length = max(map(len, result[0]))

        print(
            f"╔═{max_length * '═'}═╗",
            f"\n╠═{max_length * '═'}═╣\n".join(
                "\n".join(
                    design(key, value)
                    for key, value in item.items()
                )
                for item in result
            ),
            f"╚═{max_length * '═'}═╝",
            sep="\n"
        )


class modules:
    @classmethod
    def request(self, method: Literal["get", "post"] = "get", endpoint: str = "", json: dict = None):
        try:
            match method:
                case "get":
                    result = req_get(DPXAPI + endpoint).json()

                case "post":
                    result = req_post(DPXAPI + endpoint, json=json).json()

            if result.pop("status") == "success":
                return result["result"]

            else:
                show_error(result)
                return

        except (ConnectionError, IOError):
            print("Invalid response")
            return

    @classmethod
    def show_balance(self, wallet: str) -> None:
        result = self.request(endpoint="/balance/" + wallet)

        if result:
            print(
                f"{Fore.CYAN}Balance is: {Fore.LIGHTCYAN_EX}{result} DPX{Fore.RESET}")

    @classmethod
    def show_transfer(self, departure: str, secret: str, destination: str, amount: int) -> None:
        data = {
            "departure": departure,
            "secret": secret,
            "destination": destination,
            "amount": amount
        }

        result = self.request("post", "/transfer", json=data)

        if result:
            show_box(result)

    @classmethod
    def show_transaction(self, transactionId: str) -> None:
        result = self.request(endpoint="/transaction/" + transactionId)

        if result:
            show_box(result)

    @classmethod
    def show_transactions(self, departure: str = None, destination: str = None, offset: int = None) -> None:
        data = {
            "destination": destination,
            "departure": departure,
            "offset": offset
        }

        result = self.request("post", "/transactions", json=data)

        if result:
            show_box(result)

    @classmethod
    def show_verify(self, wallet: str, secret: str) -> None:
        data = {
            "wallet": wallet,
            "secret": secret
        }

        result = self.request("post", "/verify", json=data)

        if result:
            print(f"{Fore.CYAN}Credentials are valid for the wallet{Fore.RESET}")

    @classmethod
    def show_revoke(self, wallet: str, secret: str) -> None:
        data = {
            "wallet": wallet,
            "secret": secret
        }

        result = self.request("post", "/revoke", json=data)

        if result:
            print(
                f"{Fore.CYAN}Secret has been revoked, the new Secret is: {Fore.LIGHTCYAN_EX + result + Fore.RESET}")