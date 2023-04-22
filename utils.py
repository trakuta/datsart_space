def calc_dist(p1, p2):
    return sum([(p1[i] - p2[i]) ** 2 for i in range(len(p1))]) ** 0.5

