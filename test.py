from abc import ABC, abstractmethod

# Lớp trừu tượng
class Student(ABC):
    def intro(self):
        print("Tôi là học sinh và đây là bài tập về nhà của tôi:")

    @abstractmethod
    def do_homework(self):
        pass

# Học sinh tiểu học
class PrimaryStudent(Student):
    def do_homework(self):
        print("Tôi làm bài tập cộng trừ đơn giản.")

# Học sinh cấp 3
class HighSchoolStudent(Student):
    def do_homework(self):
        print("Tôi làm bài tập toán nâng cao.")

class PersonFactory:

    @staticmethod
    def build_person(person_type):
        if person_type == "Student 1":
            return PrimaryStudent()
        if person_type == "Teacher 3":
            return HighSchoolStudent()
        print("Invalid Type")
        return -1


if __name__ == "__main__":
    choice = input("What type of level do you want to create?\n")
    person = PersonFactory.build_person(choice)
    person.do_homework()