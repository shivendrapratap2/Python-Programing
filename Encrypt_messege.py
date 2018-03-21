from collections import OrderedDict

#function to return 2D index of any letter
def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return (10*(i+1)+(x.index(v)+1))

#variable initialisation
grid = []
Key = input("Enter a KeyWord: ")
alphabets = "asdfghjklxcvbnmqwertyuiopz"

#removing repeated elements from key
set_key = "".join(OrderedDict.fromkeys(Key))
grid_elements = ""
encrypted_msg = []

#creating mixed alphabet and filling in grid
for c in alphabets:
    if c not in set_key :
        grid_elements += c       
grid_elements = set_key + grid_elements

for i in range (0,5):
    rows = list(grid_elements[i*5:i*5+5])
    grid.append(rows)

#encoding message
message = input("Enter your message: ")

for c in message:
    if c != " " :
       encrypted_msg.append(index_2d(grid, c))
print(encrypted_msg)
