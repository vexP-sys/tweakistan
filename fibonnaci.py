a = 1          
b = 1         
position = 2   

while len(str(b)) < 100:   
    nächste = a + b        
    a = b                   
    b = nächste
    position = position + 1 

print(position)