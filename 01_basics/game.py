"""
CS50P - Problem Set 4: Guessing Game
https://cs50.harvard.edu/python/psets/4/game/

Mục tiêu:
Luyện tập thư viện random (random.randint), bắt ngoại lệ ValueError và điều khiển vòng lặp.
"""

import random

from tomlkit import value


def main():
    while True:
        try:
            n = input("Hãy chọn level(ví dụ 5, 6, 50, 100,...): ")
            n = int(n)
            if n < 0:
                raise ValueError
            break
        except ValueError:
            print("hãy nhập lại n")
    secret = random.randint(0, n)
    while True:
        try:
            guess = int(input("Hãy đoán một số: "))
            if guess == secret:
                print("Just right!")
                break
            elif guess > secret:
                print("Too large!")
            else:
                print("Too small!")
        except ValueError:
            print("hãy nhập số nguyên")


if __name__ == "__main__":
    main()
