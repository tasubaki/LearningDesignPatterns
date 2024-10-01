from house_builder import HouseBuilder

def get_user_input():
    # Hỏi người dùng các thông số để xây dựng nhà
    walls = int(input("Enter the number of walls: "))
    doors = int(input("Enter the number of doors: "))
    has_roof = input("Do you want a roof? (yes/no): ").strip().lower() == "yes"
    has_pool = input("Do you want a pool? (yes/no): ").strip().lower() == "yes"
    color = input("Enter the color of the house: ")

    return walls, doors, has_roof, has_pool, color

if __name__ == "__main__":
    """ # Sử dụng builder để tạo ra đối tượng House
    house1 = (HouseBuilder()
              .build_doors(5)
              .build_roof(True)
              .build_pool(True)
              .build_walls(4)
              .with_color("Blue")
              .build())
    
    print(house1) """


    # Lấy thông tin từ người dùng
    walls, doors, has_roof, has_pool, color = get_user_input()

    # Sử dụng builder để xây dựng đối tượng House
    house = (HouseBuilder()
             .build_walls(walls)
             .build_doors(doors)
             .build_roof(has_roof)
             .build_pool(has_pool)
             .with_color(color)
             .build())
    
    # In ra kết quả cuối cùng
    print(house)