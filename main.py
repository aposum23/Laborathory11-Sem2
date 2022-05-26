from threading import Thread
from time import sleep
import math

eps = 10 ** (-7)

def solve(x, num):
    global eps
    a = 1
    summa = 1
    i = 1
    prev = 0
    y = (eps ** x - eps ** (-x)) / 2
    while abs(summa - prev) > eps:
        a = x ** 3 / (1 * 2 * 3) + x ** 5 / (1 * 2 * 3 * 4 * 5)
        prev = summa
        if i % 2 == 0:
            summa += a
        else:
            summa += -1 * a
        i += 1
    print(f"Sum: {num} = {summa}")
    print(f"Check: {y}")


if __name__ == '__main__':
    th = Thread(target=solve, args=(0, 1))
    th.start()
    solve()
    x = 2
