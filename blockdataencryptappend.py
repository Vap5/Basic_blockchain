import hashlib
#m = hashlib.sha256()
#m.update(b"Nobody inspects")
#m.update(b" the spammish repetition")
#print(m.digest())
#print(m.digest_size)
#print(m.block_size)
class ExData:
    
    def __init__(self,previous_block_hash,data_bucket):
        self.previous_block_hash=previous_block_hash
        self.data_bucket=data_bucket
        self.block_data="-".join(data_bucket)+"-"+previous_block_hash
        self.block_hash=hashlib.sha256(self.block_data.encode()).hexdigest()

print("Write the data for 2 entries(Name and id_no) and Write name followed by Id !")                                         #Using dictionary DS

def listToString(s):  
    # initialize an empty string
    str1 = "" 
    # traverse in the string  
    for ele in s: 
        str1 += ele  
    # return string  
    return str1 
        
name=[]                                                                                                                      #For Name
# number of elements as input
n = int(input("Enter number of elements : "))
# iterating till the range
for i in range(0, n):
    ele =input()
    name.append(ele) # adding the element
print(name)

Id=[]                                                                                                                           #ID
n = int(input("Enter number of elements in integer: "))  
for i in range(0, n):
    ele =input()  
    Id.append(ele)       
print(Id)
nameStr=listToString(name)
idStr=listToString(Id)

#Let x be the number of blocks to be added in data blockchain.
n = int(input("Enter number of blocks to be appended and encrypted: "))  
for x in range(0, n):
    #for g in name:
        #for k in Id:


            x=ExData("Initial String",[nameStr,idStr])                         #Initial block#

            print(x.block_data)
            print(x.block_hash)

#second_block=VCoinBlock("initial_block.block_hash",[t3,t4])                #2nd block#

#print(second_block.block_data)
#print(second_block.block_hash)

#third_block=VCoinBlock("second_block.block_hash",[t4,t5])                  #3rd block#

#print(third_block.block_data)
#print(third_block.block_hash)


