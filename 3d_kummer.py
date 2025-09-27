import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def binomial_p_adic_val(n, k, p):
    """Kummer's theorem: count carries in base-p subtraction"""
    count = 0
    while n > 0 or k > 0:
        if k % p > n % p:
            count += 1
        n //= p
        k //= p
    return count

def generate_kummer_lucas_3d(rows=64, p=2):
    Z = np.zeros((rows, rows))
    for n in range(rows):
        for k in range(n + 1):
            Z[n, k] = binomial_p_adic_val(n, k, p)
    return Z

def plot_kummer_lucas_3d(rows=64, p=2, cmap='plasma'):
    Z = generate_kummer_lucas_3d(rows, p)
    X, Y = np.meshgrid(np.arange(rows), np.arange(rows))

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    surf = ax.plot_surface(X, Y, Z, cmap=cmap, edgecolor='k', linewidth=0.2, antialiased=True)

    ax.set_xlabel("n")
    ax.set_ylabel("k")
    ax.set_zlabel(f"v_p(binomial(n,k)), p={p}")
    ax.set_title(f"Kummer-Lucas Fractal in 3D (mod {p})")

    fig.colorbar(surf, shrink=0.5, aspect=8)
    return fig

# 実行
fig = plot_kummer_lucas_3d(rows=64, p=2, cmap='inferno')
plt.show()
