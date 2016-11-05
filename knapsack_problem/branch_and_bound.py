#!/usr/bin/env python3

import itertools

from dataio import *


def run_bb(job):
    def bb_step(items_used, current_price, current_weight):
        nonlocal items_best
        nonlocal price_best

        # stop recursion if max depth was reached
        if len(items_used) == item_count:
            return

        # stop recursion if better results are not possible
        possible_price = current_price + remaining_prices[len(items_used)]
        if possible_price < price_best:
            return

        # add next item
        new_price = current_price + job.items[len(items_used)].price
        new_weight = current_weight + job.items[len(items_used)].weight
        # stop recursion if max capacity would be reached
        if new_weight <= job.capacity:
            # set a new best
            if new_price > price_best:
                items_best = items_used + [True]
                price_best = new_price
            bb_step(items_used + [True],
                    new_price,
                    new_weight)

        # do NOT add next item
        bb_step(items_used + [False],
                current_price,
                current_weight)

    item_count = len(job.items)
    price_best = 0
    items_best = []

    # get remaining prices array
    remaining_prices = [0] * item_count
    remaining_prices[item_count-1] = job.items[item_count-1].price
    for i in range(item_count-1-1, 0, -1):
        remaining_prices[i] = remaining_prices[i+1] + job.items[i].price

    bb_step([], 0, 0)

    # append False until items_best lenght is correct
    while len(items_best) < item_count:
        items_best.append(False)

    # print results
    report_knapsack_results(job.id, item_count, price_best, items_best)

    return ((job.id, item_count, price_best, items_best))
