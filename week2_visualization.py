print("WEEK 2 - DATA VISUALIZATION")
print("COVID-19 Data Analysis Project")
print("My Python project is ready!")

import pandas as pd

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
file_path = "archive (1)/covid_19_clean_complete.csv"

df = pd.read_csv(file_path)

print("\nCSV FILE SUCCESSFULLY LOADED!")
print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

# Prepare data for graph
daily_cases = df.groupby("Date")["Confirmed"].sum().tail(10)

# Convert dates to text labels
dates = daily_cases.index.astype(str)

# Create bar graph
plt.figure(figsize=(10, 5))
plt.bar(dates, daily_cases.values)

plt.title("COVID-19 Confirmed Cases - Last 10 Dates")
plt.xlabel("Date")
plt.ylabel("Total Confirmed Cases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("covid_last_10_dates.png")
plt.show()

# Top 10 countries by confirmed cases
country_cases = (
    df.groupby("Country/Region")["Confirmed"]
    .max()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10, 5))
plt.bar(country_cases.index, country_cases.values)

plt.title("Top 10 Countries by Confirmed COVID-19 Cases")
plt.xlabel("Country")
plt.ylabel("Confirmed Cases")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("top_10_countries.png")
plt.show()

# Dataset Summary
print("\n===== COVID-19 DATA ANALYSIS SUMMARY =====")

print("\nTotal Countries/Regions:")
print(df["Country/Region"].nunique())

print("\nTotal Confirmed Cases in Dataset:")
print(df["Confirmed"].sum())

print("\nTotal Deaths in Dataset:")
print(df["Deaths"].sum())

print("\nTop 5 Countries by Confirmed Cases:")
print(
    df.groupby("Country/Region")["Confirmed"]
    .max()
    .sort_values(ascending=False)
    .head(5)
)

print("\n===== ANALYSIS COMPLETED =====")




