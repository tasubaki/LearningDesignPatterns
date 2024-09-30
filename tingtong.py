from threading import Thread, Lock
from typing import Any, Callable, Iterable, Mapping

# Định nghĩa lớp MyThread kế thừa từ Thread
class MyThread(Thread):
    def __init__(self, target: Callable[..., Any], args: Iterable[Any] = (), kwargs: Mapping[str, Any] = None) -> None:
        super().__init__(target=target, args=args, kwargs=kwargs)
        self.result = 0  # Biến lưu trữ kết quả tính toán

    # Để trả về kết quả
    def get_result(self) -> int:
        return self.result

# Hàm tính tổng từ start đến end
def compute_sum(start: int, end: int, lock: Lock, total: list) -> None:
    local_total = 0  # Tổng cục bộ cho luồng này
    for i in range(start, end + 1):
        local_total += i
    
    # Sử dụng lock để đảm bảo không có tranh chấp khi cập nhật total
    with lock:
        total[0] += local_total

# Hàm tính tổng với đa luồng
def calculate_sum_with_threads(n: int) -> int:
    num_threads = 4  # Số lượng luồng
    threads = []
    total = [0]  # Sử dụng danh sách để lưu trữ tổng, cho phép chia sẻ giữa các luồng
    lock = Lock()  # Khóa để bảo vệ tổng

    # Chia n thành các khoảng cho từng luồng
    step = n // num_threads
    for i in range(num_threads):
        start = i * step + 1
        end = (i + 1) * step if i < num_threads - 1 else n
        thread = MyThread(target=compute_sum, args=(start, end, lock, total))
        threads.append(thread)
        thread.start()  # Bắt đầu luồng

    # Chờ tất cả các luồng hoàn thành
    for thread in threads:
        thread.join()  # Chờ luồng hoàn thành

    return total[0]  # Trả về tổng đã tính

# Nhập số n từ người dùng
n = int(input("Nhập số n: "))

# Tính tổng bằng đa luồng
result = compute_sum(n)
print(f"Tổng từ 1 đến {n} là: {result}")
