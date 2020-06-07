# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(obj, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse iterable non-string object as csv into a list of records
    '''

    if isinstance(obj, str):
        raise RuntimeError("obj must be an interable non-string object")

    if select and has_headers == False:
        raise RuntimeError("select argument requires column headers")

    rows = csv.reader(obj, delimiter=delimiter)

    if has_headers:
        # Read the file headers
        headers = next(rows)

    # If a column selector was given, find indices of the specified columns.
    # Also narrow the set of headers used for resulting dictionaries
    if select:
        indices = [headers.index(colname) for colname in select]
        headers = select

    records = []
    for i, row in enumerate(rows):
        try:
            if not row:     # Skip rows with no data
                continue

            # Filter the row if specific columns were selected
            if select:
                row = [row[index] for index in indices]
            # Convert values if types were specified
            if types:
                row = [func(val) for func, val in zip(types, row)]

            if has_headers:
                # Make a dictionary
                record = dict(zip(headers, row))
            else:
                # Make a tuple
                record = tuple(row)
        except ValueError as e:
            if not silence_errors:
                print(f'Row {i}: Couldn\'t convert {row}\nRow {i}: Reason: {e}')
            continue

        records.append(record)

    return records