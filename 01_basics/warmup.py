"""
BÀI KHỞI ĐỘNG (WARM-UP): KÍCH HOẠT LẠI PHẢN XẠ PYTHON

Mục tiêu:
1. Nhớ lại cách định nghĩa hàm (def), nhận tham số và return kết quả.
2. Làm quen với Type Hinting (viết code chuẩn chỉ như kỹ sư).
3. Thao tác với List và Dictionary (2 cấu trúc dữ liệu xuất hiện 90% khi làm Data).
4. Vòng lặp for và tính toán đơn giản.

Đề bài:
Bạn có danh sách các lệnh mua/bán cổ phiếu như dưới đây.
Hãy hoàn thiện 2 hàm:
1. calculate_pnl(buy_price, sell_price): Tính % lãi/lỗ của một lệnh.
   Công thức: ((sell_price - buy_price) / buy_price) * 100
2. summarize_trades(trades): Duyệt qua danh sách lệnh, in ra mã nào lãi, mã nào lỗ và % tương ứng.
"""

# Dữ liệu mẫu (Danh sách các dictionary)
sample_trades = [
    {"symbol": "VCB", "buy": 90.0, "sell": 95.5},
    {"symbol": "HPG", "buy": 28.0, "sell": 26.5},
    {"symbol": "FPT", "buy": 120.0, "sell": 138.0},
    {"symbol": "MWG", "buy": 50.0, "sell": 50.0},
]


def calculate_pnl(buy_price: float, sell_price: float) -> float:
    """Tính % lợi nhuận (lãi/lỗ) từ giá mua và giá bán.

    Trả về số thực (float) làm tròn 2 chữ số thập phân.
    """
    # TODO: Viết code tính toán ở đây
    pass


def summarize_trades(trades: list[dict]) -> None:
    """Duyệt qua từng trade và in ra kết quả định dạng:

    - VCB: +6.11% (Lãi)
    - HPG: -5.36% (Lỗ)
    - MWG: 0.00% (Hoà vốn)
    """
    # TODO: Viết vòng lặp for ở đây
    pass


if __name__ == "__main__":
    print("--- KẾT QUẢ GIAO DỊCH ---")
    summarize_trades(sample_trades)
