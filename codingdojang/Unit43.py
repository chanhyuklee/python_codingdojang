import re
url = input()
result = None
if re.match('^(http://|https://)[a-zA-Z0-9-\.]+\.([a-zA-zZ0-9]+)(/)*[a-zA-Z0-9-=_,\./]*', url):
    result = True
else:
    result = False
 
print(result)
