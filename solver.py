from DE import *
from scipy.integrate import odeint
import math

class Exact_Solution:
    def __init__(self):
        return

    def solve(self, de: DE):
        try:
            ysa = []
            xs =[de.x0]
            for i in range(1, de.N + 1):
                xs.append(de.x0 + (i * de.h))
            dydx = eval("lambda y, x :" + de.string)
            ys = odeint(dydx, de.y0, xs)
            for i in range(0, len(ys)):
                ysa.append(ys[i][0])
            return xs, ysa
        except:
            print("Can not find exact solution")
            return [], []


class Euler_Solution:
    def __init__(self):
        return

    def solve(self, de: DE):
        try:
            xs = [de.x0]
            ys = [de.y0]
            h = (de.x - de.x0) / de.N
            for i in range(1, de.N+1):
                xs.append(de.x0 + (i * h))
                ys.append(ys[i-1] + (h * de.f(xs[i-1], ys[i-1])))
            return xs, ys
        except:
            print("Can not find euler solution")
            return [], []

class Improved_Euler_Solution:
    def __init__(self):
        return

    def solve(self, de: DE):
        try:
            xs = [de.x0]
            ys = [de.y0]
            y_temp = de.y0
            h = (de.x - de.x0) / de.N
            for i in range(1, de.N+1):
                k1 = de.f(xs[i-1], y_temp)
                k2 = de.f(xs[i-1] + h, y_temp + h*k1)
                k = (k1 + k2) / 2
                y_temp += h * k
                xs.append(de.x0 + (i * h))
                ys.append(y_temp)
            return xs, ys
        except:
            print("Can not find improved euler solution")
            return [], []

class Runge_Kutta_Solution:
    def __init__(self):
        return

    def solve(self, de: DE):
        try:
            xs = [de.x0]
            ys = [de.y0]
            h = (de.x - de.x0) / de.N
            for i in range(1, de.N+1):
                xs.append(de.x0 + (i * h))
                k1 = de.fi(ys[i-1], xs[i-1])
                k2 = de.fi(ys[i-1] + k1 * h/2, xs[i-1] + h/2)
                k3 = de.fi(ys[i-1] + k2 * h/2, xs[i-1] + h/2)
                k4 = de.fi(ys[i - 1] + h * k3, xs[i - 1] + h)
                k = h/6 * (k1 + k2*2 + 2*k3 +k4)
                ys.append(ys[i-1] + k)
            return xs, ys
        except:
            print("Can not find runge kutta solution")
            return [], []

