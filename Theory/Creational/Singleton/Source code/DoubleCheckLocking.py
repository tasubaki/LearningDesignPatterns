"""Double-Checked Locking (Khóa kiểm tra kép)
Ý tưởng:

    Giống như Thread-Safe, nhưng tránh việc dùng lock quá nhiều lần. Chỉ dùng lock khi đối tượng chưa được khởi tạo, và sau đó kiểm tra lại một lần nữa.

Ưu điểm:

    Tối ưu hóa hơn so với phương pháp Thread-Safe thông thường vì chỉ dùng khóa khi thực sự cần.

Nhược điểm:

    Cách này phức tạp hơn và yêu cầu hiểu biết rõ về đa luồng.
"""
import threading

class SingletonDoubleChecked:
    _instance = None
    _lock = threading.Lock()

    @staticmethod
    def get_instance():
        # Kiểm tra lần đầu (không dùng khóa)
        if SingletonDoubleChecked._instance is None:
            with SingletonDoubleChecked._lock:
                # Kiểm tra lần hai (dùng khóa)
                if SingletonDoubleChecked._instance is None:
                    SingletonDoubleChecked._instance = "Đối tượng Singleton (Kiểm tra kép)"
        return SingletonDoubleChecked._instance

# Sử dụng Singleton
singleton1 = SingletonDoubleChecked.get_instance()
singleton2 = SingletonDoubleChecked.get_instance()

print(singleton1)  # Kết quả: Đối tượng Singleton (Kiểm tra kép)
print(singleton1 == singleton2)  # Kết quả: True, vì chúng đều là cùng một đối tượng
