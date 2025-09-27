#以下，p:prime.
import numpy as np
import matplotlib.pyplot as plt

def binomial_p_adic_val(n, k, p):
    """
    Return the p-adic valuation v_p( C(n, k) ) using Kummer's theorem:
    count the number of carries in base-p subtraction of k from n
    """
    count = 0
    while n > 0 or k > 0:
        n_i = n % p
        k_i = k % p
        if k_i > n_i:
            count += 1
        n //= p
        k //= p
    return count

def generate_kummer_lucas_array(rows=128, p=3):
    arr = np.zeros((rows, rows), dtype=int)
    for n in range(rows):
        for k in range(n + 1):  # Pascal triangle: k <= n
            v = binomial_p_adic_val(n, k, p)
            arr[n, k] = v
    return arr

def plot_kummer_lucas_fractal(rows=128, p=3, cmap='viridis'):
    data = generate_kummer_lucas_array(rows, p)

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.imshow(data, cmap=cmap, origin='upper')
    ax.axis('off')
    ax.set_title(f"Kummer-Lucas Fractal (mod {p})", fontsize=14)
    return fig

# 実行
fig = plot_kummer_lucas_fractal(rows=615, p=3, cmap='plasma')
plt.show()
