import tensorflow as tf
import matplotlib.pyplot as plt

print("Start")

x = -6.0
g = []
n = 1200

for i in range(n):
    output = tf.math.sigmoid(x)
    g.append(output)
    print(output)

    x += 12 / n

plt.plot(g)
plt.show()