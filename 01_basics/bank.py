"""
CS50P - Problem Set 1: Home Federal Savings Bank
https://cs50.harvard.edu/python/psets/1/bank/

Yêu cầu:
Hoàn thiện hàm value(greeting):
- Nhận vào chuỗi greeting (ví dụ: "Hello", "  hello world  ", "Hey", "What's up")
- Trả về số nguyên int: 0, 20, hoặc 100
"""


def main():
    greeting = input("Lời chào: ")
    print(f"${value(greeting)}")


def value(greeting: str) -> int:
    greeting = greeting.strip().lower()
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
