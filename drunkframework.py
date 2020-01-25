#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Create the environment
# Agent Framework

import random

# Defining agents (drunk)
class Drunk():
    def __init__(self, environment, drunks, name):
        self.drunks = drunks
        self.environment = environment
        self.x = random.randint(0,300) 
        self.y = random.randint(0,300)
        self.name = name 

# Moving randomly
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 300
        else:
            self.y = (self.y - 1) % 300

        if random.random() < 0.5:
            self.x = (self.x + 1) % 300
        else:
            self.x = (self.x - 1) % 300

# Method to monitor density. 
    def steps(self):
        self.environment[self.y][self.x] += 1 

