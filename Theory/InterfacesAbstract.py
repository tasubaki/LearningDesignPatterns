from abc import ABC, abstractstaticmethod

class  IPerson(ABC):
    @abstractstaticmethod
    def person_method():
        """ Interfact Method"""

class Student(IPerson):

    def __init__(self) -> None:
        self.name = "Basic Student name"

    def person_method(self):
        print("I am a student")

class Teacher(IPerson):

    def __init__(self) -> None:
        self.name = "Basic teacher name"

    def person_method(self):
        print("I am a teacher")

class PersonFactory:

    @staticmethod
    def build_person(person_type):
        if person_type == "Student":
            return Student()
        if person_type == "Teacher":
            return Teacher()
        print("Invalid Type")
        return -1


if __name__ == "__main__":
    choice = input("What type of person do you want to create?\n")
    person = PersonFactory.build_person(choice)
    person.person_method()