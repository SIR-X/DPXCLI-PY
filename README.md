# 💎 DPXCLI-PY
python command line utility for interacting with DPX API

## ✨ Examples

### 💠 Help
Description: shows the help menu  
Usage: `dpxcli.py help`
```text
$ dpxcli.py help
```

### 💠 Balance
Description: retrieves the balance of the wallet  
Usage: `dpxcli.py balance -w|--wallet <wallet>`
```text
$ dpxcli.py balance --wallet ADDRESS
```

### 💠 Transfer
Description: transfers specified amount of DPX from departure wallet to destination wallet  
Usage: `dpxcli.py transfer -a|--amount <amount> -w|--wallet <wallet> -s|--secret <secret> -d|--destination <destination>`
```text
$ dpxcli.py transfer --amount 10.5 --wallet ADDRESS --secret SECRET --destination ADDRESS
```

### 💠 Transactions
Description: retrieves transactions in descending order from specified offset (default is 0)  
Usage: `dpxcli.py transactions (-o|--offset <offset>)? (-w|--wallet <departure>)? (-d|--destination <destination>)?`
```text
$ dpxcli.py transactions // show latest 256 transactions
$ dpxcli.py transactions --offset 128 // show from offset 128
$ dpxcli.py transactions --wallet ADDRESS // filter transactions that are from this departure
$ dpxcli.py transactions --destination ADDRESS // filter transactions that are to this destination
$ dpxcli.py transactions -o 64 -w DEPARTURE -d DESTINATION // filter transactions that are from DEPARTURE to DESTINATION and show from offset 64
```

### 💠 Transaction
Description: retrieves information of the given transaction id  
Usage: `dpxcli.py transaction -i|--id <transactionId>`
```text
$ dpxcli.py transaction --id transactionId
```

### 💠 Revoke
Description: revokes the secret of the wallet and returns the new secret  
Usage: `dpxcli.py revoke -w|--wallet <wallet> -s|--secret <secret>`
```text
$ dpxcli.py revoke --wallet ADDRESS --secret SECRET
```

### 💠 Verify
Description: verifies a wallet credentials  
Usage: `dpxcli.py verify -w|--wallet <wallet> -s|--secret <secret>`
```text
$ dpxcli.py verify --wallet ADDRESS --secret SECRET
```

## ⚡ DPX API Documentation
You can read the [documentation of the DPX API here](https://github.com/Developix-ir/DPXCLI/blob/master/DPXAPI.md).


## 💻 C DPXCLI
You can see the main project made using C in [this repository](https://github.com/Developix-ir/DPXCLI).

## 🖊️ Contribution
Your contribution to dpxcli development is very welcome!

You may contribute in the following ways:

- Report issues and feedback
- Submit fixes, features via Pull Request
- Write/polish documentation

## 📃 License
GNU Affero General Public License v3.0 see https://www.gnu.org/licenses/agpl-3.0.en.html
