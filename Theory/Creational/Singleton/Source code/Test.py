from abc import ABC, abstractstaticmethod

class EagerInitialization:
    # Tạo instance từ đầu khi chương trình bắt đầu
    _instance = None

    """
    Python sử dụng phương thức __new__ thay vì constructor để đảm bảo chỉ có một instance duy nhất được tạo. 
    Điều này giống với việc Eager Initialization trong Java đảm bảo instance được tạo ngay từ đầu.
    """
    def __new__(cls):
        if cls._instance is None:
            # Chỉ tạo instance duy nhất
            cls._instance = super(EagerInitialization, cls).__new__(cls)
            cls._instance.name = None
        return cls._instance

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name


class IPerson(ABC):
    @abstractstaticmethod
    def print_data():
        """ Implement in child class"""

class PersonSingleton(IPerson):
    """Biến này là name mangling(tức là _PersonSingleton__instance). Biến này được coi là private và sẽ 
    không thể truy cập từ bên ngoài class một cách trực tiếp (ví dụ: object.__instance sẽ gây lỗi)."""
    __instance = None

    def __init__(self, name: str, age: int) -> None:
        if PersonSingleton.__instance is not None:
            raise Exception("Singleton cannot be instantiated more than once!")
        else:
            self.name = name
            self.age = age
            PersonSingleton.__instance = self

    @staticmethod
    # Lazy design patterns
    def get_instance():
        if PersonSingleton.__instance is None:
            PersonSingleton("Default Name", 0)
        return PersonSingleton.__instance

    @staticmethod
    def print_data():
        print(f"Name: {PersonSingleton.__instance.name}, Age: {PersonSingleton.__instance.age}")

# Test the Singleton
if __name__ == "__main__":
    eager1 = EagerInitialization()
    eager1.set_name("John")
    print(eager1.get_name())

    eager2 = EagerInitialization()
    print(eager2.get_name())        # Dù có bao nhiêu lần gọi EagerInitialization, vẫn chỉ có một instance duy nhất được trả về.
    

    #test2 
    test2 = PersonSingleton("taki", 12)
    print(test2)
    test2.print_data()

    #test = PersonSingleton("a", 12)
    test = PersonSingleton.get_instance()
    print(test)
    test.print_data()