import hashlib
import random
import binascii
import datetime
import collections
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5
from collections import OrderedDict
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5

class Client:
    def __init__(self):
        random_gen = Random.new().read
        self._private_key = RSA.generate(1024, random_gen)
        self._public_key = self._private_key.publickey()
        self._signer = PKCS1_v1_5.new(self._private_key)

    @property
    def identity(self):
        return binascii.hexlify(self._public_key.exportKey(format='DER')).decode('ascii')

class Transaction:
    def __init__(self, sender, recipient, value):
        self.sender = sender
        self.recipient = recipient
        self.value = value
        self.time = datetime.datetime.now()

    def to_dict(self):
        if self.sender == "Genesis":
            identity = "Genesis"
        else:
            identity = self.sender.identity
        return OrderedDict({
            'sender': identity,
            'recipient': self.recipient,
            'value': self.value,
            'time': str(self.time)
        })

    def sign_transaction(self):
        private_key = self.sender._private_key
        signer = PKCS1_v1_5.new(private_key)
        h = SHA.new(str(self.to_dict()).encode('utf8'))
        return binascii.hexlify(signer.sign(h)).decode('ascii')


def display_transaction(transaction):
    details = transaction.to_dict()
    print("Sender: " + details['sender'])
    print("Recipient: " + details['recipient'])
    print("Value: " + str(details['value']))
    print("Time: " + details['time'])
    print('-------------------------------------')


def dump_blockchain(blockchain):
    print("Number of blocks in the chain: " + str(len(blockchain)))
    for index, block in enumerate(blockchain):
        print("Block #" + str(index))
        for transaction in block.verified_transactions:
            display_transaction(transaction)
        print('=====================================')


class Block:
    def __init__(self):
        self.verified_transactions = []
        self.previous_block_hash = ""
        self.Nonce = ""


def sha256(message):
    return hashlib.sha256(message.encode('ascii')).hexdigest()


def mine(message, difficulty=1):
    assert difficulty >= 1
    prefix = '1' * difficulty
    for i in range(100000):  # Increased range for better mining chances
        digest = sha256(str(hash(message)) + str(i))
        if digest.startswith(prefix):
            return i
    return None


# Clients
A = Client()
B = Client()
C = Client()

# Transactions
t0 = Transaction("Genesis", A.identity, 500.0)
t1 = Transaction(A, B.identity, 40.0)
t2 = Transaction(A, C.identity, 70.0)
t3 = Transaction(B, C.identity, 700.0)

# Blockchain
TPCoins = []

# Block 0 (Genesis Block)
block0 = Block()
block0.previous_block_hash = None
block0.Nonce = None
block0.verified_transactions.append(t0)
digest = hash(block0)
last_block_hash = digest
TPCoins.append(block0)

# Block 1
block1 = Block()
block1.previous_block_hash = last_block_hash
block1.verified_transactions.append(t1)
block1.verified_transactions.append(t2)
block1.Nonce = mine(str(block1), 2)
digest = hash(block1)
last_block_hash = digest
TPCoins.append(block1)

# Block 2
block2 = Block()
block2.previous_block_hash = last_block_hash
block2.verified_transactions.append(t3)
block2.Nonce = mine(str(block2), 2)
digest = hash(block2)
last_block_hash = digest
TPCoins.append(block2)

# Display Blockchain
dump_blockchain(TPCoins)
