import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Select the column interested, in sample, target_col is number of days of xxx
df_subset = df.select("target_col").filter("target_col >= 0") 

# convert to pandas
df_pd = df_subset.toPandas()

# Print descriptive statis for the column
stats = df_pd['target_col'].describe()

# Filter only first 20 days (days 0 to 19, sample data very sparse after 20 days)
df_pd = df_pd[df_pd['target_col'] < 20] 

# Set the visual style and figure size
sns.set_style("whitegrid")
plt.figure(figsize=(10,6)) 

# Create the histogram for the distribution with a separate bin for each day
sns.histplot(
    data = df.pd,
    x="target_col", 
    bins=range(0,21)
    color="blue",
    alpha=0.7
)

# Print the general stats
print(stats)

# Add titles and lables
plt.title("Distribution of target_col", fontsize=16)
plt.xlabel("xxxxx", fontsize=14)
plt.ylable("Frequency", fontsize=14)

plt.show()
