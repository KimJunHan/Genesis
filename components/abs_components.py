from abc import ABCMeta, abstractmethod

class abs_components(metaclass=ABCMeta):

    @abstractmethod
    def accelerator(self):
        pass

    @abstractmethod
    def brake(self):
        pass

    @abstractmethod
    def engine(self):
        pass

    @abstractmethod
    def steering(self):
        pass