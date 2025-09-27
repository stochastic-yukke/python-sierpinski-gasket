import matplotlib.pyplot as plt
import numpy as np

def is_binom_odd(n: int, k: int):
    return (n & k) == k

def lucas_mod2_triangle(rows):
    triangle = np.zeros((rows, 2 * rows - 1), dtype=int)
    for n in range(rows):
        for k in range(n + 1):
            col = rows - n + 2 * k - 1
            triangle[n, col] = is_binom_odd(n, k)
    return triangle

def plot_sierpinski_lucas(rows):
    data = lucas_mod2_triangle(rows)
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.imshow(data, cmap='binary', interpolation='nearest')
    ax.axis('off')
    return fig

# 図を生成して表示
fig = plot_sierpinski_lucas(256)
plt.show()


print(is_binom_odd(5,2))
print(1&0,0&1,1&1,0&0,5&2)#110010/101&010論理積
