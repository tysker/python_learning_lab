import pandas as pd

SQUIRREL_DATA = "./data/2018_Central_Park_Squirrel_Census_Data.csv"
OUTPUT = "./data/squirrel_count.csv"

# Fur Color, Count
# grey, 2473
# cinnamon, 392
# black, 103

# data = pd.read_csv(SQUIRREL_DATA)
#
# colors = data["Primary Fur Color"]
# targets = ["Gray", "Cinnamon", "Black"]
#
# data_dict = {
#     "Fur color": targets,
#     "Count": [(colors == c).sum() for c in targets],
# }
#
# df = pd.DataFrame(data_dict)
# df.to_csv(OUTPUT)

# or

data = pd.read_csv(SQUIRREL_DATA)

# Normalize names and drop missing values
#
# dropna() = removes missing values
# str = string accessor
# strip() = removes whitespace
colors = data["Primary Fur Color"].dropna().str.strip()

# Count all colors at once
counts = colors.value_counts()

# Filter colors
filtered = counts.loc[["Gray", "Cinnamon", "Black"]]

# Make a dataframe and save
df = filtered.reset_index()
print(df)
df.columns = ["Fur color", "Count"]
df.to_csv(OUTPUT, index=False)

print(df)
