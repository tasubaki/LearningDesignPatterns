"""Eager Initislizstion( khởi tạo sớm)
Ý tưởng:

    Đối tượng Singleton sẽ được tạo ngay lập tức khi chương trình chạy, bất kể có được sử dụng hay không.

Ưu điểm:

    Đơn giản, dễ triển khai.
    Luôn sẵn sàng khi cần.

Nhược điểm:

    Nếu đối tượng Singleton nặng (tốn nhiều tài nguyên), nó sẽ được tạo ra ngay cả khi không cần đến.
"""

class EagerInitialization:
    _instace = None

    # Khởi tạo ngay lập tức khi class được định nghĩa
    _instance = "This is Singleton"

    @staticmethod
    def get_instance():
        return EagerInitialization
    
if __name__ == "__main__":
    singleton1 = EagerInitialization.get_instance()
    singleton2 = EagerInitialization.get_instance()

    print(singleton1)  
    # Kết quả : <class '__main__.EagerInitialization'> là đối tượng của singleton                 
    print(singleton1 == singleton2)
    # Kết quả: True, vì chúng đều là cùng một đối tượng
    