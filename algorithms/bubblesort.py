#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Jul-13-19 18:02
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org

import os
import random
import pysnooper
import time
import csv

from quicksort import quicksort


def bubblesort(l: list):
    for i in range(len(l)):
        for j in range(i, len(l)):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]
    return l


def main():
    """
    bubblesort的时间复杂度是O(n^2)
    quicksort的时间复杂度是O(nlogn)
    """
    # csv_path = "./bubblesort.csv"
    csv_path = "./quicksort.csv"

    nsample = 1
    N = list(range(10, 10000, 10))
    avg_elapsed = 0
    for n in N:
        for _ in range(nsample):
            l = [random.randint(0, 10000) for _ in range(n)]
            start = time.clock()
            # bubblesort(l)
            quicksort(l)
            elapsed = (time.clock() - start)
            # print("Time used:", elapsed)
            avg_elapsed += elapsed
        avg_elapsed /= nsample
        print("n:", n)
        print("Average time used:", avg_elapsed)

        if not os.path.exists(csv_path):
            f = open(csv_path, "w")
            f_csv = csv.writer(f)
            f_csv.writerow(["N", "avg_elapsed"])
            f_csv.writerow((n, avg_elapsed))
        else:
            f = open(csv_path, "a")
            f_csv = csv.writer(f)
            f_csv.writerow((n, avg_elapsed))
        avg_elapsed = 0


if __name__ == "__main__":
    main()
