
class A():
    pass

class B(A):
    pass


a = A()
b = B()

print(isinstance(b, A))
print(isinstance(a, A))
print(type(a) == type(b))
print(type(a), type(b))

c = 'sdjshdjs'
print(isinstance(c, str))