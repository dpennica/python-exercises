#!/usr/bin/env python

# In[1]:
import csv

# In[11]:
import xlsxwriter

# In[33]:
# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook(
    './global_database_power_plants/global_power_plant_database.xlsx')

# In[34]:
worksheet = workbook.add_worksheet()


# In[35]:

with open("./global_database_power_plants/global_power_plant_database.csv") as csvfile:
    # Start from the first cell. Rows and columns are zero indexed.
    row_num = col_num = 0
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        for item in row:
            worksheet.write(row_num, col_num, item)
            col_num += 1
        row_num += 1
        col_num = 0


# In[36]:
workbook.close()
