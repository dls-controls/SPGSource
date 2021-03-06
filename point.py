from collections import OrderedDict


class Point(object):
    """Contains information about for each scan point

    Attributes:
        positions (dict): Dict of str position_name -> float position for each
            scannable dimension. E.g. {"x": 0.1, "y": 2.2}
        lower (dict): Dict of str position_name -> float lower_bound for each
            scannable dimension. E.g. {"x": 0.95, "y": 2.15}
        upper (dict): Dict of str position_name -> float upper_bound for each
            scannable dimension. E.g. {"x": 1.05, "y": 2.25}
        indexes (list): List of int indexes for each dataset dimension, fastest
            changing last. E.g. [15]
    """

    def __init__(self):
        self.positions = OrderedDict()
        self.lower = OrderedDict()
        self.upper = OrderedDict()
        self.indexes = []
