from cloneable import CloneableUser

def get_user_input() -> CloneableUser:
    """Tương tác với người dùng để tạo User"""
    user_name = input("Nhập tên người dùng: ")
    email = input("Nhập email: ")
    age = int(input("Nhập tuổi: "))
    return CloneableUser(user_name, email, age)

def main():
    user1 = get_user_input()  # Tạo đối tượng User từ bàn phím
    print("User 1:", user1)

    # Clone user1 sang user2
    user2 = user1.clone()
    print("User 2 (clone):", user2)

    print("==================")

    # Cập nhật tuổi của user1
    new_age = int(input("Nhập tuổi mới cho User 1: "))
    user1.set_age(new_age)

    print("User 1 sau khi cập nhật:", user1)
    print("User 2 (clone, không bị thay đổi):", user2)

if __name__ == "__main__":
    main()
