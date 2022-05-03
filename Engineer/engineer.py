class Engineer(object):

    def __init__(self):
        self.name = "Hundai"
        self.Engineer_on = False

    # def __new__(cls):
    #     if not hasattr(cls, 'instance'):
    #         cls.instance = super(Engineer, cls).__new__(cls)
    #     return cls.instance