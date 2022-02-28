class Line:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return "Line {} Color {}".format(self.name, self.color)


class Station(Line):
    def __init__(self, name, Line):
        self.name = name
        self.Line = Line

    def __str__(self):
        return "Station {} on Line {}".format(self.name, self.Line.name)
