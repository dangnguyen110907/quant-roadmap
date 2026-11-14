"""
BỘ KIỂM THỬ CHO BÀI LÀM SẠCH DỮ LIỆU BTC (MODULE 3)
"""

import sys
import os
import pandas as pd

sys.path.append(os.path.abspath("04_numpy_pandas"))
from data_cleaning import clean_btc_data


def test_clean_btc_data():
    df_raw = pd.read_csv("04_numpy_pandas/btc_1year_raw.csv")
    df_clean = clean_btc_data(df_raw)

    # 1. Bảng sạch không được có bất kỳ dòng trùng lặp nào
    assert df_clean.duplicated().sum() == 0

    # 2. Bảng sạch không được có bất kỳ ô trống (NaN) nào
    assert df_clean.isna().sum().sum() == 0

    # 3. Kiểu dữ liệu cột Date phải là datetime
    assert pd.api.types.is_datetime64_any_dtype(df_clean["Date"])

    # 4. Kiểu dữ liệu cột Close và Volume phải là số (float/int)
    assert pd.api.types.is_numeric_dtype(df_clean["Close"])
    assert pd.api.types.is_numeric_dtype(df_clean["Volume"])

    # 5. Ban đầu 367 dòng, sau khi trừ 2 trùng + 1 thiếu close + 1 rác volume -> còn đúng 363 dòng
    assert len(df_clean) == 363
