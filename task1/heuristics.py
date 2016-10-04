#!/usr/bin/env python3

import itertools

from dataio import *


def run_heuristics(jobs):
    results = []
    print('Heuristics results: ')
    for job in jobs:
        item_count = len(job.items)

        price = 0
        weight = 0
        items = [False for x in range(item_count)]

        # create array with (original position, item) tuples
        items_positions = []
        for i in range(item_count):
            items_positions.append((i, job.items[i]))

        # sort job items by weight/price ratio descending
        items_positions_sorted = sorted(items_positions,
                                        key=lambda x: x[1].ratio,
                                        reverse=True)

        # calculate which items should be used using simple heuristics
        for item in items_positions_sorted:
            if weight + item[1].weight < job.capacity:
                weight += item[1].weight
                price += item[1].price
                items[item[0]] = True

            if weight == job.capacity:
                break

        # print results
        report_knapsack_results(job.id, item_count, price, items)

        results.append((job.id, item_count, price, items))

    print()
    return results
