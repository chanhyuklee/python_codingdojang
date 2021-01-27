keys = input().split()
values = map(int, input().split())

x = dict(zip(keys,values))

x.pop('delta')
x = {keys:values for keys,values in x.items() if values != 30}
print(x)
