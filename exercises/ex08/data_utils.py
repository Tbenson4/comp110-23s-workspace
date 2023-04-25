"""EX08 - Data Wrangling."""

__author__ = "730480987"

from csv import DictReader

def head(filename: str) -> list[dict[str, str]]:
    """Read csv file and return as a list of dicts with header keys."""
    result: list[dict[str,str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result

def select(table: list[dict[str, str]], column: str) -> list[str]:
    """Returns values in a table column under a specific header."""
    result: list[str] = []
    #step through table
    for row in table:
        #save every value under key "header"
        item: str = row[column]
        result.append(item)
    return result

def concat(row_table: list[dict[str, str]]) -> dict[str, list[str]]: 
    """Reformats data so that it's a dictionary with column headers as keys"""
    result: dict[str, list[str]] = {}
    # loop through keys of one row of table
    first_row: dict[str,str] = row_table[0]
    for key in first_row:
        # for each key, make a dictionary entry with all column values
        result[key] = select(row_table, key)
    return result