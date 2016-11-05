#!/usr/bin/env python3

from dataio import *


def run_dynamic(job):
    price_sum = sum([item.price for item in job.items])

    # [items_analyzed][(price_of_added_items,items_added_mask)] = weight_of_added_items
    dynamic_array = [[[0, False] for i in range(price_sum + 1)] for i in range(job.item_count + 1)]

    def get_best_solution():
        best_price = 0
        best_items = []
        for i in range(price_sum + 1, -1, -1):
            if dynamic_array[job.item_count][i - 1][0] != 0:
                best_price = i - 1
                break

        x = job.item_count
        y = best_price
        while x != 0 and y != 0:
            current_item_used = dynamic_array[x][y][1]
            best_items.append(current_item_used)
            if current_item_used:
                y -= job.items[x-1].price
                x -= 1
            else:
                x -= 1

        while len(best_items) != job.item_count:
            best_items.append(False)
        return (best_price, best_items[::-1])



    def add_item(pos_x, pos_y):
        pos_x_new = pos_x + 1
        # current price + price of added item
        pos_y_new = pos_y + job.items[pos_x + 1 - 1].price

        # calculate new weight - weight of items added till now + new item's weight
        new_weight = dynamic_array[pos_x][pos_y][0] + job.items[pos_x_new - 1].weight
        if new_weight > job.capacity:
            return
        # weight that might be calculated before for another combination of items
        pos_new_weight = dynamic_array[pos_x_new][pos_y_new][0]

        # if current solution is better (weight is lower)
        if pos_new_weight == 0 or pos_new_weight > new_weight:
            # set new weight
            dynamic_array[pos_x_new][pos_y_new][0] = new_weight

            # set items used mask
            dynamic_array[pos_x_new][pos_y_new][1] = dynamic_array[pos_x][pos_y][1]
            dynamic_array[pos_x_new][pos_y_new][1] = True

            # run another recursion step
            dynamic_step(pos_x_new, pos_y_new)

    def not_add_item(pos_x, pos_y):

        # calculate new weight
        current_weight = dynamic_array[pos_x][pos_y][0]
        pos_new_weight = dynamic_array[pos_x + 1][pos_y][0]
        if current_weight < pos_new_weight or pos_new_weight == 0:
            # set new weight
            dynamic_array[pos_x + 1][pos_y][0] = current_weight

            # set items used mask
            dynamic_array[pos_x + 1][pos_y][1] = dynamic_array[pos_x][pos_y][1]
            dynamic_array[pos_x + 1][pos_y][1] = False

            # run next recursion step
            dynamic_step(pos_x + 1, pos_y)

    def dynamic_step(pos_x, pos_y):
        """Run a single recursion step

        Args:
            pos_x: number of items analyzed
            pos_y: total price of added items
        """
        # stop if all items were analyzed
        if pos_x == job.item_count:
            return

        add_item(pos_x, pos_y)
        not_add_item(pos_x, pos_y)

    dynamic_step(0, 0)
    price_best, items_best = get_best_solution()
    report_knapsack_results(job.id, job.item_count, price_best, items_best)
    return (job.id, job.item_count, price_best, items_best)
