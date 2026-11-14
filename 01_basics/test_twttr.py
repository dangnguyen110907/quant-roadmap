import runpy

twttr_mod = runpy.run_path("01_basics/twttr.py")
shorten = twttr_mod["shorten"]

def test_lowercase():
    assert shorten("twitter") == "twttr"

def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"

def test_mixed():
    assert shorten("What's your name?") == "Wht's yr nm?"

def test_numbers_and_punctuation():
    assert shorten("CS50, 2026!") == "CS50, 2026!"
