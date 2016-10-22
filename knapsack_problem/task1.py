#!/usr/bin/env python3

# $1 - set dataset size, default 10

import statistics
import sys
import time

from bruteforce import run_bruteforce
from heuristics import run_heuristics
from dataio import *


try:
    dataset_size = int(sys.argv[1])
except:
    dataset_size = 10

# parse input data into list of KnapsackJob objects
jobs = get_knapsack_jobs(dataset_size)

# run bruteforce
before_bf = time.process_time()
bruteforce_results = run_bruteforce(jobs)
after_bf = time.process_time()

# get expected results
expected_results = get_expected_results(dataset_size)

# compare bruteforce and heuristics
if not compare_results(expected_results, bruteforce_results):
    exit(1)

# run heuristics
before_hs = time.process_time()
heuristics_results = run_heuristics(jobs)
after_hs = time.process_time()

# calculate and report relative error
relative_errors = []
for i in range(50):
    bf_price = bruteforce_results[i][2]
    hs_price = heuristics_results[i][2]
    relative_error = (float(bf_price) - float(hs_price))/float(bf_price)
    relative_errors.append(relative_error)

print('\nAverage relative error is: {}%'
      .format(statistics.mean(relative_errors)*100))
print('Max error is: {}%'
      .format(max(relative_errors)*100))

print('\nExecution times:')
print('Bruteforce: {0:.10f}s'.format(after_bf - before_bf))
print('Heuristics: {0:.10f}s'.format(after_hs - before_hs))
