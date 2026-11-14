import json
import os
import runpy

mod = runpy.run_path("02_data_io/clean_stock_data.py")
load_csv = mod["load_csv"]
clean_data = mod["clean_data"]
export_json = mod["export_json"]

def test_load_csv():
    # File có thật: phải đọc được 8 dòng
    records = load_csv("02_data_io/vcb_prices.csv")
    assert isinstance(records, list)
    assert len(records) == 8

    # File không có thật: không được sập chương trình, trả về []
    empty = load_csv("02_data_io/file_khong_ton_tai.csv")
    assert empty == []

def test_clean_data():
    raw = [
        {"Date": "2026-01-02", "Close": "92.0", "Volume": "1500000"},
        {"Date": "2026-01-06", "Close": "CORRUPT", "Volume": "980000"},
        {"Date": "2026-01-08", "Close": "", "Volume": "1450000"},
        {"Date": "2026-01-12", "Close": "-99.0", "Volume": "1600000"},
        {"Date": "2026-01-13", "Close": "96.5", "Volume": "2300000"},
    ]
    cleaned, errors = clean_data(raw)
    
    # Phải lọc được 2 dòng sạch (2026-01-02 và 2026-01-13)
    assert len(cleaned) == 2
    # Phải bắt được 3 dòng lỗi
    assert errors == 3
    
    # Kiểm tra kiểu dữ liệu của dòng sạch: Close phải là float, Volume phải là int
    assert isinstance(cleaned[0]["Close"], float)
    assert isinstance(cleaned[0]["Volume"], int)
    assert cleaned[0]["Close"] == 92.0
    assert cleaned[0]["Volume"] == 1500000

def test_export_json(tmp_path):
    test_data = [{"Date": "2026-01-02", "Close": 92.0, "Volume": 1500000}]
    out_file = str(tmp_path / "test_out.json")
    
    res = export_json(test_data, out_file)
    assert res is True
    assert os.path.exists(out_file)
    
    with open(out_file, "r", encoding="utf-8") as f:
        loaded = json.load(f)
    assert loaded == test_data
