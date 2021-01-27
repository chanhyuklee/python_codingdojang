a=[]
with open('words.txt', 'r') as file:
    a=file.read()
b = a.replace(',','')
b = b.replace('.','')
b = b.split()

for i in range(len(b)):
    if b[i].find('c')>-1:
        print(b[i])
