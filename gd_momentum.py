# _*_ coding: utf-8 _*_
import numpy as np
import matplotlib.pyplot as plt
import os

a = np.linspace(-10,10,100)
b = np.linspace(-10, 10, 100)
# print "a={0}, b={1}".format(a,b)
X, Y = np.meshgrid(a, b)
# print "X={0},\n Y={1}".format(X, Y)
Z =  X*X + 50 *Y*Y
# print Z


def f(x):
    return x[0] * x[0] + 50 * x[1] * x[1]


def g(x):
    return np.array([2 * x[0], 100 * x[1]])


def contour(X,Y,Z, arr=None, name=None):
    plt.figure()
    plt.figure(figsize=(15, 7))
    plt.contour(X, Y, Z, color="black")
    plt.plot(0, 0, marker="*")
    if arr is not None:
        arr = np.array(arr)
        for i in range(len(arr)-1):
            plt.plot(arr[i:i+2, 0], arr[i:i+2, 1])
    if name is not None:
        curpath = os.path.abspath(os.curdir).__str__()
        plt.savefig(os.path.join(curpath,name.__str__()+"jpg"))
        return
    plt.show()


def gd(x_start,lr,g,it=20):
    x = np.array(x_start,dtype='float64')
    process_dot = [x.copy()]
    for i in range(it):
        grad = g(x)
        x -= lr * grad
        process_dot.append(x.copy())
        print "iteration={0}, grad={1}, x={2}".format(i, grad, x)
        if abs(sum(grad)) < 1e-6:
            break
    return x, process_dot


def momentum(x_start, lr, g, discount=0.7, it=20):
    x = np.array(x_start,dtype='float64')
    process_dot = [x.copy()]
    pre_grad = np.zeros_like(x)
    for i in range(it):
        grad = g(x)
        pre_grad = pre_grad * discount - lr * grad
        x += pre_grad
        process_dot.append(x.copy())
        print "iteration={0}, grad={1}, pre_grad={2}, x={3}, f(x)={4}".format(i, grad, pre_grad,x,f(x))
        if abs(sum(grad)) < 1e-6:
            break
    return x, process_dot


def nesterov(x_start, lr, g, discount=0.7, it=20):
    x = np.array(x_start, dtype='float64')
    process_dot = [x.copy()]
    pre_grad = np.zeros_like(x)
    for i in range(it):
        x_future = x + discount * pre_grad
        grad = g(x_future)
        pre_grad = pre_grad * discount - lr * grad
        x += pre_grad
        process_dot.append(x.copy())
        print "iteration={0}, grad={1}, pre_grad={2}, x={3}".format(i, grad, pre_grad, x)
        if abs(sum(grad)) < 1e-6:
            break
    return x, process_dot


x, arr_x = momentum([9.5,7.5],0.01,g,discount=0.9,it=30)
contour(X,Y,Z,arr_x,name="momentum")  #

# x, arr_x_gd = gd([9.5,7.5],0.012,g,it=50)
# contour(X,Y,Z,arr_x_gd,name="gd")
#
x, arr_x_nes = nesterov([9.5,7.5],0.012,g,discount=0.9,it=12)
contour(X,Y,Z,arr_x_nes,name="nesterov")
# plt.figure()
# Z = X * X + 50 * Y * Y
