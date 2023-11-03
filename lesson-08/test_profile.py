from memory_profiler import profile


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class PointSlots:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y


@profile
def run_points(n):
    points = [Point(3388, 4455) for i in range(n)]

    for p in points:
        p.x = 1
        p.y += 10


@profile
def run_slot_points(n):
    points = [PointSlots(3388, 4455) for i in range(n)]

    for p in points:
        p.x = 1
        p.y += 10


if __name__ == "__main__":
    n = 50_000
    run_points(n)
    run_slot_points(n)
