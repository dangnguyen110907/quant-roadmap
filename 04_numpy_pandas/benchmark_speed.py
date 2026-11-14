"""
MODULE 3: NUMPY & PANDAS (BÀI 1: BẢN CHẤT VECTORIZATION)
Thí nghiệm đo tốc độ: Python thuần (Vòng lặp for) VS NumPy (Vectorization)
Bài toán: Nhân đôi giá của 1.000.000 (1 triệu) dòng dữ liệu nến.
"""

import time
import numpy as np


def python_loop_way(data: list) -> list:
    """Cách truyền thống: Dùng vòng lặp for của Python thuần."""
    result = []
    for x in data:
        result.append(x * 2.0)
    return result


def numpy_vectorized_way(data: np.ndarray) -> np.ndarray:
    """Cách của kỹ sư Quant: Phép toán véc-tơ hoá (Vectorization).

    Không hề có một vòng lặp for nào!
    """
    return data * 2.0


def main():
    n = 1_000_000  # 1 triệu phần tử
    print(f"⚡ BẮT ĐẦU ĐO TỐC ĐỘ TRÊN {n:,} PHẦN TỬ DỮ LIỆU:")
    print("--------------------------------------------------")

    # Tạo 1 triệu con số ngẫu nhiên
    raw_list = [float(i) for i in range(n)]
    np_array = np.arange(n, dtype=np.float64)

    # 1. Đo tốc độ vòng for Python thuần
    t0 = time.perf_counter()
    res1 = python_loop_way(raw_list)
    t1 = time.perf_counter()
    time_loop = t1 - t0
    print(f"1. Vòng lặp for Python thuần : {time_loop:.4f} giây")

    # 2. Đo tốc độ NumPy Vectorization
    t0 = time.perf_counter()
    res2 = numpy_vectorized_way(np_array)
    t1 = time.perf_counter()
    time_numpy = t1 - t0
    print(f"2. NumPy Vectorization       : {time_numpy:.4f} giây")

    # So sánh
    speedup = time_loop / time_numpy
    print("--------------------------------------------------")
    print(f"🚀 KẾT QUẢ: NumPy nhanh gấp {speedup:.1f} LẦN so với vòng for!")


if __name__ == "__main__":
    main()
