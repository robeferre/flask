class Enum(object):
    @classmethod
    def all(cls):
        return [v for k,v in cls.__dict__.iteritems() if k[0] != '_']
