class SinhVien:
    def __init__(self, student_id, name, gpa):
        self.student_id = student_id
        self.name = name
        self.gpa = gpa

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, GPA: {self.gpa}"
    