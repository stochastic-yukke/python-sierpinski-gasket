import matplotlib.pyplot as plt
import numpy as np

def binomial_mod2(n, k):
    # Lucasの定理に基づき binomial(n, k) mod 2 を計算
    while n > 0 or k > 0:
        if (n % 2) < (k % 2):
            return 0
        n //= 2
        k //= 2
    return 1

def lucas_mod2_triangle(rows):
    triangle = np.zeros((rows, 2 * rows - 1), dtype=int)
    for n in range(rows):
        for k in range(n + 1):
            val = binomial_mod2(n, k)
            col = rows - n + 2 * k - 1
            triangle[n, col] = val
    return triangle

def plot_sierpinski_lucas(rows):
    data = lucas_mod2_triangle(rows)
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.imshow(data, cmap='binary', interpolation='nearest')
    ax.axis('off')
    return fig

# 図を生成して表示
fig = plot_sierpinski_lucas(128)
plt.show()
