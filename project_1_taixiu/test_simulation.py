"""
BỘ KIỂM THỬ CHO PROJECT 1: MÔ PHỎNG TÀI XỈU
"""

import sys
import os

sys.path.append(os.path.abspath("project_1_taixiu"))
from simulation import evaluate_round, simulate_player


def test_house_edge_triples():
    assert evaluate_round(1, 1, 1, "XIU") == -1
    assert evaluate_round(6, 6, 6, "TAI") == -1
    assert evaluate_round(2, 2, 2, "XIU") == -1
    assert evaluate_round(5, 5, 5, "TAI") == -1


def test_xiu_outcomes():
    assert evaluate_round(1, 2, 3, "XIU") == 1
    assert evaluate_round(1, 2, 3, "TAI") == -1
    assert evaluate_round(3, 3, 4, "XIU") == 1


def test_tai_outcomes():
    assert evaluate_round(4, 5, 6, "TAI") == 1
    assert evaluate_round(4, 5, 6, "XIU") == -1
    assert evaluate_round(3, 4, 4, "TAI") == 1


def test_simulate_player_basics():
    history = simulate_player(1000.0, 100.0, 10)
    assert isinstance(history, list)
    assert history[0] == 1000.0
    assert len(history) <= 11


def test_simulate_player_bankrupt():
    history = simulate_player(0.0, 100.0, 10)
    assert history == [0.0]
