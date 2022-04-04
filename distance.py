from __future__ import annotations


class Distance:
    kilometers = 0.0
    meters = 0.0

    def __init__(self, kilometers=0.0, meters=0.0):
        self.kilometers = kilometers
        self.meters = meters

    def __gt__(self, other: Distance):
        self_total = (self.kilometers*1000) + self.meters
        other_total = (other.kilometers*1000) + other.meters
        return self_total > other_total

    def __lt__(self, other: Distance):
        self_total = (self.kilometers * 1000) + self.meters
        other_total = (other.kilometers * 1000) + other.meters
        return self_total < other_total

    def __eq__(self, other):
        self_total = (self.kilometers * 1000) + self.meters
        other_total = (other.kilometers * 1000) + other.meters
        return self_total == other_total

    def __str__(self):
        return f'{self.kilometers}km {self.meters}m'


d1 = Distance(5, 100)
d2 = Distance(2, 500)
d3 = Distance(5, 100)

print('Distance d1:', d1)
print('Distance d2:', d2)
print('Distance d3:', d3)

print('d1 > d2:', d1 > d2)
print('d1 < d2:', d1 < d2)
print('d1 == d3:', d1 == d3)


