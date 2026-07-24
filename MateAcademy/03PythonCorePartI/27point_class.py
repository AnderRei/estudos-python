from math import sqrt


class Point:
    points = []

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        Point.points.append(self)

    def distance_to_origin(self) -> float:
        return round(sqrt(self.x ** 2 + self.y ** 2), 2)

    def distance_to_point(self, point) -> float:
        return round(sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2), 2)

    def distance_to_x_axis(self):
        return abs(self.y)

    def distance_to_y_axis(self):
        return abs(self.x)

    def find_closest_point(self):
        other_points = [p for p in Point.points if p is not self]

        if not other_points:
            return None

        return min(
            other_points,
            key=lambda p: self.distance_to_point(p)
        )
