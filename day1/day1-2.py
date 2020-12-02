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
Using the above example again, the three entries that sum to 2020 are 979, 366, and 675.
Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?
"""
import pandas as pd

# load data
#df = pd.DataFrame({'expenses': [1721, 979, 366, 299, 675, 1456]})
df = pd.read_csv("puzzle_inputs/input_day1-1.txt", sep=" ", header=None, names=['expenses'])

expenses_set = set(df.expenses)

for expense in df.expenses:
    x = 2020 - expense
    for y in df.expenses:
        z = x - y
        if y in expenses_set and z in expenses_set:
            solution = expense * y * z
            break
print("The solution is: ", solution)