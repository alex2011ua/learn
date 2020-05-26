class SomeObject:
    def __init__(self):
        self.integer_field = 0
        self.float_field = 0.0
        self.string_field = ""


class NullHandler:
    pass


class IntHandler(NullHandler):
    pass


class FloatHandle(NullHandler):
    pass


class StrHandler(NullHandler):
    pass

