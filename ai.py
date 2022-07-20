# AI for Doom



# Importing the libraries
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.autograd import Variable 

# importing the packages for openAI and Doom
import gym
from gym.wrappers import SkipWrapper
from ppaqette_gym_doom.wrappers.action_space import ToDiscrete

# import the other Python files
import experience_replay, image_preprocessing

# Part 1 Building AI
# Making the Brain 
class CNN(nn.Module):
    def __init__(self, number_actions):
        super(CNN,self).__init__()
        self.convolution1 = nn.Conv2d(in_channels = 1, out_channels = 32, kernel_size = 5)
        self.convolution2 = nn.Conv2d(in_channels = 32, out_channels = 32, kernel_size = 3)
        self.convolution3 = nn.Conv2d(in_channels = 32, out_channels = 64, kernel_size = 2)
        self.fc1 = nn.Linear(in_features = number_neurons, out_features = 40)
        self.fc2 = nn.Linear(in_features = 40, number_actions)
        
        
        
