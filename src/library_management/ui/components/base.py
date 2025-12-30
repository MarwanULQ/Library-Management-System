from abc import ABC, abstractmethod

class BaseComponent(ABC):
    @abstractmethod
    def render(self):
        pass
