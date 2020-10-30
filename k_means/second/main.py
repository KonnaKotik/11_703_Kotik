import numpy as np
import matplotlib.pyplot as plt


def dist(x1, y1, x2, y2):
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def cluster(x_cc, y_cc, x, y, k):
    clust = []
    for i in range(0, n):
        r = dist(x_cc[0], y_cc[0], x[i], y[i])
        num = 0
        for j in range(1, k):
            if r > dist(x_cc[j], y_cc[j], x[i], y[i]):
                r = dist(x_cc[j], y_cc[j], x[i], y[i])
                num = j
        clust.append(num)
    return clust


def draw(x, y, clust, x_cc, y_cc, k):
    for i in range(0, len(x)):
        clr = (clust[i] + 1) / k
        plt.scatter(x[i], y[i], color=(clr, 0.2, clr ** 2))
    plt.scatter(x_cc, y_cc)
    plt.show()


def recntr(x, y, clust, k):
    for i in range(0, len(clust)):
        z_x = []
        z_y = []
        for j in range(0, k):
            if clust[i] == j:
                z_x.append(x[i])
                z_y.append(y[i])
        x_cc = np.mean(z_x)
        y_cc = np.mean(z_y)


def check():
    x_old, y_old = x_cc, y_cc
    recntr(x, y, clust, k)
    if (x_old == x_cc and y_old == y_cc):
        return True
    else:
        return False


def k_means(x, y, k):
    x_c = np.mean(x)  # ср.ариф всех координат
    y_c = np.mean(y)  # x_c и y_c - центр окружности
    R = 0
    for i in range(0, n):
        r_m = dist(x_c, y_c, x[i], y[i])
        if r_m > R:
            R = r_m
    x_cc = [R * np.cos(2 * np.pi * i / k) + x_c for i in range(k)]
    y_cc = [R * np.cos(2 * np.pi * i / k) + y_c for i in range(k)]

    clust = cluster(x_cc, y_cc, x, y, k)

    clust_iter = []

    while True:
        clust = cluster(x_cc, y_cc, x, y, k)
        if np.array_equal(clust, clust_iter):
            clust_iter = clust
            break
        else:
            clust_iter = clust
            recntr(x, y, clust, k)
        return clust_iter, x_cc, y_cc


def formul(x, y, x_cc, y_cc, clusters, k):
    r = 0
    for iter in range(k):
        for i in range(len(x_cc)):
            if clusters[i] == iter:
                r += dist(x[i], y[i], x_cc[iter], y_cc[iter]) ** 2
    return r


def optimal_k(x, y):
    clust_iter, x_cc, y_cc = k_means(x, y, 1)
    r_minus_2 = formul(x, y, x_cc, y_cc, clust_iter, 1)

    clust_iter, x_cc, y_cc = k_means(x, y, 2)
    r_minus_1 = formul(x, y, x_cc, y_cc, clust_iter, 2)

    for k in range(3, len(x)):
        clust_iter, x_cc, y_cc = k_means(x, y, k)
        r = formul(x, y, x_cc, y_cc, clust_iter, k)
        if np.abs((r_minus_1 - r) / (r_minus_2 - r_minus_1)) < 0.5:
            k = k - 1
            break
        r_minus_2 = r_minus_1
        r_minus_1 = r
    return k


n = 100
# n, k = 100, 4
x = np.random.randint(1, 100, n)
y = np.random.randint(1, 100, n)
optim = optimal_k(x, y)
print("optimal k = ", optim)
clust_new, x_cc_new, y_cc_new = k_means(x, y, optim)
draw(x, y, clust_new,x_cc_new, y_cc_new, optim)
# x_c = np.mean(x)  # ср.ариф всех координат
# y_c = np.mean(y)  # x_c и y_c - центр окружности
# R = 0
# for i in range(0, n):
#    r_m = dist(x_c, y_c, x[i], y[i])
#   if r_m > R:
#       R = r_m
# x_cc = [R * np.cos(2 * np.pi * i / k) + x_c for i in range(k)]
# y_cc = [R * np.cos(2 * np.pi * i / k) + y_c for i in range(k)]

#clust = cluster(x_cc, y_cc, x, y)
#draw(x, y, clust, x_cc, y_cc)


# набор точек, находим центр тядести - центр.
# Находим самую дальную точку, проводим окружность.
# Назодим 4 точки по формуле

# подбирать k оптимально по формуле
