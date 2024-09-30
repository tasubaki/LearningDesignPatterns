from abc import ABC, abstractstaticmethod

class Laptop(ABC):
    @abstractstaticmethod
    def get_segment(self):
        pass