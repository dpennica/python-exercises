# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import sys
import sqlite3 as lite
from pandas import ExcelWriter
from pandas import ExcelFile
import pandas as pd

# %%
df = pd.read_excel(
    "./global_database_power_plants/global_power_plant_database.xlsx", sheet_name="Sheet1")

# %%
country_set = set(df["country"])

# %%
try:
    con = lite.connect("gbpower.db")

    c = con.cursor()
    for country in country_set:
        c.execute("INSERT INTO country( country ) VALUES (?)", [country, ])
        con.commit()
except lite.Error as e:
    print("Error %s:" % e.args[0])
    sys.exit(1)
finally:
    if con:
        con.close()


# %%
gp_df = df[["name", "latitude", "longitude"]]


# %%
gp_df = gp_df.rename(columns={"latitude": "lat", "longitude": "lng"})


# %%
try:
    con = lite.connect("gbpower.db")

    gp_df.to_sql('global_power_location', con, if_exists='replace')
except lite.Error as e:
    print("Error %s:" % e.args[0])
    sys.exit(1)
finally:
    if con:
        con.close()
