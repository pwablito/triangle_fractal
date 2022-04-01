import math
import matplotlib.pyplot as plt
import random
import time


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


class Graph:
    def __init__(self):
        plt.axis([-0.1, 1.1, -0.1, 1.1])

    def plot_point(self, point: Point):
        plt.scatter(point.x, point.y, c=["#000000"], marker=",", linewidths=0, s=1)

    def update_display(self):
        plt.pause(0.001)


def midpoint(a: Point, b: Point):
    return Point(
        (a.x + b.x) / 2.0,
        (a.y + b.y) / 2.0,
    )


def main():
    graph = Graph()
    corners = [
        Point(0.0, 0.0),
        Point(1.0, 0.0),
        Point(0.5, 0.5 * math.sqrt(3.0)),
    ]
    for point in corners:
        graph.plot_point(point)
    point = Point(0.0, 0.0)
    total_points = 100000
    group_size = 2000
    for _ in range(int(total_points / group_size)):
        for _ in range(group_size):
            graph.plot_point(point)
            point = midpoint(
                point,
                random.choice(corners)
            )
        graph.update_display()
    print("Finished generating fractal")
    while True:
        time.sleep(1)


if __name__ == "__main__":
    main()
