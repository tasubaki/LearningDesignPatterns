from candyfactory import CandyFactory
from candytype import CandyType

def main():
    print("Select candy type:")
    print("1. Minty Candy")
    print("2. Hard Candy")
    
    choice = int(input("Enter your choice (1 or 2): "))
    
    if choice == 1:
        candy_type = CandyType.MINTY_CANDY
    elif choice == 2:
        candy_type = CandyType.HARD_CANDY
    else:
        print("Invalid choice")
        return
    
    candy = CandyFactory.get_candy(candy_type)
    print(f"You got: {candy.get_candy_name()}")

if __name__ == "__main__":
    main()