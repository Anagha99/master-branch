#!/usr/bin/env python3


input_string = """Number of employees: 6

Goodies and Prices:

Fitbit Plus: 7980
IPods: 22349
MI Band: 999
Cult Pass: 2799
Macbook Pro: 229900
Digital Camera: 11101
Alexa: 9999
Sandwich Toaster: 2195
Microwave Oven: 9800
Scale: 4999
"""


def parse_data(input_lines):
    
    m = int(input_lines[0].split(":")[-1].strip())
    items = []
    prices = []

    for item in input_lines[4:]:
        if item:
            name = item.split(':')[0]
            price = int(item.split(':')[1].strip())

            items.append([name, price])
    return m, items



def find_gudie(items, m):
    difference = None
    start_gudie = None

    for index, item in enumerate(items):
        if index + (m - 1) >= len(items):
            break

        if difference is None:
            start_gudie = 0
            difference = items[m -1][1] - items[0][1]
            continue
        if items[index + m -1][1] - items[index][1] < difference:
            start_gudie = index
            difference = items[index + m -1][1] - items[index][1]

    return start_gudie, difference



def write_output(items, m, start_guddie, difference):
    with open("output.txt", "w") as f:
        print("The goodies selected for distribution are:\n", file=f)
        for item in items[start_guddie:start_guddie+m]:
            print("{}: {}".format(item[0], item[1]), file=f)
        print(f"\nAnd the difference between the chosen goodie with highest price and the lowest price is {difference}", file=f)



if __name__ == '__main__':
    # m = number of employees
    # items = list of guddie, price
    input_data = open("input.txt").readlines()

    m, items = parse_data(input_data)

    n = len(items)  # number of items

    # sort items by price
    items.sort(key=lambda x: x[1])
    start_guddie, difference = find_gudie(items, m)
    write_output(items, m, start_guddie, difference)


