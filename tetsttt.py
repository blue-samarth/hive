from beem import Steem
from beem.block import Block
import json
s = Steem()

current_block_num = s.get_dynamic_global_properties()["head_block_number"]
num_blocks_to_search = 30
# block would be displayed in the console
print(Block(current_block_num))
bl = Block(current_block_num)
transactions = []
for i in range(current_block_num, current_block_num - num_blocks_to_search, -1):
    block = Block(i)
    for transaction in block["transactions"]:
        transactions.append(transaction)

if transactions:
    print("Transactions in the last 20 blocks:")
else:
    print("No transactions found in the last 20 blocks.")

