import subprocess
import sys

def run_nutrition(user_input: str) -> str:
    res = subprocess.run(
        [sys.executable, "01_basics/nutrition.py"],
        input=user_input + "\n",
        capture_output=True,
        text=True,
    )
    return res.stdout

def test_apple():
    out = run_nutrition("Apple")
    assert "130" in out

def test_lowercase():
    out = run_nutrition("avocado")
    assert "50" in out

def test_multi_word():
    out = run_nutrition("Sweet Cherries")
    assert "100" in out

def test_not_found():
    out = run_nutrition("tomato")
    # Không được in Calories nếu không có trong từ điển
    assert "Calories" not in out
