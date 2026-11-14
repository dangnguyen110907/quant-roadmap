"""
CS50P - Problem Set 2: Just setting up my twttr
https://cs50.harvard.edu/python/psets/2/twttr/

Yêu cầu:
Hoàn thiện hàm shorten(word):
- Nhận vào chuỗi word (ví dụ: "Twitter")
- Trả về chuỗi mới đã bỏ hết các nguyên âm (a, e, i, o, u cả thường lẫn hoa)
"""


def main():
    text = input("Input: ")
    print(f"Output: {shorten(text)}")


def shorten(word: str) -> str:
    return "".join([char for char in word if char.lower() not in "ueoai"])


if __name__ == "__main__":
    main()
