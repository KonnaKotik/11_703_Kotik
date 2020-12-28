import numpy as np
import matplotlib.pyplot as plt


def dist(x1, y1, x2, y2):
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def cluster(array, n, k):
    cl = np.zeros(n)
    for i in range(n):
        max_ar = max(array[i])
        for j in range(k):
            if array[i][j] == max_ar:
                cl[i] = j
    return cl



def draw(x, y, clust, x_cc, y_cc):
    colors = ['b', 'g', 'r', 'darkmagenta', 'm', 'y', 'k', 'w']
    for i in range(len(x)):
        plt.scatter(x[i], y[i], c=colors[int(clust[i])])

    plt.scatter(x_cc, y_cc, marker='X')
    plt.show()


def recntr(x, y, clust, k, m):
    x_cc = np.zeros(k)
    y_cc = np.zeros(k)

    for i in range(k):
        s_x = 0
        s_y = 0
        n = 0

        for j in range(len(x)):
            max = 0
            for q in clust[j]:
                if q > max :
                    max = q
                if clust[j, i] == max:
                    n = n + clust[j, i] ** m
                    s_x = s_x + clust[j, i] ** m * x[j]
                    s_y = s_y + clust[j, i] ** m * y[j]

            if n != 0:
                x_cc[i] = s_x / n
                y_cc[i] = s_y / n
            else:
                x_cc[i] = 0
                y_cc[i] = 0

    return x_cc, y_cc


def calculate(x, y, x_c, y_c, n, k, m):
    clust = np.zeros((n, k))
    for i in range(n):
        for j in range(k):
            sum = 0
            distance_j = dist(x[i], y[i], x_c[j], y_c[j])
            for q in range(k):
                distance_q = dist(x[i], y[i], x_c[q], y_c[q])
                sum += (distance_j / distance_q) ** (2 / (m - 1))
            clust[i, j] = 1 / sum
    return clust

def check(cl, clust, n, k, eps):
    max = 0
    for i in range(n):
        for j in range(k):
            diff = np.abs(clust[i, j] - cl[i, j])
            if diff > max:
                max = diff
    return max < eps


def c_means():
    n = 100
    k = 4
    m = 1.5
    esp = 0.1

    x = np.random.randint(1, 100, n)
    y = np.random.randint(1, 100, n)

    clust = np.zeros((n,k))

    for i in range(n):
        for j in range(k):
            clust[i, j] = np.random.uniform(1, 4)

    while True:
        x_c, y_c = recntr(x, y, clust, k, m)
        new_cl = calculate(x, y, x_c, y_c, n, k, m)
        if check(new_cl, clust, n, k, esp):
            clusters = cluster(new_cl, n, k)
            draw(x, y, clusters, x_c, y_c)
            break
        clust = new_cl
    return x_c, y_c, new_cl


c_means()

