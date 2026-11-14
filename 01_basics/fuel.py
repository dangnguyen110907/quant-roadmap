"""
CS50P - Problem Set 3: Fuel Gauge
https://cs50.harvard.edu/python/psets/3/fuel/

Mục tiêu:
Luyện tập bắt ngoại lệ: ValueError, ZeroDivisionError và vòng lặp while True.
"""


def main():
    while True:
        try:
            Fraction = input("Hãy nhập số(ví dụ 3/4): ")
            x, y = Fraction.split("/")
            x = int(x)
            y = int(y)
            if x < 0 or y <= 0 or x > y:
                raise ValueError
            percent = round(float(x / y) * 100)
            if percent <= 1:
                print("E")
            elif percent >= 99:
                print("F")
            else:
                print(f"{percent}%")

            break
        except (ValueError, ZeroDivisionError):
            print("vui long nhap lại")


if __name__ == "__main__":
    main()
