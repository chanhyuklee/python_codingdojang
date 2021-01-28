def html_tag(tag):
    def real_decorator(func):
        def wrapper():
            result = '<{0}>{1}</{2}>'.format(tag, func(), tag)
            return result
        return wrapper
    return real_decorator
 
a, b = input().split()
 
@html_tag(a)
@html_tag(b)
def hello():
    return 'Hello, world!'

print(hello())