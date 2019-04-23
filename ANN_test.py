import cv2
import numpy as np
from random import randint

# 通过调用OpenCV函数创建ANN
animals_net = cv2.ml.ANN_MLP_create()

# ANN_MLP_RPROP和ANN_MLP_BACKPROP都是反向传播算法，此处设置相应的拓扑结构
animals_net.setLayerSizes(np.array([3, 6, 4]))
animals_net.setTrainMethod(cv2.ml.ANN_MLP_RPROP | cv2.ml.ANN_MLP_UPDATE_WEIGHTS)
animals_net.setActivationFunction(cv2.ml.ANN_MLP_SIGMOID_SYM)

# 指定ANN的终止条件
animals_net.setTermCriteria((cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1))

"""Input arrays
weight, length, teeth
"""

"""Output arrays
dog, eagle, dolphin and dragon
"""


def dog_sample():
    return [randint(10, 20), 1, randint(38, 42)]


def dog_class():
    return [1, 0, 0, 0]


def condor_sample():
    return [randint(3, 10), randint(3, 5), 0]


def condor_class():
    return [0, 1, 0, 0]


def dolphin_sample():
    return [randint(30, 190), randint(5, 15), randint(80, 100)]


def dolphin_class():
    return [0, 0, 1, 0]


def dragon_sample():
    return [randint(1200, 1800), randint(30, 40), randint(160, 180)]


def dragon_class():
    return [0, 0, 0, 1]


def record(sample, classification):
    return (np.array([sample], dtype=np.float32), np.array([classification], dtype=np.float32))


'''
为了提高精度，大多数ANN会迭代多个周期；一些常见的ANN示例，会对数据进行数百次迭代。
'''
if( __name__ == "__main__"):
    records = []

    RECORDS = 5000
    for x in range(0, RECORDS):
        records.append(record(dog_sample(), dog_class()))
        records.append(record(condor_sample(), condor_class()))
        records.append(record(dolphin_sample(), dolphin_class()))
        records.append(record(dragon_sample(), dragon_class()))

    EPOCHS = 2
    for e in range(0, EPOCHS):
        print("Epoch %d:" % e)
        for t, c in records:
            animals_net.train(t, cv2.ml.ROW_SAMPLE, c)

    TESTS = 100
    dog_results = 0
    for x in range(0, TESTS):
        clas = int(animals_net.predict(np.array([dog_sample()], dtype=np.float32))[0])
        print("class: %d" % clas)
        if (clas) == 0:
            dog_results += 1

    condor_results = 0
    for x in range(0, TESTS):
        clas = int(animals_net.predict(np.array([condor_sample()], dtype=np.float32))[0])
        print("class: %d" % clas)
        if (clas) == 1:
            condor_results += 1

    dolphin_results = 0
    for x in range(0, TESTS):
        clas = int(animals_net.predict(np.array([dolphin_sample()], dtype=np.float32))[0])
        print("class: %d" % clas)
        if (clas) == 2:
            dolphin_results += 1

    dragon_results = 0
    for x in range(0, TESTS):
        clas = int(animals_net.predict(np.array([dragon_sample()], dtype=np.float32))[0])
        print("class: %d" % clas)
        if (clas) == 3:
            dragon_results += 1

    print("Dog accuracy: %f%%" % (dog_results))
    print("condor accuracy: %f%%" % (condor_results))
    print("dolphin accuracy: %f%%" % (dolphin_results))
    print("dragon accuracy: %f%%" % (dragon_results))
    pass