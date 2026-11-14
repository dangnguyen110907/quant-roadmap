"""
MODULE 3: NUMPY & PANDAS (STEP 5)
Làm sạch dữ liệu Bitcoin 1 năm và viết hàm Báo cáo chất lượng dữ liệu.
"""

import pandas as pd


def data_quality_report(df: pd.DataFrame) -> None:
    """Hàm 1: Báo cáo chất lượng dữ liệu.

    In ra:
    - Tổng số dòng và số cột của bảng: df.shape
    - Số dòng bị trùng lặp: df.duplicated().sum()
    - Số ô bị thiếu (NaN) ở từng cột: df.isna().sum()
    - Kiểu dữ liệu của các cột: df.dtypes
    """
    print("=== BÁO CÁO CHẤT LƯỢNG DỮ LIỆU ===")
    print(f"Tổng số dòng và cột của bảng: {df.shape}")
    print(f"Số dòng bị trung lặp: {df.duplicated().sum()}")
    print(f"Số ô bị thiếu: {df.isna().sum()}")
    print(f"kiểu dữ liêu của các cột: {df.dtypes}")


def clean_btc_data(df: pd.DataFrame) -> pd.DataFrame:
    """Hàm 2: Làm sạch toàn diện bảng dữ liệu.

    1. Xoá dòng trùng lặp: df.drop_duplicates()
    2. Ép cột 'Date' sang datetime: pd.to_datetime(...)
    3. Ép cột 'Volume' và 'Close' sang số thực float: pd.to_numeric(..., errors='coerce')
    4. Xoá các dòng chứa ô trống: df.dropna()
    Trả về DataFrame sạch.
    """
    df = df.drop_duplicates()
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df["Volume"] = pd.to_numeric(df["Volume"], errors="coerce")
    df["Close"] = pd.to_numeric(df["Close"], errors="coerce")
    df = df.dropna()
    return df





def main():
    raw_path = "04_numpy_pandas/btc_1year_raw.csv"
    print(f"1. Đang đọc dữ liệu từ: {raw_path}...")
    df = pd.read_csv(raw_path)

    print("\n2. Kiểm tra chất lượng dữ liệu THÔ ban đầu:")
    data_quality_report(df)

    print("\n3. Tiến hành làm sạch dữ liệu...")
    df_cleaned = clean_btc_data(df)

    print("\n4. Kiểm tra lại chất lượng dữ liệu SAU KHI LÀM SẠCH:")
    data_quality_report(df_cleaned)

    # Xuất ra file CSV sạch (bỏ cột index mặc định)
    out_path = "04_numpy_pandas/btc_1year_cleaned.csv"
    df_cleaned.to_csv(out_path, index=False)
    print(f"\n✅ Đã lưu dữ liệu sạch ra: {out_path}")


if __name__ == "__main__":
    main()
