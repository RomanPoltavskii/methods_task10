# y'=(y^3 + x + 1) / (3y^2), y(0) = -1.24, (0 <= x <= 8)

def f(x, y):
    return (y ** 3 + x + 1) / (3 * y ** 2)


def runge_kutta(f, y0, a, b, h):
    n = int((b - a) / h)
    x = [a + i * h for i in range(n + 1)]
    y = [y0]

    for i in range(n):
        k1 = f(x[i], y[-1])
        k2 = f(x[i] + h/ 2, y[-1] + h / 2 * k1)
        k3 = f(x[i] + h / 2, y[-1] + h / 2 * k2)
        k4 = f(x[i] + h, y[-1] + h * k3)
        y.append(y[-1] + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4))

    return x, y


x, y = runge_kutta(f, -1.24, 0, 8, 0.1)

for i in range(len(x)):
    print('y({:.1f}) = {:.6f}'.format(x[i], y[i]))