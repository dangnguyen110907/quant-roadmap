"""
CS50P - Problem Set 2: Nutrition Facts
https://cs50.harvard.edu/python/psets/2/nutrition/

Mục tiêu:
Luyện tập cấu trúc dữ liệu Dictionary (dict):
1. Tra cứu xem một Key có nằm trong dict không (dùng toán tử 'in').
2. Lấy giá trị (Value) tương ứng từ Key: dict_name[key].
"""

# Dữ liệu bảng FDA (đã tạo sẵn toàn bộ chữ thường để dễ tra cứu)
FRUITS = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plums": 70,
    "strawberries": 50,
    "sweet cherries": 100,
    "tangerine": 50,
    "watermelon": 80,
}


def main():
    item = input("Item: ").lower()
    if item in FRUITS:
        print(f"Calories: {FRUITS[item]}")


if __name__ == "__main__":
    main()
