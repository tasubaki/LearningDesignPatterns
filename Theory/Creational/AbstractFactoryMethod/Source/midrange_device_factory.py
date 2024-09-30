from electronic_device_abstract_factory import ElectronicDeviceAbstractFactory
from midrange_laptop import MidRangeLaptop
from midrange_phone import MidRangePhone

class MidRangeDeviceFactory(ElectronicDeviceAbstractFactory):
    def create_laptop(self):
        return MidRangeLaptop()
    
    def create_phone(self):
        return MidRangePhone()