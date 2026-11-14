import runpy

mod = runpy.run_path("01_basics/market_filter.py")
filter_gainers = mod["filter_gainers"]

def test_mixed_stocks():
    stocks = [
        {"symbol": "VCB", "change": 1.2},
        {"symbol": "HPG", "change": -0.5},
        {"symbol": "FPT", "change": 2.1},
        {"symbol": "MWG", "change": -1.0},
    ]
    assert filter_gainers(stocks) == ["VCB", "FPT"]

def test_all_loss():
    stocks = [
        {"symbol": "A", "change": -1.0},
        {"symbol": "B", "change": -0.1},
    ]
    assert filter_gainers(stocks) == []

def test_zero_change():
    # change == 0 thì không tính là tăng giá
    stocks = [
        {"symbol": "A", "change": 0.0},
        {"symbol": "B", "change": 0.5},
    ]
    assert filter_gainers(stocks) == ["B"]

def test_empty():
    assert filter_gainers([]) == []
