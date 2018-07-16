

class lazyclass(object):
    classes = {}

    @classmethod
    def register(cls, clz):
        cls.classes[clz.__name__] = clz
        return clz

    @classmethod
    def get_class(cls, item):
        if item not in cls.classes:
            raise AttributeError
        return cls.classes[item]
