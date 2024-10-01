class User:
    def __init__(self, user_name: str, email: str, age: int):
        """Constructor for User"""
        self.user_name = user_name
        self.email = email
        self.age = age

    def __str__(self):
        return f"User(userName='{self.user_name}', email='{self.email}', age={self.age})"

    # Hàm setter và getter cho user_name
    def set_user_name(self, user_name: str):
        self.user_name = user_name

    def get_user_name(self) -> str:
        return self.user_name

    def set_email(self, email: str):
        self.email = email

    def get_email(self) -> str:
        return self.email

    def set_age(self, age: int):
        self.age = age

    def get_age(self) -> int:
        return self.age
