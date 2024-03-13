import csv
from itertools import islice

filename = 'train.csv'

csv.field_size_limit(1000000000)

def fix_nulls(s):
    for line in s:
        yield line.replace('\0', ' ')

def lazy_print(s):
    for line in s:
        yield line

def yield_from_index(csv_reader):
    for row in csv_reader:
        yield row

with open(filename, 'r+') as f:
    reader = csv.reader(fix_nulls(f))
    for item in islice(yield_from_index(reader), 2002, 4000):
        print(len(item))

