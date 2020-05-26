class SomeObject:
    def __init__(self):
        self.integer_field = 0
        self.float_field = 0.0
        self.string_field = ""


class EventGet:
    def __init__(self, kind):
        self.get = kind
        self.set = None


class EventSet:
    def __init__(self, kind):
        self.set = kind
        self.get = None


class NullHandler:
    def __init__(self, successor=None):
        self.__successor = successor

    def handle(self, obj, event):
        if self.__successor is not None:
            self.__successor.handle(obj, event)


class IntHandler(NullHandler):
    def handle(self, obg, event):
        if event.get == int:
            print(obg.integer_field)
        elif type(event.set) == int:
            obg.integer_field = event.set

        else:

            super().handle(obg, event)


class FloatHandler(NullHandler):
    def handle(self, obg, event):
        if event.get == float:
            print(obg.float_field)
        elif type(event.set) == float:
            obg.float_field = event.set

        else:

            super().handle(obg, event)


class StrHandler(NullHandler):
    def handle(self, obg, event):
        if event.get == str:
            print(obg.string_field)
        elif type(event.set) == str:
            obg.string_field = event.set

        else:

            super().handle(obg, event)
