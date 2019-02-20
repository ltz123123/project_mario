div = 10000
range_ = [0, 2]
integral = 0
interval = (range_[1] - range_[0]) / div
a = 0
b = interval

def f(x):
    return x

while b <= range_[1]:
    integral += (f(b) + f(a)) * 0.5 * interval
    a += interval
    b += interval
else:
    print(integral)

