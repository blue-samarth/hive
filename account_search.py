from beem import Hive
from beem.account import Account

# Initialize Hive instance
h = Hive()

def get_user_transactions(username):
    try:
        # Get the account object for the given username
        account = Account(username, blockchain_instance=h)

        # Get the list of transactions for the account
        transactions = account.history(use_block_num=False, only_ops=['transfer'])

        # Print the transactions
        print(f"Transactions for {username}:")
        for transaction in transactions:
            print(transaction)
        return transactions
    except Exception as e:
        print("An error occurred:", e)

# Call the function with a username
get_user_transactions('mcbot')
# Call the function with a different username


