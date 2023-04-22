def calc_dist(p1, p2):
    return sum([(p1[i] - p2[i]) ** 2 for i in range(len(p1))]) ** 0.5

if __name__ == 'main':
    print(calc_dist((0, 0), (2, 1)))
    cos = (0 * 2 + 0 * 1) / calc_dist
