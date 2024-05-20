from brownie import SimpleStorage, accounts

def main():
    admin = accounts[1]
    ss = SimpleStorage.deploy({
        "from": admin,
    })
    print("Poicy block is deployed at address:", ss)