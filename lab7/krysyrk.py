import numpy as np
from matplotlib import pyplot as plt
import tensorflow as tf

# tworzymy tablice o wymiarach 128x128x3 (3 kanaly to RGB)
# uzupelnioną zerami = kolor czarny
data = np.zeros((128, 128, 3), dtype=np.uint8)


# chcemy zeby obrazek byl czarnobialy,
# wiec wszystkie trzy kanaly rgb uzupelniamy tymi samymi liczbami
# napiszmy do tego funkcje
def draw(img, x, y, color):
    img[x, y] = [color, color, color]


# zamalowanie 4 pikseli w lewym górnym rogu
draw(data, 5, 5, 100)
draw(data, 6, 6, 100)
draw(data, 5, 6, 255)
draw(data, 6, 5, 255)


# rysowanie kilku figur na obrazku
for i in range(128):
    for j in range(128):
        if (i-64)**2 + (j-64)**2 < 900:
            draw(data, i, j, 200)
        elif i > 100 and j > 100:
            draw(data, i, j, 255)
        elif (i-15)**2 + (j-110)**2 < 25:
            draw(data, i, j, 150)
        elif (i-15)**2 + (j-110)**2 == 25 or (i-15)**2 + (j-110)**2 == 26:
            draw(data, i, j, 255)

# konwersja macierzy na obrazek i wyświetlenie
plt.imshow(data, interpolation='nearest')
plt.show()

# b
kernel = np.array([[1, 0, -1],
                   [1, 0, -1],
                   [1, 0, -1]])

output = np.zeros((126, 126, 3), dtype=np.uint8)
for c in range(3):
    for i in range(126):
        for j in range(126):
            patch = data[i:i+3, j:j+3, c]
            output[i, j] = np.sum(patch * kernel)

plt.imshow(output, interpolation='nearest')
plt.show()

# c
kernel = np.array([[1, 0, -1],
                   [1, 0, -1],
                   [1, 0, -1]])

output = np.zeros((63, 63, 3), dtype=np.uint8)
for c in range(3):
    for i in range(0, 126, 2):  # zmiana inkrementacji na 2
        for j in range(0, 126, 2):
            patch = data[i:i+3, j:j+3, c]
            output[i//2, j//2] = np.sum(patch * kernel)

plt.imshow(output, interpolation='nearest')
plt.show()

# d

kernel2 = np.array([[1, 1, 1],
                   [0, 0, 0],
                   [-1, -1, -1]])

output3 = np.zeros((126, 126, 3), dtype=np.uint8)
for c in range(3):
    for i in range(126):
        for j in range(126):
            patch = data[i:i+3, j:j+3, c]
            output3[i, j, c] = np.sum(patch * kernel2)
plt.imshow(output3, interpolation='nearest')
plt.show()


# d, stride = 2
kernel2 = np.array([[1, 1, 1],
                   [0, 0, 0],
                   [-1, -1, -1]])

output2 = np.zeros((63, 63, 3), dtype=np.uint8)
for c in range(3):
    for i in range(0, 126, 2):  # zmiana inkrementacji na 2
        for j in range(0, 126, 2):
            patch = data[i:i+3, j:j+3, c]
            output2[i//2, j//2] = np.sum(patch * kernel2)

plt.imshow(output2, interpolation='nearest')
plt.show()

# e

# Tworzenie jądra Sobela
kernel_x = np.array([[-1, -2, -1],
                     [0,  0,  0],
                     [1,  2,  1]])

kernel_y = np.array([[-1,  0,  1],
                     [-2,  0,  2],
                     [-1,  0,  1]])

# Konwolucja z jądrem Sobela
output_x = np.zeros((126, 126, 3), dtype=np.uint8)
output_y = np.zeros((126, 126, 3), dtype=np.uint8)

for c in range(3):
    for i in range(126):
        for j in range(126):
            patch = data[i:i+3, j:j+3, c]
            output_x[i, j, c] = np.sum(patch * kernel_x)
            output_y[i, j, c] = np.sum(patch * kernel_y)

# Połączenie wyników uzyskanych dla krawędzi poziomej i pionowej
output = np.abs(output_x) + np.abs(output_y)

# Wyświetlenie obrazka z wykrytymi krawędziami ukośnymi
plt.imshow(output, interpolation='nearest')
plt.show()
