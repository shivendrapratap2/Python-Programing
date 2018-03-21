from collections import OrderedDict

#variable initialisation
grid = []
Key = input("Enter a KeyWord: ")
alphabets = "asdfghjklxcvbnmqwertyuiopz"

#removing repeated elements from key
set_key = "".join(OrderedDict.fromkeys(Key))
grid_elements = ""
message = ""

#creating mixed alphabet and filling in grid
for c in alphabets:
    if c not in set_key :
        grid_elements += c       
grid_elements = set_key + grid_elements

for i in range (0,5):
    rows = list(grid_elements[i*5:i*5+5])
    grid.append(rows)

#Decoding message
encrypted_msg = list(map(int, input("Enter encoded message: ").split()))

for index in encrypted_msg :
    x =  int(index/10)
    y = index%10
    message += grid[x-1][y-1]

print(message)
   
