
class Foo():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def foo(self):
        pass


f  = Foo.__new__(Foo, object)
if isinstance(f, Foo) : f.__init__(10, 20)


print(f.y)