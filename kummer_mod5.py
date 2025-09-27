import matplotlib.pyplot as plt
import numpy as np

def binom_mod5(n, k):
    count = 0
    while n > 0 or k > 0:
        n_i = n % 5
        k_i = k % 5
        if k_i > n_i:
            count += 1
        n //= 5
        k //= 5
    return count

def lucas_mod2_triangle(rows):
    triangle = np.zeros((rows, 2 * rows - 1), dtype=int)
    for n in range(rows):
        for k in range(n + 1):
            val = binom_mod5(n, k)
            col = rows - n + 2 * k - 1
            triangle[n, col] = val
    return triangle

def plot_sierpinski_lucas(rows=100):
    data = lucas_mod2_triangle(rows)
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.imshow(data, cmap='binary', interpolation='nearest')
    ax.axis('off')
    return fig

# 図を生成して表示
fig = plot_sierpinski_lucas(128)
plt.show()
