from math import fabs
from DE import *

class Error:
    def __init__(self):
        return

    def local_calc(self, y: list, appx: list, appy: list):
        try:
            x = []
            err = []
            for i in range(len(appx)):
                x.append(appx[i])
                err.append(fabs(appy[i] - y[i]))
            return x, err
        except ValueError:
            print("Can not find local error")
            return [], []

    def global_calc(self, ey,appx, appy):
        try:
            g_x, g_y = self.local_calc(ey, appx, appy)
            x = []
            err = []
            for i in range(1, min(len(g_x), len(g_y))):
                x.append(g_x[i])
                err.append(fabs(g_y[i] - g_y[i - 1]))
            return x, err
        except ValueError:
            print("Can not find total error")
            return [], []
