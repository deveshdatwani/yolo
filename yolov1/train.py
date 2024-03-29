import os
import torch
import argparse
import torchvision
from utils import *
from model import YOLO
from torch.optim import SGD


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="argument parser for training yolo network")
    parser.add_argument('--batch-size', default=4, type=int, help="set batch size for mini batch gradient descent")
    parser.add_argument('--epochs', default=10, type=int, help="set number of epochs to train for")
    parser.add_argument('--learning-rate', default=0.00001, type=float, help="set learning rate of the network")
    parser.add_argument('--momentum', default=0.9, type=float, help="set momentume or update rule")
    parser.add_argument('--weight-decay', default=0.00005, type=float, help="set weight decay")
    parser.add_argument('--num-workers', default=4, type=int, help="set number of workers for parellel compute")

    args = parser.parse_args()