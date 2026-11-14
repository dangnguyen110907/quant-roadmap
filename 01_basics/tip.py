"""
CS50P - Problem Set 0: Tip Calculator
Đề bài gốc của Harvard CS50P:
https://cs50.harvard.edu/python/psets/0/tip/

Mục tiêu:
Luyện tập bóc tách chuỗi (string manipulation), ép kiểu float, và hàm return.
"""

def main():
    dollars = dollars_to_float(input("Bữa ăn hết bao nhiêu tiền? (ví dụ $50.00): "))
    percent = percent_to_float(input("Bạn muốn tip bao nhiêu phần trăm? (ví dụ 15%): "))
    
    tip = dollars * percent
    print(f"Tiền tip cần trả là: ${tip:.2f}")


def dollars_to_float(d: str) -> float:
    d=d.replace("$", "")
    return float(d)


def percent_to_float(p: str) -> float:
    p=p.replace("%", "")
    return float(p)/100


if __name__ == "__main__":
    main()
