import hashlib
import json
from textwrap import dedent
from time import time
from uuid import uuid4
from flask import Flask
from urllib.parse import urlparse
import requests


class blockchain(object):

    # instantiate our node
    app = Flask(_name_)

# Generate a globlly a unique address for this node
node_indentifier = str(uuid4.()).replace('-','')

# Instantiate the blockchain
blockchain = Blockchain()

@app.route('/mine', methods=['Get'])
def mine():
    # we run the proof of work algorthim to get the next proof...
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)

    # We must  receive a reward  for finding  the proof
    # the sender is "0" to signify  that is node  has mined  a new coin
    blockchain.new_transaction(
        sender="0",
        recipient=node_identifier,
        amount=1,
    )
    # forge the new block by adding it to chain
    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof, pervious_hash)

    response = {
        'message': "New block forged",
        'index': block['index',]
        'transactions': block['transactions'],
        'proof': block['proof'],
        'pervious_hash': block['previous_hash'],
    }
    return jsonfy(response), 200

@app.route('/transactions/new', methods=['Post'])
def new_transaction():
    values = request.get_json()

    # check that requird  fields  are in the post
    requird = ['sender', 'recipient', 'amount']
    if not all (k in values for k in requird):
        return 'Missing values', 400
    # Create a new transaction 
    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])
    response = {'message': f'Transaction will be added to Block {index}'} 
    return jsonify(response),201 


@app.route('/chain', methods=['Get'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
        
    }
    return jsonify(response), 200
if __name__ ==  '__main__':
    app.run(host = '0.0.0.0', port = '5000')    
   
   
   
   
    def proof_of_work(self, last_proof):
         """
        Simple Proof of Work Algorithm:
         - Find a number p' such that hash(pp') contains leading 4 zeroes, where p is the previous p'
         - p is the previous proof, and p' is the new proof
        :param last_proof: <int>
        :return: <int>
        """

        proof = 0

        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof    
    
    
    @staticmethod
    def valid_proof(last_proof, proof):
        """
        Validates the Proof: Does hash(last_proof, proof) contain 4 leading zeroes?
        :param last_proof: <int> Previous Proof
        :param proof: <int> Current Proof
        :return: <bool> True if correct, False if not.
        """
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return geuss_hash[:4] == "0000"
    
    
    
    
    
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        # create the genesis block
        self.new_block(pervious_hash=1, proof=100)
        self.nodes = set()

    def register_node(self, address):

        """
        Add a new node to the list of nodes
        :param address: <str> Address of node. Eg. 'http://192.168.0.5:5000'
        :return: None
        """
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)


    def  new_block(self, proof, previous_hash=None):
        """
        Create a new Block in the Blockchain
        :param proof: <int> The proof given by the Proof of Work algorithm
        :param previous_hash: (Optional) <str> Hash of previous Block
        :return: <dict> New Block
        """

        block = {
            'index':len(self.chain) + 1 ,
            'timestamp': time(),
            'transactoins': self.current_transactoins,
            'proof' : proof,
            'previous_hash' : pervious_hash or self.hash(self.chain[-1])
        }

        # Reset the current list of transactions
        self.current_transactions = []

        self.chain.append(block)
        return block

    def new_transactions(self, sender, recipient, amount):
        """
        Creates a new transaction to go into the next mined Block
        :param sender: <str> Address of the Sender
        :param recipient: <str> Address of the Recipient
        :param amount: <int> Amount
        :return: <int> The index of the Block that will hold this transaction
        """
        self.current_transactions.append({
            'sender': sender ,
            'recipient': recipient ,
            'amount': amount ,
        })
        
        return self.last_block['index'] +

    def valid_chain(self, chain):
        """
        Determine if a given blockchain is valid
        :param chain: <list> A blockchain
        :return: <bool> True if valid, False if not
        """
        last_block = chain[0]
        current_index = 1
        while current_index < len(chain):
            block = chain[current_index]
            print(f'{last_block}')
            print(f'{block}')
            print("\n-----------\n")
            # check the hash of the block is correct
            if block['pervious_hash'] != self.hash(last_block)
                return False
            # check the proof of work is correct
            if not self.valid_proof(last_block['proof'], block['proof']):
                return False
            last_block = block
            current_index += 1
        return True
    def resolve_conflicts(self):
        """
        This is our Consensus Algorithm, it resolves conflicts
        by replacing our chain with the longest one in the network.
        :return: <bool> True if our chain was replaced, False if not
        """
        neighbours = self.nodes
        new_chain = None
        # We are looking for a chains longer  than ours
        max_length = len(self.chain)

        # Grab and verify the chains from all the nodes in our network
        for node in neighbours :
            response = requests.get(f'http://{node}/chain')

            if response.status_code == 200 :
                length = response.json()['lenght']
                chain = response.json()['chain']

                # check if the length is longer and the chain is valid
                if length > max_length and self.valid_chain(chain):
                    max_length = length
                    new_chain = chain
        # replace our chain if we discovred a new one , valid chain longer than ours
        if new_chain:
            self.chain = new_chain
            retunr True

        return False                
        
    @staticmethod
    def hash(block):
        """
        Creates a SHA-256 hash of a Block
        :param block: <dict> Block
        :return: <str>
        """
        # We must make sure that the Dictionary is Ordered, or we'll have inconsistent hashes
        block_string =  json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
        

    @property
    def last_block(self):
        return self.chain[-1]    