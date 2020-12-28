import matplotlib.pyplot as plt
import numpy as np
import random

def dist(x1, y1, x2, y2):
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def plot(x, y, color_index):
    plt.scatter(x, y, c=colors[color_index])


def with_classification(number_of_class_el, number_of_classes):
    data = []
    for classNum in range(number_of_classes):
        centerX, centerY = random.random() * 5.0, random.random() * 5.0
        for rowNum in range(int(number_of_class_el)):
            data.append([[random.gauss(centerX, 0.5), random.gauss(centerY, 0.5)], classNum])
    return data


def without_classification(number_of_class_el, number_of_classes):
    data = []
    for classNum in range(number_of_classes):
        centerX, centerY = random.random() * 5.0, random.random() * 5.0
        for rowNum in range(int(number_of_class_el)):
            data.append([random.gauss(centerX, 0.5), random.gauss(centerY, 0.5)])
    return data


k = 20
clusters = []
cl = 4

colors = ['darkmagenta', 'b', 'g', 'r', 'y', 'k', 'w', 'm']


count = cl * 400
count_classified = count * 0.8
count_uncl = count * 0.2
classified = with_classification(count_classified / cl, cl)
new_objects = without_classification(count_uncl / cl, cl)

for i in range(len(classified)):
    color = classified[i][1] + 1
    plot(classified[i][0][0], classified[i][0][1], color)

plt.show()

for i in range(len(new_objects)):
    plot(new_objects[i][0], new_objects[i][1], 0)

plt.show()

for i in range(len(new_objects)):
    neighbours = []
    for j in range(len(classified)):
        distance_to_point = dist(new_objects[i][0],
                                 new_objects[i][1],
                                 classified[j][0][0],
                                 classified[j][0][1])
        point_cluster_number = classified[j][1]
        neighbours.append([distance_to_point, point_cluster_number])
    neighbours.sort()
    k_nearest_neighbours = [neighbours[i] for i in range(k)]

    clusters_c = np.zeros(cl)
    for j in range(len(k_nearest_neighbours)):
        clusters_c[k_nearest_neighbours[j][1]] += 1

    max_neighbours = 0
    cluster_with_max_neighbours = 0

    iterator = 0
    for neighbours_in_cluster in clusters_c:
        if neighbours_in_cluster > max_neighbours:
            max_neighbours = neighbours_in_cluster
            cluster_with_max_neighbours = iterator
        iterator = iterator + 1
    clusters.append(cluster_with_max_neighbours)

for i in range(len(new_objects)):
    color = clusters[i] + 1
    plot(new_objects[i][0], new_objects[i][1], color)

plt.show()