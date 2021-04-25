from abc import ABC, abstractmethod

class Entity(ABC):

    @abstractmethod
    def from_dict(self, dict):
        pass
   
    @abstractmethod
    def to_dict(self):
        pass