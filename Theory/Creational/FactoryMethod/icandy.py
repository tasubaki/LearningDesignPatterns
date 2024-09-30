from abc import ABC, abstractstaticmethod

class Candy(ABC):
    @abstractstaticmethod
    def get_candy_name():
        pass