#!/usr/bin/env python3

# $1 - set dataset size, default 10

import statistics
import sys
import time

from dynamic import run_dynamic
from branch_and_bound import run_bb
from bruteforce_recursion import run_bruteforce
from dataio import *


try:
    dataset_size = int(sys.argv[1])
except:
    dataset_size = 10

# parse input data into list of KnapsackJob objects
jobs = get_knapsack_jobs(dataset_size)

# get expected results
expected_results = get_expected_results(dataset_size)

# run bruteforce (recursion)
print('Bruteforce (recursion) results: ')
bruteforce_results = []
before_bruteforce = time.process_time()
for job in jobs:
    bruteforce_results.append(run_bruteforce(job))
after_bruteforce = time.process_time()

# compare bruteforce results with correct expected results
compare_results(expected_results, bruteforce_results)

# run branch and bound
print('Branch and Bound results: ')
bb_results = []
before_bb = time.process_time()
for job in jobs:
    bb_results.append(run_bb(job))
after_bb = time.process_time()

# compare branch and brand results with correct expected results
compare_results(expected_results, bb_results)

# run dynamic
# before_dyn = time.process_time()
# dynamic_results = []
# for job in jobs[:1]:
#     dynamic_results.append(run_dynamic(job))
# after_dyn = time.process_time()

# compare dynamic results with correct expected results
# compare_results(expected_results[:1], dynamic_results[:1])

print('\nExecution times:')
print('Bruteforce: {0:.10f}s'.format(after_bruteforce - before_bruteforce))
print('Branch & Bound: {0:.10f}s'.format(after_bb - before_bb))
# print('Dynamic: {0:.10f}s'.format(after_dyn - before_dyn))
