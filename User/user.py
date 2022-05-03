
class User(object):

    def __init__(self):
        self.name = "JH"
        self.user_on = False

    # # singleton
    # def __new__(cls):
    #     if not hasattr(cls, 'instance'):
    #         cls.instance = super(User, cls).__new__(cls)
    #     return cls.instance
    #
