with open('words.txt', 'r') as file:
    a=file.read()
    a=a.split('\n')
for i in a:
    j=list(i)
    j.reverse()
    if list(i)==j:
        print(i)
