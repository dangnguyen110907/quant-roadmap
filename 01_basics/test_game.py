import os
import subprocess
import sys

def run_game(inputs: list[str]) -> str:
    input_str = "\n".join(inputs) + "\n"
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    res = subprocess.run(
        [sys.executable, "01_basics/game.py"],
        input=input_str,
        capture_output=True,
        text=True,
        encoding="utf-8",
        env=env,
    )
    return res.stdout

def test_level_one_direct_guess():
    # Level 1 thì số bí mật chắc chắn là 1
    # Nhập: Level 1, Đoán 1 -> Phải in ra "Just right!"
    output = run_game(["1", "1"])
    assert "Just right!" in output

def test_too_small_and_too_large():
    # Khi dùng python -c patch random để số bí mật luôn là 5
    script = """
import random
random.randint = lambda a, b: 5
import runpy
runpy.run_path('01_basics/game.py', run_name='__main__')
"""
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    res = subprocess.run(
        [sys.executable, "-c", script],
        input="10\n2\n8\n5\n",
        capture_output=True,
        text=True,
        encoding="utf-8",
        env=env,
    )
    # Đoán 2 -> Too small!
    assert "Too small!" in res.stdout
    # Đoán 8 -> Too large!
    assert "Too large!" in res.stdout
    # Đoán 5 -> Just right!
    assert "Just right!" in res.stdout

def test_invalid_level_and_guesses():
    # Level: nhập rác ("cat", "-5", "0"), rồi mới nhập 1
    # Guess: nhập rác ("dog", "-1", "0"), rồi mới nhập 1
    output = run_game(["cat", "-5", "0", "1", "dog", "-1", "0", "1"])
    assert "Just right!" in output
