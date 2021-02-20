from point import Point


def convert_to_string(point: Point) -> str:
    data = str(point.x) + "," + str(point.y)
    return data


def convert_to_point(data: str) -> Point:
    x, y = data.split(",")
    return Point(int(x), int(y))
