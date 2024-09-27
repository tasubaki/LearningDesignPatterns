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


# Test the Singleton
if __name__ == "__main__":
    eager1 = EagerInitialization()
    eager1.set_name("John")
    print(eager1.get_name())

    eager2 = EagerInitialization()
    print(eager2.get_name())        # Dù có bao nhiêu lần gọi EagerInitialization, vẫn chỉ có một instance duy nhất được trả về.
