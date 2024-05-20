from web3 import Web3
import json

ganache_url = "http://127.0.0.1:7545"  # your Ganache local address

web3 = Web3(Web3.HTTPProvider(ganache_url))
print("Connected to Ganache")

# Get accounts
accounts = web3.eth.accounts

accounts_json = json.dumps(accounts, indent=4)

# Write JSON to file
with open('accounts.json', 'w') as json_file:
    json_file.write(accounts_json)
    
print("JSON file 'accounts.json' has been created successfully.")