# Author: Lesley Miller
# Date: 2020/12/02
"""
For example, suppose your expense report contained the following:
1721
979
366
299
675
1456
In this list, the two entries that sum to 2020 are 1721 and 299.
Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to 2020;
what do you get if you multiply them together?
"""

# import packages
import pandas as pd

# load puzzle input
test_df = pd.DataFrame({'expenses': [1721, 979, 366, 299, 675, 1456]})
df = pd.read_csv("puzzle_inputs/input_day1-1.txt", sep=" ", header=None, names=['expenses'])

expenses_set = set(df.expenses)

for expense in df.expenses:
    x = 2020 - expense
    if x in expenses_set:
        solution = x * expense
        break

print("The solution is: ", solution)
