from abc import ABC, abstractstaticmethod
from house import House

class Builder(ABC):
    @abstractstaticmethod
    def build_roof(self, has_roof):
        pass

    abstractstaticmethod
    def build_walls(self, walls):
        pass

    abstractstaticmethod
    def build_pool(self, has_pool):
        pass

    abstractstaticmethod
    def build_doors(self, doors):
        pass

    abstractstaticmethod
    def with_color(self, color):
        pass

    abstractstaticmethod
    def build(self):
        pass