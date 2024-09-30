from abc import ABC, abstractstaticmethod

class Phone(ABC):
    @abstractstaticmethod
    def get_segment(self):
        pass