# Author: Lesley Miller
# Date: 2020/12/02

"""
For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc

Each line gives the password policy and then the password. The password policy indicates
the lowest and highest number of times a given letter must appear for the password to be valid.
For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not;
it contains no instances of b,
but needs at least 1. The first and third passwords are valid: they contain one a or nine c,
both within the limits of their respective policies.

How many passwords are valid according to their policies?
"""

# import packages
import pandas as pd

#df = pd.DataFrame({'database': ['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']})
df = pd.read_csv('puzzle_inputs/day2.txt', sep="\t", header=None, names=['database'])


valid_passwords = 0
for master_string in df.database:
    policy = master_string.split()[0].split('-')
    letter = master_string.split()[1].replace(':', '')
    password = master_string.split()[2]
    num_count = password.count(letter)

    if num_count >= int(policy[0]) and num_count <= int(policy[1]):
        valid_passwords += 1

print("Soultion is: ", valid_passwords)
