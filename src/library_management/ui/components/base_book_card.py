from abc import ABC, abstractmethod
from ui.components.base import BaseComponent

class BaseBookCard(BaseComponent, ABC):
    def __init__(self, book):
        self.book = book

    @abstractmethod
    def render(self):
        pass
