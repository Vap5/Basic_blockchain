import hashlib
class VCoinBlock:
    
    def __init__(self,previous_block_hash,transaction_list):
        self.previous_block_hash=previous_block_hash
        self.transaction_list=transaction_list
        self.block_data="-".join(transaction_list)+"-"+previous_block_hash
        self.block_hash=hashlib.sha256(self.block_data.encode()).hexdigest()

t1="Alice sends 2 VC to Mike"
t2="Bob sends 5 VC to Mike"
t3="Mike sends 3 VC to Bob"
t4="Daniel sends 11 VC to Alice"
t5="Mike sends 2 VC to Daniel"

initial_block=VCoinBlock("Initial String",[t1,t2])                         #Initial block#

print(initial_block.block_data)
print(initial_block.block_hash)

second_block=VCoinBlock("initial_block.block_hash",[t3,t4])                #2nd block#

print(second_block.block_data)
print(second_block.block_hash)

third_block=VCoinBlock("second_block.block_hash",[t4,t5])                  #3rd block#

print(third_block.block_data)
print(third_block.block_hash)