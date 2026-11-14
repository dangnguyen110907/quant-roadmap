import os
import subprocess
import sys

def run_fuel(inputs: list[str]) -> str:
    input_str = "\n".join(inputs) + "\n"
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    res = subprocess.run(
        [sys.executable, "01_basics/fuel.py"],
        input=input_str,
        capture_output=True,
        text=True,
        encoding="utf-8",
        env=env,
    )
    return res.stdout

def test_percentages():
    assert "75%" in run_fuel(["3/4"])
    assert "25%" in run_fuel(["1/4"])
    assert "50%" in run_fuel(["2/4"])

def test_full_and_empty():
    assert "E" in run_fuel(["0/4"])
    assert "E" in run_fuel(["1/100"])
    assert "F" in run_fuel(["4/4"])
    assert "F" in run_fuel(["99/100"])

def test_zero_division():
    # Nhập 1/0 bị lỗi chia cho 0 -> phải hỏi lại -> nhập 3/4 -> ra 75%
    output = run_fuel(["1/0", "3/4"])
    assert "75%" in output

def test_invalid_values():
    # Nhập chữ, số thập phân hoặc X > Y -> phải hỏi lại cho đến khi nhập đúng
    output = run_fuel(["three/four", "1.5/3", "5/4", "1/2"])
    assert "50%" in output
