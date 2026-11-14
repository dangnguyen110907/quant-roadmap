"""
CS50P - Week 5: Unit Tests
https://cs50.harvard.edu/python/psets/5/test_twttr/

Mục tiêu:
Tự tay viết các hàm kiểm thử unit test bằng pytest và từ khoá assert.
"""

import runpy

# Tải hàm shorten từ bài twttr.py trước đó
twttr_mod = runpy.run_path("01_basics/twttr.py")
shorten = twttr_mod["shorten"]


# TODO: Bạn hãy viết 4 hàm test bắt đầu bằng 'def test_...':
# 1. def test_lowercase():
#       assert shorten("twitter") == "twttr"
# 2. def test_uppercase():
#       ...
# 3. def test_numbers():
#       ...
# 4. def test_punctuation():
#       ...
