import runpy

tip_mod = runpy.run_path("01_basics/tip.py")
dollars_to_float = tip_mod["dollars_to_float"]
percent_to_float = tip_mod["percent_to_float"]

def test_dollars():
    assert dollars_to_float("$50.00") == 50.0
    assert dollars_to_float("$0.50") == 0.50
    assert dollars_to_float("$1000.00") == 1000.0

def test_percent():
    assert percent_to_float("15%") == 0.15
    assert percent_to_float("0%") == 0.0
    assert percent_to_float("100%") == 1.0
