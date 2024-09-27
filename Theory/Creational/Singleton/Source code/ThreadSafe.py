""" Thread-Safe Singleton (An toàn với đa luồng)
Ý tưởng:

    Đảm bảo rằng đối tượng Singleton chỉ được khởi tạo một lần duy nhất, ngay cả khi có nhiều luồng (threads) đang chạy đồng thời.

Ưu điểm:

    An toàn trong môi trường đa luồng.

Nhược điểm:

    Có thể có chi phí hiệu năng vì sử dụng khóa (lock) trong môi trường đa luồng.
"""
import threading

class SingletonThreadSafe:
    _instance = None
    _lock = threading.Lock()

    @staticmethod
    def get_instance():
        with SingletonThreadSafe._lock:
            if SingletonThreadSafe._instance is None:
                SingletonThreadSafe._instance = "Đối tượng Singleton (An toàn đa luồng)"
        return SingletonThreadSafe._instance

# Sử dụng Singleton
singleton1 = SingletonThreadSafe.get_instance()
singleton2 = SingletonThreadSafe.get_instance()

print(singleton1)  # Kết quả: Đối tượng Singleton (An toàn đa luồng)
print(singleton1 == singleton2)  # Kết quả: True, vì chúng đều là cùng một đối tượng
