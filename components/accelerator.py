import  abs_components

class Accelerator(abs_components):

    def __init__(self):
        self.accelerator()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Accelerator, cls).__new__(cls)
        return cls.instance

    def accelerator(self):
        return Accelerator()




