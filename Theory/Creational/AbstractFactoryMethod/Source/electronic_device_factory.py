from midrange_device_factory import MidRangeDeviceFactory
from highend_device_factory import HighEndDeviceFactory

class Segment:
    HIGH_END = "HIGH_END"
    MID_RANGE = "MID_RANGE"


class ElectronicDeviceFactory:
    @staticmethod
    def get_factory(segment):
        if segment == Segment.HIGH_END:
            return HighEndDeviceFactory()
        elif segment == Segment.MID_RANGE:
            return MidRangeDeviceFactory()
        else:
            raise NotImplementedError("This device is unsupported") 