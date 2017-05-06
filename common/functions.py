# coding: utf-8
import numpy as np

def relu(x):
  return np.maximum(x, 0)


def mean_squared_error(y, t):
  return 0.5 * np.sum((y-t) ** 2)


def step_function(x):
  y = x > 0
  return y.astype(np.int)


def sigmoid(x):
  return 1 / (1 + np.exp(-x))


def softmax(x):
  c = np.max(x)
  # オーバーフロー対策
  exp_x = np.exp(x - c)
  sum_exp_x = np.sum(exp_x)
  return exp_x / sum_exp_x