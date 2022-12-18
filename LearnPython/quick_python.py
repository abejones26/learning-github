# # Loop through a range of numbers (0 through 4)
# for x in range(5):
#     print(x)

# print("-----------------------------------------")

# Loop through a range of numbers (2 through 6 - yes 6! Up to, but not including, 7)
# for x in range(2, 7):
#     print(x)

# print("----------------------------------------")

# Iterate through letters in a string
# word = ["Peace", "World"]
# for letters in word:
#     print(letters)

# print("----------------------------------------")

# # Iterate through a list
# zoo = ["cow", "dog", "bee", "zebra"]
# for animal in zoo:
#     print(animal)

# print("----------------------------------------")

# # Loop while a condition is being met
# run = "y"

# while run == "y":
#     print("Hi!")
#     run = input("To run again. Enter 'y'")

# old_name = ['Abe', 'Kendall', 'Fab', 'John']

# new_name = []

# for name in old_name:
#     # print(name)
#     new_name.append(f'{name} Jones')
#     print(new_name)

import pandas as pd

# Dataframe = ['dfm1_', 'dfm2_']
# Dataflow = '[dfw_]'

# table = 'tbl_'
# staging = 'stg_'
# reporting = 'rpt_'

# stg_tbl_dfw_testing = 'some table'

dfm1 = {
    'First Name': [],
    'Last Name': []
}

first_name = ['Abe', 'Bryan', 'Fab', 'Kendall', 'Marshall']

for name in first_name:
    dfm1['First Name'].append(name)
    dfm1['Last Name'].append('Jones')

dfm2 = pd.DataFrame(dfm1)

dfm3 = {
    'First Name': [],
    'Last Name': []
}

count = 0

# for name in dfm2.iterrows():
# print(name)

for index, row in dfm2.iterrows():
    count += 1
    if row[1] == 'Jones':
        dfm3['First Name'].append(row[0])
        dfm3['Last Name'].append(f'{row[1]}{count}')

dfm3 = pd.DataFrame(dfm3)

dfm4 = {
    'First Name': [],
    'Last Name': [],
    'Full Name': []
}

for index2, row2 in dfm2.iterrows():
    # print('Startpoint-----------------------------------------------------')
    firstName = row2[0]
    for index3, row3 in dfm3.iterrows():
        # print(f'First Loop: {row2[0]}')
        # print(f'Second Loop: {row3[0]}')
        # print('Endpoint-------------------------------------------------------')
        secondName = row3[1]
    dfm4['First Name'].append(firstName)
    dfm4['Last Name'].append(secondName)
    dfm4['Full Name'].append(f'{firstName} {secondName}')

print(pd.DataFrame(dfm4))
