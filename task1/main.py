#!/usr/bin/env python3

# $1 - set dataset size, default 10

import statistics
import sys
from bruteforce import run_bruteforce
from heuristics import run_heuristics
from dataio import *
from timeit import default_timer as timer


try:
    dataset_size = int(sys.argv[1])
except:
    dataset_size = 10

# parse input data into list of KnapsackJob objects
jobs = get_knapsack_jobs(dataset_size)

# run bruteforce
before_bf = timer()
bruteforce_results = run_bruteforce(jobs)
after_bf = timer()

# TODO parse sample correct results, compare them with bruteforce

# run heuristics
before_hs = timer()
heuristics_results = run_heuristics(jobs)
after_hs = timer()

# calculate and report relative error
relative_errors = []
for i in range(40):
    bf_price = bruteforce_results[i][2]
    hs_price = heuristics_results[i][2]
    relative_error = (bf_price - hs_price)/bf_price
    relative_errors.append(relative_error)

print('\nAverage relative error is: {}%'
      .format(statistics.mean(relative_errors)*100))

print('\nExecution times:')
print('Bruteforce: {0:.10f}s'.format(after_bf - before_bf))
print('Heuristics: {0:.10f}s'.format(after_hs - before_hs))
