# Creates a variable with a string "Frankfurter"
title = "Frankfurter"
print(title)

# Creates a variable with an integer 80
years = 80
yr_str = "80"
yr_cst = int("80")
yr_str_cst = str(yr_cst)

print(years)
print(yr_str)
print(yr_cst)
print(yr_str_cst)

# Creates a variable with the boolean value of True
expert_status = True
print(expert_status)

# Prints a statement adding the variable
print("Nick is a professional " + title)

# Convert the integer years into a string and prints
print("He has been coding for " + str(years) + " years")

# Converts a boolean into a string and prints
print("Expert status: " + str(expert_status))

# An f-string accepts all data types without conversion
print(f"Expert status2: {expert_status}")

# Use good naming convention
tbl_ = 'table'
df_tbl_ = 'More than one table combine'
stg_ = 'Staging table'
stg_df_tbl = 'Staging table in a dataflow'

# How to name multiple variables at once
Kendall, Fab, Bryan = "Kendall", "Fab", "Bryan"
print(Kendall)
print(Fab)
print(Bryan)
