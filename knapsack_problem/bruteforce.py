#!/usr/bin/env python3

import itertools

from dataio import *


def run_bruteforce(jobs):
    results = []
    print('Bruteforce results:')
    for job in jobs:
        item_count = len(job.items)

        price_best = 0
        items_best = []

        # generate all possible items combinations
        # (array of True/False values, where True indicates items was used)
        items_used_vectors = list(itertools.product([True, False],
                                                    repeat=item_count))

        # for every items conbination
        for items_used_vector in items_used_vectors:
            price = 0
            weight = 0

            # calculate price and weight
            for i in range(item_count):
                if items_used_vector[i]:
                    weight += job.items[i].weight
                    price += job.items[i].price

            # update current best if necessary
            if weight <= job.capacity and price > price_best:
                price_best = price
                items_best = items_used_vector

        # print results
        report_knapsack_results(job.id, item_count, price_best, items_best)

        results.append((job.id, item_count, price_best, items_best))

    print()
    return results
