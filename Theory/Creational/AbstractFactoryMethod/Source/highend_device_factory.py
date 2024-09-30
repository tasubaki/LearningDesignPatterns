from electronic_device_abstract_factory import ElectronicDeviceAbstractFactory
from highend_laptop import HighEndLaptop
from highend_phone import HighEndPhone

class HighEndDeviceFactory(ElectronicDeviceAbstractFactory):
    def create_laptop(self):
        return HighEndLaptop()
    
    def create_phone(self):
        return HighEndPhone()