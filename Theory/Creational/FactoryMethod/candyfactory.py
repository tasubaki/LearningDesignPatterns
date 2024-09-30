from candytype import CandyType
from hardcandy import HardCandy
from mintycandy import MityCandy

class CandyFactory:
    candy_map = {
        CandyType.MINTY_CANDY: MityCandy,
        CandyType.HARD_CANDY: HardCandy
    }

    @staticmethod
    def get_candy(candy_type: CandyType):
        if candy_type in CandyFactory.candy_map:
            return CandyFactory.candy_map[candy_type]()
        else:
            raise ValueError("This candy type is unsupported")