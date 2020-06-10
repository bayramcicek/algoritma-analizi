#!/usr/bin/python3
# created by cicek on Jun 10, 2020 11:00

import random
import pylab

'''
sample içindeki elemanları arttırır isek 
varyans her zaman düşer.
'''


def variance(a):
    """Assumes that X is a list of numbers.
    Returns the standard deviation of X"""
    mean = sum(a) / len(a)
    tot = 0.0
    for x in a:
        tot += (x - mean) ** 2
    return tot / len(a)


def std_dev(b):
    """Assumes that X is a list of numbers.
    Returns the standard deviation of X"""
    return variance(b) ** 5


def plot_means(num_dice_per_trial, num_dice_thrown, num_bins, legend, color, style):
    means = []
    num_trials = num_dice_thrown // num_dice_per_trial
    for i in range(num_trials):
        vals = 0
        for j in range(num_dice_per_trial):
            vals += 5 * random.random()
        means.append(vals / num_dice_per_trial)
        pylab.hist(means, num_bins, color=color, label=legend,
                   weights=pylab.array(len(means) * [1]) / len(means),
                   hatch=style)
    return sum(means) / len(means), variance(means)


mean, var = plot_means(10, 100, 50, '1 die', 'w', '*')
print('Mean of rolling 10 die = ', round(mean, 4), 'Variance = ', round(var, 4))

mean, var = plot_means(1, 100, 50, '1 die', 'w', '*')
print('Mean of rolling 1 die = ', round(mean, 4), 'Variance = ', round(var, 4))

"""
output:

    Mean of rolling 10 die =  2.5632 Variance =  0.0852
    Mean of rolling 1 die =  2.4495 Variance =  2.0982
    
    Process finished with exit code 0
    
"""
