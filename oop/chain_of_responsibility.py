class SomeObject:
    def __init__(self):
        self.integer_field = 0
        self.float_field = 0.0
        self.string_field = ""


class EventGet:
    def __init__(self, kind):
        self.kind = kind




class EventSet:
    def __init__(self, kind):
        self.kind = kind


class NullHandler:
    def __init__(self, successor=None):
        self.__successor = successor

    def handle(self, obj, event):
        if self.__successor is not None:
            return self.__successor.handle(obj, event)


class IntHandler(NullHandler):
    def handle(self, obg, event):
        if event.kind == int:
            return obg.integer_field
        elif type(event.kind) == int:
            obg.integer_field = event.kind

        else:
            return super().handle(obg, event)


class FloatHandler(NullHandler):
    def handle(self, obg, event):
        if event.kind == float:
            return obg.float_field
        elif type(event.kind) == float:
            obg.float_field = event.kind

        else:
            return super().handle(obg, event)


class StrHandler(NullHandler):
    def handle(self, obg, event):
        if event.kind == str:
            return obg.string_field
        elif type(event.kind) == str:
            obg.string_field = event.kind

        else:
            return super().handle(obg, event)

'''obj = SomeObject()
obj.integer_field = 42
obj.float_field = 3.14
obj.string_field = "some text"
chain = IntHandler(FloatHandler(StrHandler(NullHandler)))
print(chain.handle(obj, EventGet(int)))


print(chain.handle(obj, EventGet(str)))

chain.handle(obj, EventSet(100))
print(chain.handle(obj, EventGet(int)))

chain.handle(obj, EventSet(0.5))
print(chain.handle(obj, EventGet(float)))

chain.handle(obj, EventSet('new text'))
print(chain.handle(obj, EventGet(str)))
'''