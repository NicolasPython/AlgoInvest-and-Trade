#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import itertools


def get_actions_list(data_doc):
    """Load CSV and format data.

    Args:
        data_doc ([.CSV]): [.csv file with invest data]

    Returns:
        [list]: [name, price, profits]
    """
    with open(data_doc) as csv_file:
        csv_list = list(csv.reader(csv_file))
        actions_list = []
        for row in csv_list[1:]:
            if float(row[1]) > 0:
                # Calculate profits
                round_profit = round((float(row[1]) * float(row[2])) / 100, 2)
                # Create a list of all actions if data is usable
                actions_list.append([row[0], float(row[1]), int(round_profit)])
    return actions_list


def force_brute(max_money, elements):
    """Checking every combination and chose the better one.

    Args:
        max_money ([int]): [total money]
        elements ([list]): [the return of get_actions_list()]

    Returns:
        [tuple]: [list of actions, total price, total profits]
    """
    remaining_combinations = []
    length = len(elements)
    i = 1
    # Search every combination of 1:n elements
    while i <= length:
        combination = list(itertools.combinations(elements, i))
        i += 1
        for possibilities in combination:
            price = 0
            profit = 0
            for element in possibilities:
                price += float(element[1])
                profit += float(element[2])
            # Checking if price > max_money and append possibilities
            if price <= float(max_money):
                remaining_combinations.append(
                    {"combination": possibilities, "price": price, "profit": profit}
                )
    #first sort with profit
    sorted_combinations = sorted(
        remaining_combinations, key=lambda k: (k["profit"]), reverse=True
    )
    maximum_profit = sorted_combinations[0]["profit"]
    #make a list with only combinations with best profit
    sorted_combinations = [
        l for l in sorted_combinations if l["profit"] == maximum_profit
    ]
    #second sort with price to get the lowest price in index 0
    sorted_combinations = sorted(sorted_combinations, key=lambda k: k["price"])

    # Organise results for show
    final_combination = (
        f'COMBINATION : {[x[0] for x in sorted_combinations[0]["combination"]]}'
    )
    final_price = f'PRICE : {(sorted_combinations[0]["price"])}'
    final_profits = f'PROFITS : {(sorted_combinations[0]["profit"])}'
    return final_combination, final_price, final_profits

if __name__ == "__main__":
    print(force_brute(500, get_actions_list("actions_premiere_partie.csv")))
