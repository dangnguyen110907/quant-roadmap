"""
CS50P Week 2: List of Dictionaries
Luyện tập bóc tách dữ liệu từ danh sách các Dictionary (nền tảng của Data Science).

Yêu cầu:
Hoàn thiện hàm filter_gainers(stocks):
- Nhận vào: danh sách các dictionary (mỗi dict có key 'symbol' và 'change')
- Trả về: một list các chuỗi (str) là tên các mã có 'change' > 0
"""


def main():
    sample_stocks = [
        {"symbol": "VCB", "price": 92.5, "change": 1.2},
        {"symbol": "HPG", "price": 27.8, "change": -0.5},
        {"symbol": "FPT", "price": 136.0, "change": 2.1},
        {"symbol": "MWG", "price": 49.5, "change": -1.0},
    ]
    gainers = filter_gainers(sample_stocks)
    print(f"Các mã tăng giá: {gainers}")


def filter_gainers(stocks: list[dict]) -> list[str]:
    return[s["symbol"] for s in stocks if s.get("change", 0) > 0]


if __name__ == "__main__":
    main()
