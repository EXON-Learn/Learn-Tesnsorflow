import tensorflow as tf
import matplotlib.pyplot as plt

#시작
print("Start")


x = -6.0

#그래프를 그릴 변수
g = []

#반복할 수
n = 1200


for i in range(n + 1):
    output = tf.math.sigmoid(x)
    g.append(output)
    print(i, output)

    x += 12 / n

#그래프 그리기
plt.plot(g)
plt.show()