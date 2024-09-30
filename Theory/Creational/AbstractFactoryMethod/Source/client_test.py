from electronic_device_factory import ElectronicDeviceFactory, Segment

def main():
    """ high_end_device_factory = ElectronicDeviceFactory.get_factory(Segment.HIGH_END)
    high_end_laptop = high_end_device_factory.create_laptop()
    high_end_phone = high_end_device_factory.create_phone()

    print(high_end_laptop.get_segment())
    print(high_end_phone.get_segment())

    print("=========================")

    # Mid-range device factory
    mid_range_device_factory = ElectronicDeviceFactory.get_factory(Segment.MID_RANGE)
    mid_range_laptop = mid_range_device_factory.create_laptop()
    mid_range_phone = mid_range_device_factory.create_phone()

    print(mid_range_laptop.get_segment())
    print(mid_range_phone.get_segment()) """


    # Hướng dẫn người dùng nhập loại thiết bị
    print("Vui lòng chọn loại thiết bị (nhập 'high' cho High-End hoặc 'mid' cho Mid-Range): ")
    user_input = input().strip().lower()

    # Chuyển đổi giá trị người dùng nhập thành segment
    if user_input == 'high':
        segment = Segment.HIGH_END
    elif user_input == 'mid':
        segment = Segment.MID_RANGE
    else:
        print("Lựa chọn không hợp lệ!")
        return  # Dừng chương trình nếu nhập sai

    # Nhận factory dựa trên giá trị người dùng nhập
    device_factory = ElectronicDeviceFactory.get_factory(segment)

    # Tạo và in thông tin của Laptop và Phone
    laptop = device_factory.create_laptop()
    phone = device_factory.create_phone()

    print("Thông tin thiết bị bạn chọn:")
    print(f"Laptop: {laptop.get_segment()}")
    print(f"Phone: {phone.get_segment()}")

    
if __name__ == "__main__":
    main()