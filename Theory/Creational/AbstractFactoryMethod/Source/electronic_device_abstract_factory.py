from abc import ABC, abstractstaticmethod


class ElectronicDeviceAbstractFactory(ABC):
    @abstractstaticmethod
    def create_laptop(self):
        pass

    @abstractstaticmethod
    def create_phone(self):
        pass