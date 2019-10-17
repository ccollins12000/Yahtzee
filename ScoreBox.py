import abc

class ScoreBox:

    def __init__(self):
        self._points = 0
        self._assigned = False

    @property
    def points(self):
        return self._points

    def getpoints(self):
        return self._points

    @property
    def assigned(self):
        return self._assigned

    def getassigned(self):
        return self._assigned

    @abc.abstractmethod
    def assign_points(self, value):
        pass


class Aces(ScoreBox):
    def assign_points(self, value):
        if not self.assigned:
            self._points = value
            self._assigned = True

    def __str__(self):
        return 'Aces: ' + str(self._points)





test = Aces()
print(test)
test.assign_points(4)
print(test)

test.assign_points(5)
print(test)