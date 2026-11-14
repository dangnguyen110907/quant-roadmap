import sys

print("Toàn bộ danh sách sys.argv hiện tại:", sys.argv)
print("Số lượng phần tử trong sys.argv:", len(sys.argv))

if len(sys.argv) < 2:
    sys.exit("⚠️ Lỗi: Bạn chưa truyền tham số nào! Hãy thử chạy: python 01_basics/demo_sys.py FPT")

print(f"✅ Tuyệt vời! Tham số bạn vừa truyền là: {sys.argv[1]}")
