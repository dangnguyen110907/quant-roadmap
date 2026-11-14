import subprocess
import sys

def run_coke(inputs: list[str]) -> str:
    input_str = "\n".join(inputs) + "\n"
    res = subprocess.run(
        [sys.executable, "01_basics/coke.py"],
        input=input_str,
        capture_output=True,
        text=True,
    )
    return res.stdout

def test_exact_change():
    output = run_coke(["25", "25"]).lower()
    assert "change owed: 0" in output
    assert "amount due: 25" in output or "amount_due: 25" in output

def test_with_change():
    output = run_coke(["25", "10", "25"]).lower()
    assert "change owed: 10" in output

def test_invalid_coins():
    output = run_coke(["30", "25", "25"]).lower()
    assert "change owed: 0" in output
