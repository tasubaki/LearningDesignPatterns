import copy
from user import User

class CloneableUser(User):
    def clone(self):
        """Shallow copy of User object"""
        return copy.deepcopy(self)  # Sử dụng copy để tạo clone
