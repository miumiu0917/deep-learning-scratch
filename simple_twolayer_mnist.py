# coding: utf-8

import numpy as np

from common.functions import *
from dataset.mnist import load_mnist


class TwoLayer(object):
  def __init__():
    self.w1 = 


def main():
  (train_image, train_label), (test_image, test_label) = load_mnist(normalize=True, flatten=True)
  print(train_image.shape)


if __name__ == '__main__':
  main()