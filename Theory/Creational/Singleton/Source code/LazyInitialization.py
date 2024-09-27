"""Lazy Initialization (Khởi tạo khi cần)
Ý tưởng:

    Đối tượng Singleton chỉ được tạo khi thực sự cần, tức là khi lần đầu tiên có yêu cầu truy cập đến nó.

Ưu điểm:

    Tiết kiệm tài nguyên nếu đối tượng Singleton nặng, vì nó chỉ được tạo khi cần.

Nhược điểm:

    Không an toàn trong môi trường đa luồng.
"""
class SingletonLazy:
    _instance = None

    @staticmethod
    def get_instance():
        # Chỉ khởi tạo khi được gọi lần đầu tiên
        if SingletonLazy._instance is None:
            SingletonLazy._instance = "Đây là đối tượng Singleton được khởi tạo khi cần"
        return SingletonLazy._instance

# Sử dụng Singleton
singleton1 = SingletonLazy.get_instance()
singleton2 = SingletonLazy.get_instance()

print(singleton1)  # Kết quả: Đây là đối tượng Singleton được khởi tạo khi cần
print(singleton1 == singleton2)  # Kết quả: True, vì chúng đều là cùng một đối tượng
