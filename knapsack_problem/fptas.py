#!/usr/bin/env python3

import copy

from dataio import *
from dynamic import *


def run_fptas(job, eps):
    job_copy = copy.deepcopy(job)
    c_max = max([item.price for item in job_copy.items])
    k = float(eps)*float(c_max)/float(job_copy.item_count)

    for item in job_copy.items:
        item.price = int(float(item.price)/float(k))
        # print(item.price)

    return run_dynamic(job_copy)
