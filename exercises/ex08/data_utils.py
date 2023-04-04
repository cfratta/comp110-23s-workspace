"""EX08 - Data Wrangling!"""

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read csv file and return as a list of dicts with header keys."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], header: str) -> list[str]:
    """Returns values in a table column under a specific header."""
    result: list[str] = []
    # step through table
    for row in table:
        # save every value under key "header"
        result.append(row[header])
    return result


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Reformats data so that it's a dictionary with coulmn headers as keys."""
    result: dict[str, list[str]] = {}
    # loop through keys of one row of table
    first_row: dict[str, str] = table[0]
    for key in first_row:
        # for each key, make a dictionary entry with all column values
        result[key] = column_values(table, key)
    return result


def head(columns: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Return a table with specified number of rows for each column."""
    first_rows: dict[str, list[str]] = {}
    for key in columns:
        n_values: list[str] = []
        idx: int = 0
        if rows >= len(columns):
            return columns
        while idx < rows:
            n_values.append(columns[key][idx])  # columns[key] is a list so I can use subscription
            idx += 1
        first_rows[key] = n_values
    return first_rows


def select(table: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Returns a table with specified columns."""
    new_table: dict[str, list[str]] = {}
    for item in columns:
        new_table[item] = table[item]
    return new_table


def concat(d_one: dict[str, list[str]], d_two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combine two column-based tables (dictionaries) into one."""
    d_concat: dict[str, list[str]] = {}
    for key in d_one:
        d_concat[key] = d_one[key]
    for key in d_two:
        if key in d_concat:
            d_concat[key] += d_two[key]
        else:
            d_concat[key] = d_two[key]
    return d_concat


def count(values: list[str]) -> dict[str, int]:
    """Tally the frequencies of items in a dictionary."""
    frequencies: dict[str, int] = {}
    for item in values:
        if item in frequencies:  # item already established
            frequencies[item] += 1
        else:
            frequencies[item] = 1
    return frequencies
