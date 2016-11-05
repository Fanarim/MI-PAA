#!/usr/bin/env python3

# $1 - set dataset size, default 10

import statistics
import sys
import time

from branch_and_bound import run_bb
from bruteforce_recursion import run_bruteforce
from dynamic import run_dynamic
from fptas import run_fptas
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
# print('Bruteforce (recursion) results: ')
# bruteforce_results = []
# before_bruteforce = time.process_time()
# for job in jobs:
#     bruteforce_results.append(run_bruteforce(job))
# after_bruteforce = time.process_time()

# compare bruteforce results with correct expected results
# compare_results(expected_results, bruteforce_results)

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
print('Dynamic results: ')
before_dyn = time.process_time()
dynamic_results = []
for job in jobs:
    dynamic_results.append(run_dynamic(job))
after_dyn = time.process_time()

# compare dynamic results with correct expected results
compare_results(expected_results, dynamic_results)

# run fptas
print('FPTAS results: ')
before_fptas = time.process_time()
fptas_results = []
for job in jobs:
    result = run_fptas(job, 0.1)
    fptas_results.append(result)
    # calculate mistake
    price = 0
    for i in range(job.item_count):
        if result[3][i] is True:
            price += job.items[i].price
    # price = sum([job.items[i].price for i in range(len(result[3])) if result[3][i] is True])
    expected_price = [res[2] for res in expected_results if res[0] == result[0]][0]
    print("Price:" + str(price) + "   Expected price: " + str(expected_price))
    relative_error = (float(expected_price) - float(price)) / float(expected_price)
    print("Relative error: " + str(relative_error))
after_fptas = time.process_time()


print('\nExecution times:')
print('Branch & Bound: {0:.10f}s'.format(after_bb - before_bb))
print('Dynamic: {0:.10f}s'.format(after_dyn - before_dyn))
print('FPTAS: {0:.10f}s'.format(after_fptas - before_fptas))
