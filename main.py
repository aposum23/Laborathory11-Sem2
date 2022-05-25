from threading import Thread
from time import sleep

def solve():
    x = 2
    res = []
    for i in range(10000000000):
        res.append(x ** 3 / (1 * 2 * 3) + x ** 5 / (1 * 2 * 3 * 4 * 5))
        print(f'sum: {sum(res)}')


if __name__ == '__main__':
    th = Thread(target=solve)
    th.start()
    solve()
    x = 2
    eps = 10 ** (-7)
    y = (eps ** x - eps ** (-x)) / 2
    print(f'y: {y}')
