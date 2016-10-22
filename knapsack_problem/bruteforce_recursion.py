#!/usr/bin/env python3

import itertools

from dataio import *


def run_bruteforce(job):
    def bruteforce_step(items_used, current_price, current_weight):
        nonlocal items_best
        nonlocal price_best

        # stop recursion if max depth was reached
        if len(items_used) == item_count:
            return

        # do NOT add next item
        bruteforce_step(items_used + [False],
                current_price,
                current_weight)

        # add next item
        new_price = current_price + job.items[len(items_used)].price
        new_weight = current_weight + job.items[len(items_used)].weight
        # stop recursion if max capacity is reached
        if new_weight > job.capacity:
            return
        # set a new best
        if new_price > price_best:
            items_best = items_used + [True]
            price_best = new_price
        bruteforce_step(items_used + [True],
                new_price,
                new_weight)

    item_count = len(job.items)
    price_best = 0
    items_best = []

    bruteforce_step([], 0, 0)

    # append False until items_best lenght is correct
    while len(items_best) < item_count:
        items_best.append(False)

    # print results
    report_knapsack_results(job.id, item_count, price_best, items_best)

    return ((job.id, item_count, price_best, items_best))
