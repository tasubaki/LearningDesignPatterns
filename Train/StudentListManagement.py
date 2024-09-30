"""
Bài toán quản lý sinh viên
Yêu cầu: các chức năng sau:

1. Thêm sinh viên.
2. Cập nhật thông tin sinh viên bởi ID.
3. Xóa sinh viên bởi ID.
4. Tìm kiếm sinh viên theo tên.
5. Sắp xếp sinh viên theo điểm trung bình (GPA).
6. Sắp xếp sinh viên theo tên.
7. Hiển thị danh sách sinh vien.
8. Ghi danh sách sinh viên vào file "student.txt" .
"""

# Lớp đại diện cho sinh viên
class SinhVien:
    def __init__(self, student_id, name, gpa):
        self.student_id = student_id
        self.name = name
        self.gpa = gpa

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, GPA: {self.gpa}"

# Lớp quản lý sinh viên
class QuanLySinhVien:
    def __init__(self):
        self.students = []

    def them_sinh_vien(self, sinh_vien):
        """Thêm sinh viên vào danh sách"""
        self.students.append(sinh_vien)

    def cap_nhat_sinh_vien(self, student_id, name=None, gpa=None):
        """Cập nhật thông tin sinh viên theo ID"""
        for sv in self.students:
            if sv.student_id == student_id:
                if name:
                    sv.name = name
                if gpa:
                    sv.gpa = gpa
                return sv
        print("Không tìm thấy sinh viên")
        return None

    def xoa_sinh_vien(self, student_id):
        """Xóa sinh viên theo ID"""
        self.students = [sv for sv in self.students if sv.student_id != student_id]

    def tim_kiem_theo_ten(self, name):
        """Tìm sinh viên theo tên"""
        return [sv for sv in self.students if sv.name == name]

    def sap_xep(self, strategy):
        """Sắp xếp sinh viên dựa trên một chiến lược được truyền vào"""
        if hasattr(strategy, 'sap_xep'):
            self.students = strategy.sap_xep(self.students)
        else:
            raise TypeError("Đối tượng không có phương thức 'sap_xep'.")

    def hien_thi_sinh_vien(self):
        """Hiển thị danh sách sinh viên"""
        for sv in self.students:
            print(sv)

    def ghi_file(self, file_writer):
        """Ghi danh sách sinh viên vào file theo định dạng được chỉ định"""
        if hasattr(file_writer, 'write_file'):
            file_writer.write_file(self.students)
        else:
            raise TypeError("Đối tượng không có phương thức 'write_file'.")

# Lớp sắp xếp theo điểm GPA
class SapXepTheoGPA:
    def sap_xep(self, students):
        return sorted(students, key=lambda x: x.gpa, reverse=True)

# Lớp sắp xếp theo tên
class SapXepTheoTen:
    def sap_xep(self, students):
        return sorted(students, key=lambda x: x.name)

# Lớp ghi file dưới dạng text
class GhiFileText:
    def write_file(self, students):
        with open("students.txt", "w") as f:
            for sv in students:
                f.write(str(sv) + "\n")

# Lớp ghi file dưới dạng CSV
class GhiFileCSV:
    def write_file(self, students):
        with open("students.csv", "w") as f:
            f.write("ID,Name,GPA\n")
            for sv in students:
                f.write(f"{sv.student_id},{sv.name},{sv.gpa}\n")


# Ví dụ sử dụng hệ thống Duck Typing
if __name__ == "__main__":
    quan_ly = QuanLySinhVien()

    # Thêm sinh viên
    quan_ly.them_sinh_vien(SinhVien(1, "Nam", 3.5))
    quan_ly.them_sinh_vien(SinhVien(2, "Linh", 3.8))
    quan_ly.them_sinh_vien(SinhVien(3, "Anh", 2.9))

    # Sắp xếp sinh viên theo GPA
    print("\nSắp xếp theo GPA:")
    quan_ly.sap_xep(SapXepTheoGPA())
    quan_ly.hien_thi_sinh_vien()

    # Sắp xếp sinh viên theo tên
    print("\nSắp xếp theo tên:")
    quan_ly.sap_xep(SapXepTheoTen())
    quan_ly.hien_thi_sinh_vien()

    # Ghi danh sách sinh viên vào file text
    quan_ly.ghi_file(GhiFileText())
    
    quan_ly.xoa_sinh_vien(3)
    
    # Ghi danh sách sinh viên vào file CSV
    quan_ly.ghi_file(GhiFileCSV())

