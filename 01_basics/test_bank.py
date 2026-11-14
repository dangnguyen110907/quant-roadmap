import runpy

bank_mod = runpy.run_path("01_basics/bank.py")
value = bank_mod["value"]

def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("Hello, Newman") == 0
    assert value("  HELLO world  ") == 0

def test_h():
    assert value("Hey") == 20
    assert value("hi there") == 20
    assert value("how's it going?") == 20

def test_other():
    assert value("What's up?") == 100
    assert value("Good morning") == 100
    assert value("Xin chào") == 100
