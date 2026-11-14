"""
LỘ TRÌNH QUANT & DATA SCIENCE - MODULE 2 (STEP 3)
Bài toán thực chiến: Đọc CSV giá cổ phiếu, làm sạch dữ liệu, bắt lỗi và xuất JSON.

Yêu cầu theo lộ trình:
Chương trình được chia nhỏ thành đúng 3 HÀM CỐT LÕI:
1. load_csv(filepath): Đọc file CSV, bắt lỗi nếu file không tồn tại.
2. clean_data(raw_records): Duyệt từng dòng, ép kiểu dữ liệu, loại bỏ dòng hỏng/thiếu/giá âm.
3. export_json(data, output_filepath): Ghi dữ liệu sạch ra file JSON.
"""

import csv
import json
import sys

def load_csv(filepath: str) -> list[dict]:
    try:
        with open(filepath, "r") as f:
            reader = csv.DictReader(f)
            return list(reader)
    except FileNotFoundError:
        return []


def clean_data(raw_records: list[dict]) -> tuple[list[dict], int]:
    cleaned = []
    errors = 0
    for row in raw_records:
        try:
            close = float(row["Close"])
            volume = int(row["Volume"])
            if close <= 0 or volume < 0:
                raise ValueError
            else:
                row["Close"] = close
                row["Volume"] = volume
                cleaned.append(row)
        except (ValueError, KeyError):
            errors += 1
    return cleaned, errors


def export_json(data: list[dict], output_filepath: str) -> bool:
    with open(output_filepath, "w") as f:
        json.dump(data, f, indent=4)
    try:
        with open(output_filepath, "r") as f:
            return True
    except FileNotFoundError:
        return False


def main():
    input_file = "02_data_io/vcb_prices.csv"
    output_file = "02_data_io/vcb_cleaned.json"

    print(f"1. Đang đọc file: {input_file}...")
    records = load_csv(input_file)
    print(f"   -> Đã đọc {len(records)} dòng thô.")

    print("2. Đang làm sạch dữ liệu...")
    clean_records, error_count = clean_data(records)
    print(
        f"   -> Giữ lại {len(clean_records)} dòng hợp lệ, đã loại bỏ {error_count} dòng lỗi."
    )

    print(f"3. Đang xuất ra file JSON: {output_file}...")
    success = export_json(clean_records, output_file)
    if success:
        print("✅ Hoàn tất toàn bộ quy trình!")


if __name__ == "__main__":
    main()
