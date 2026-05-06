
import numpy
import matplotlib.pyplot as plt
from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]


mean = numpy.mean(speed)
standard_deviation = numpy.std(speed)
print(f"the mean is {mean:.3f}")
print(f"the standard deviation is {standard_deviation: .3f}")
variance = numpy.var(speed)
print(f"the variance is {variance: .3f}")
percentile = numpy.percentile(speed, 75)
print(f"the 70 percentile is {percentile}")
#plt.hist(speed, 5)
#plt.show()

#uniform = numpy.random.uniform(0.0, 20.0, 1000)
#plt.hist(uniform, 20)
#plt.show()

normal = numpy.random.normal(5.0, 2.0, 10000)
#plt.hist(normal, 100)
#plt.show()



age_x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
speed_y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(age_x, speed_y)
def myfun(x):
    return slope * x + intercept
mymodel = list(map(myfun, age_x))
plt.scatter(age_x, speed_y)
plt.plot(age_x, mymodel)
plt.show()

x = numpy.random.normal(5, 1.0, 1000)
y = numpy.random.normal(10, 2.0, 1000)
#plt.scatter(x, y)
#plt.show()






def update_w_and_b(spendings, sales, w, b, alpha):
    dl_dw = 0.0
    dl_db = 0.0

    N = len(spendings)

    for i in range(N):
        dl_dw += -2 * spendings[i] * (sales[i] - (w * spendings[i] + b))
        dl_db += -2 * (sales[i] - (w * spendings[i] + b))

    # update w and b
    w = w - alpha * dl_dw * (1/float(N))
    b = b - alpha * dl_db * (1/ float(N))

    return w, b

def avg_loss(spendings, sales, w, b):
    N = len(spendings)
    total_error = 0.0
    for i in range(N):
        total_error += (sales[i] - (w * spendings[i] + b)) ** 2
    return total_error / float(N)

def train(spendings, sales, w, b ,alpha, epochs):
    for e in range(epochs):
        w, b = update_w_and_b(spendings, sales, w, b, alpha)
        if e % 400 == 0:
            print("epoch:", e, "loss: ", avg_loss(spendings, sales, w, b))







