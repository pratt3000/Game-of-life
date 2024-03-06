import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from scipy.signal import convolve2d

def next_generation(grid):
    kernel = np.array([[1, 1, 1],
                       [1, 0, 1],
                       [1, 1, 1]])

    alive_neighbours = convolve2d(grid, kernel, mode='same', boundary='fill', fillvalue=0)

    future = np.copy(grid)
    future[(grid == 0) & (alive_neighbours == 3)] = 1
    future[(grid == 1) & ((alive_neighbours < 2) | (alive_neighbours > 3))] = 0

    return future   

def update(frame):
    global grid
    grid = next_generation(grid)
    img.set_array(grid)
    return [img]

M, N = 50, 50
grid = np.random.choice([0, 1], size=(M, N), p=[0.9, 0.1])

fig, ax = plt.subplots()
img = ax.imshow(grid, cmap='gray', interpolation='nearest')

plt.ion()  # Turn on interactive mode

for _ in range(100):
    img.set_array(grid)
    grid = next_generation(grid)
    plt.pause(1)  # Adjust the pause time as needed

plt.ioff()  # Turn off interactive mode
plt.show()

