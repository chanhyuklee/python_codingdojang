#24.5 
Word = input()
Word=Word.replace(',','') 
Word=Word.replace('.','') 
Word=Word.split() 
count=Word.count('the') 
print(count) 


#24.6
Price = input()
Price=Price.split(';')  
for i in range(len(Price)):
    Price[i]=int(Price[i])  #
Price.sort(reverse=True)
for i in range(len(Price)): 
    print(str("{:9,}".format(Price[i])))
