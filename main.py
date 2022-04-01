import math
import matplotlib.pyplot as plt
import random


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

class Graph:
    def __init__(self):
        # TODO create graph window
        plt.axis(-1, 2, -1, 2)

    def plot_point(self, point: Point):
        # TODO add point to plot
        print(f"Plotting ({point.x},{point.y})")
        plt.scatter(point.x, point.y)
        plt.pause(0.05)


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
    point = Point(0.1, 0.1)
    while True:
        graph.plot_point(point)
        point = midpoint(
            point,
            random.choice(corners)
        )


if __name__ == "__main__":
    main()
