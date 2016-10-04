#!/usr/bin/env python3

input_file = 'data/knap_{}.inst.dat'


class KnapsackItem(object):
    def __init__(self, weight, price):
        self.weight = weight
        self.price = price

    @property
    def ratio(self):
        try:
            return self.weight/self.price
        except:
            return 0

    def __str__(self):
        return 'Item w:' + str(self.weight) + ' p:' + str(self.price)


class KnapsackJob(object):
    def __init__(self, id, capacity, items):
        self.id = int(id)
        self.capacity = int(capacity)
        self.items = []
        for i in range(len(items)):
            if i % 2 is 0:
                self.items.append(KnapsackItem(int(items[i]), int(items[i+1])))
            else:
                continue

    def __str__(self):
        return ('Knapsack job ' +
                self.id +
                ' with following items: ' +
                str(self.items))


def get_knapsack_jobs(dataset_size):
    lines = open(input_file.format(dataset_size)).readlines()
    jobs = []
    for line in lines:
        words = line.split()
        jobs.append(KnapsackJob(words[0], words[2], words[3:]))

    return jobs


def report_knapsack_results(job_id, item_count, price_best, items_best):
    print("{} {} {} ".format(job_id,
                             item_count,
                             price_best), end='')
    for val in items_best:
        print(' ' + str(int(val)), end='')

    print()
