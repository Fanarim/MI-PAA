#!/usr/bin/env python3

from dataio import *


def run_dynamic(job):
    price_sum = sum([item.price for item in job.items])

    # [items_analyzed][price_of_added_items] = weight_of_added_items
    dynamic_array = [[0 for i in range(price_sum + 1)] for i in range(job.item_count + 1)]

    def get_best_price():
        for i in range(price_sum + 1, -1, -1):
            if dynamic_array[job.item_count][i-1] != 0:
                return i - 1

    def add_item(pos_x, pos_y):
        pos_x_new = pos_x + 1
        # current price + price of added item
        pos_y_new = pos_y + job.items[pos_x + 1 - 1].price

        # calculate new weight - weight of items added till now + new item's weight
        new_weight = dynamic_array[pos_x][pos_y] + job.items[pos_x_new - 1].weight
        if new_weight > job.capacity:
            return
        # weight that might be calculated before for another combination of items
        pos_new_weight = dynamic_array[pos_x_new][pos_y_new]

        # if current solution is better (weight is lower)
        if pos_new_weight == 0 or pos_new_weight > new_weight:
            # set new weight
            dynamic_array[pos_x_new][pos_y_new] = new_weight

            # run another recursion step
            dynamic_step(pos_x_new, pos_y_new)

    def not_add_item(pos_x, pos_y):

        # calculate new weight
        current_weight = dynamic_array[pos_x][pos_y]
        pos_new_weight = dynamic_array[pos_x + 1][pos_y]
        if current_weight < pos_new_weight or pos_new_weight == 0:
            # print("Do not add item --" + str(pos_x) + "--: [" + str(pos_x+1) + "][" + str(pos_y) + "] = " + str(current_weight))
            dynamic_array[pos_x + 1][pos_y] = current_weight
            dynamic_step(pos_x + 1, pos_y)

    def dynamic_step(pos_x, pos_y):
        """Run a single recursion step

        Args:
            pos_x: number of items analyzed
            pos_y: total price of added items
        """
        # print(pos_x, pos_y)
        # stop if all items were analyzed
        if pos_x == job.item_count:
            return

        add_item(pos_x, pos_y)
        not_add_item(pos_x, pos_y)

    result = dynamic_step(0, 0)
    # print(dynamic_array)
    print("Total price: " + str(get_best_price()))
