from abc import ABC, abstractmethod


class Entity(ABC):
    @abstractmethod
    def from_dict(cls: object, dict: dict):
        pass

    @abstractmethod
    def to_dict(self: object):
        pass