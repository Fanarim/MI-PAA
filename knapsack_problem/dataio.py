#!/usr/bin/env python3

input_file = 'data/knap_{}.inst.dat'


class KnapsackItem(object):
    def __init__(self, weight, price):
        self.weight = weight
        self.price = price

    @property
    def ratio(self):
        try:
            return self.price/self.weight
        except:
            return 0

    def __str__(self):
        return 'Item w:' + str(self.weight) + ' p:' + str(self.price) + ' r:'\
               + str(self.ratio)


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


def get_expected_results(dataset_size):
    expected_results = []
    with open('solutions/knap_{}.sol.dat'.format(dataset_size)) as inf:
        for line in inf.readlines():
            id, item_count, price = line.split()[:3]
            used_items = line.split()[3:]
            for i in range(len(used_items)):
                if used_items[i] == '1':
                    used_items[i] = True
                else:
                    used_items[i] = False

            expected_results.append((int(id),
                                     int(item_count),
                                     int(price),
                                     tuple(used_items)))
    return expected_results


def compare_results(expected_results, actual_results):
    correct = True
    for i in range(len(expected_results)):
        if not (expected_results[i][0] == actual_results[i][0] and
                expected_results[i][1] == actual_results[i][1] and
                expected_results[i][2] == actual_results[i][2]):
            correct = False
            print('Invalid result for job #{}: '
                  .format(expected_results[i][0]))
            print(expected_results[i], actual_results[i])
    return correct


def report_knapsack_results(job_id, item_count, price_best, items_best):
    print("{} {} {} ".format(job_id,
                             item_count,
                             price_best), end='')
    for val in items_best:
        print(' ' + str(int(val)), end='')

    print()
