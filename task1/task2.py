#!/usr/bin/env python3

# $1 - set dataset size, default 10

import statistics
import sys
import time

from dynamic import run_dynamic
from dataio import *


try:
    dataset_size = int(sys.argv[1])
except:
    dataset_size = 10

# parse input data into list of KnapsackJob objects
jobs = get_knapsack_jobs(dataset_size)

# get expected results
expected_results = get_expected_results(dataset_size)

# run dynamic
before_dyn = time.process_time()
dynamic_results = []
for job in jobs:
    dynamic_results.append(run_dynamic(job))
    # dynamic_results.append((0,0,0))
after_dyn = time.process_time()

# compare dynamic results with correct expected results
compare_results(expected_results, dynamic_results)

print('\nExecution times:')
print('Dynamic: {0:.10f}s'.format(after_dyn - before_dyn))
