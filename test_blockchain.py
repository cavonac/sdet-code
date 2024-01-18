import hashlib
import json
from time import time

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        
        # Create the genesis block
        self.new_block(previous_hash='1', proof=100)

    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]) if self.chain else None,
        }
        
        # Reset the current list of transactions
        self.current_transactions = []
        
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        return self.last_block['index'] + 1

    @property
    def last_block(self):
        return self.chain[-1] if self.chain else None

    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

def test_new_transaction():
    blockchain = Blockchain()
    blockchain.new_transaction("Alice", "Bob", 2)
    assert len(blockchain.current_transactions) == 1
    assert blockchain.current_transactions[0]['sender'] == "Alice"
    assert blockchain.current_transactions[0]['recipient'] == "Bob"
    assert blockchain.current_transactions[0]['amount'] == 2

def test_new_block():
    blockchain = Blockchain()
    proof = 12345
    blockchain.new_block(proof)
    assert len(blockchain.chain) == 2 # Check the length of the chain
    assert blockchain.chain[-1]['proof'] == proof  # Check the proof of the last block
    assert len(blockchain.current_transactions) == 0  # Transactions should be cleared after a new block

def test_full_blockchain():
    blockchain = Blockchain()
    blockchain.new_transaction("Alice", "Bob", 2)
    blockchain.new_transaction("Bob", "Charlie", 1)
    proof = 12345
    blockchain.new_block(proof)

    # Add more assertions based on the expected behavior of your blockchain