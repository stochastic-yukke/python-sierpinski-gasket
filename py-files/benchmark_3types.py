import time
import numpy as np
import matplotlib.pyplot as plt

# 漸化式による方法
def pascal_mod2_triangle(rows):
    triangle = np.zeros((rows, rows), dtype=np.uint8)
    triangle[0, 0] = 1
    for n in range(1, rows):
        triangle[n, 0] = 1
        triangle[n, n] = 1
        for k in range(1, n):
            triangle[n, k] = (triangle[n-1, k-1] ^ triangle[n-1, k])
    return triangle


# 桁ごとにLucasの定理を適用する方法
def binomial_odd_lucas(n: int, k: int) -> int:
    while n > 0 or k > 0:
        if (k & 1) > (n & 1):
            return 0
        n >>= 1
        k >>= 1
    return 1

def lucas_mod2_triangle(rows):
    triangle = np.zeros((rows, rows), dtype=np.uint8)
    for n in range(rows):
        for k in range(n+1):
            triangle[n, k] = binomial_odd_lucas(n, k)
    return triangle


# 論理積を使う方法
def binomial_odd_and(n: int, k: int) -> int:
    return (n & k) == k

def and_mod2_triangle(rows):
    triangle = np.zeros((rows, rows), dtype=np.uint8)
    for n in range(rows):
        for k in range(n+1):
            triangle[n, k] = binomial_odd_and(n, k)
    return triangle


# グラフ
def benchmark_and_plot_loglog(row_sizes):
    methods = [
        ("Pascal recurrence (mod 2)", pascal_mod2_triangle),
        ("Lucas digit comparison", lucas_mod2_triangle),
        ("Bitwise AND trick", and_mod2_triangle),
    ]

    results = {name: [] for name, _ in methods}

    for rows in row_sizes:
        print(f"Running benchmark for rows={rows}...")
        for name, func in methods:
            start = time.perf_counter()
            func(rows)
            end = time.perf_counter()
            results[name].append(end - start)

    # プロット
    plt.figure(figsize=(9,6))
    for name in results:
        plt.plot(row_sizes, results[name], marker='o', label=name)

    N = np.array(row_sizes, dtype=float)
    norm = results["Bitwise AND trick"][0] / (N[0]**2)
    plt.plot(N, norm * N**2, '--', label="Θ(N²) baseline")

    norm2 = results["Lucas digit comparison"][0] / (N[0]**2 * np.log2(N[0]))
    plt.plot(N, norm2 * N**2 * np.log2(N), '--', label="Θ(N² log N) baseline")

    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Number of rows (N)")
    plt.ylabel("Execution time (seconds)")
    plt.title("Sierpinski Gasket Generation Benchmark (log-log)")
    plt.legend()
    plt.grid(True, which="both", ls="--")
    plt.show()

# 実行例
if __name__ == "__main__":
    row_sizes = [128, 256, 512, 768, 1024]
    benchmark_and_plot_loglog(row_sizes)
