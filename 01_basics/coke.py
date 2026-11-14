"""
CS50P - Problem Set 2: Coke Machine
https://cs50.harvard.edu/python/psets/2/coke/

Mục tiêu:
Luyện tập vòng lặp while, câu lệnh điều kiện if, và toán tử cộng dồn.
"""


def main():
    amount_due = 50
    valid_coins = [25, 10, 5]
    while amount_due > 0:
        print(f"amount_due: {amount_due}")
        coin = int(input("insert_coin: "))
        if coin in valid_coins:
            amount_due -= coin
    change = abs(amount_due)
    print(f"Change Owed: {change}")


if __name__ == "__main__":
    main()
