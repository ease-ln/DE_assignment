import math
class DE:
    def __init__(self, eq: str, x0: float, y0: float, x: float, N: int):
        self.string = eq
        self.fi = eval("lambda y, x :" + eq)
        self.f = eval("lambda x, y :" + eq)
        self.x0 = x0
        self.y0 = y0
        self.h = (x-x0)/N
        self.x = x
        self.N = N

