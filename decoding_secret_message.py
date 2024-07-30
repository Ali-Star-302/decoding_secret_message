import pandas as pd
from array import *

def print_grid(array):
    for row in array:
        print(*row)

def main():
    # Read the table from the given url
    url = r'https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub'
    # url = r'https://docs.google.com/document/d/e/2PACX-1vSHesOf9hv2sPOntssYrEdubmMQm8lwjfwv6NPjjmIRYs_FOYXtqrYgjh85jBUebK9swPXh_a5TJ5Kl/pub'
    table = pd.read_html(url, encoding='utf-8')[0]

    # Separate the coordinates and characters into separate arrays by column
    xcoordinates = table.loc[1:,0].array
    characters = table.loc[1:,1].array
    ycoordinates = table.loc[1:,2].array

    # Convert string arrays to int arrays for ease of use
    xcoordinates = [int(string_coord) for string_coord in xcoordinates]
    ycoordinates = [int(string_coord) for string_coord in ycoordinates]

    grid = [['*' for i in range(max(xcoordinates)+1)] for j in range(max(ycoordinates)+1)]

    for x_idx, x_coord in enumerate(xcoordinates):
        grid[max(ycoordinates)-ycoordinates[x_idx]][x_coord] = characters[x_idx]

    print_grid(grid)


if __name__ == "__main__":
    main()