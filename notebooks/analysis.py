import pandas as pd
import matplotlib.pyplot as plt
import os

# Create output folders
os.makedirs("outputs/figures", exist_ok=True)
os.makedirs("outputs/tables", exist_ok=True)

#Load cleaned data
crime = pd.read_csv("data/processed/crime_clean.csv")
service = pd.read_csv("data/processed/service_clean.csv")

print("Crime data preview:")
print(crime.head())

print("\n311 service data preview:")
print(service.head())

#Top crime categories
crime_top = crime["category"].value_counts().head(10)

print("\nTop Crime Categories:")
print(crime_top)

crime_top.to_csv("outputs/tables/top_crime_categories.csv")

plt.figure(figsize=(10, 6))
crime_top.plot(kind="bar")
plt.title("Top 10 Crime Categories")
plt.xlabel("Crime Category")
plt.ylabel("Count")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("outputs/figures/top_crime_categories.png")
plt.close()

#Top 311 service request categories
service_top = service["category"].value_counts().head(10)

print("\nTop 311 Service Request Categories:")
print(service_top)

service_top.to_csv("outputs/tables/top_311_categories.csv")

plt.figure(figsize=(10, 6))
service_top.plot(kind="bar")
plt.title("Top 10 311 Service Request Categories")
plt.xlabel("311 Service Request Category")
plt.ylabel("Count")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("outputs/figures/top_311_categories.png")
plt.close()

#Monthly trends
crime["month"] = crime["month"].astype(str)
service["month"] = service["month"].astype(str)

crime_monthly = crime.groupby("month").size()
service_monthly = service.groupby("month").size()

monthly_trends = pd.DataFrame({
    "crime_count": crime_monthly,
    "service_request_count": service_monthly
}).fillna(0)

print("\nMonthly Trends:")
print(monthly_trends)

monthly_trends.to_csv("outputs/tables/monthly_trends.csv")

plt.figure(figsize=(10, 6))
monthly_trends.plot()
plt.title("Monthly Trends in Crime and 311 Service Requests")
plt.xlabel("Month")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("outputs/figures/monthly_trends.png")
plt.close()

#Correlation analysis limitation
common_months = set(crime["month"]).intersection(set(service["month"]))

print("\nCommon months between crime and 311 data:")
print(common_months)

if len(common_months) < 2:
    print("Not enough overlapping months to calculate meaningful correlations.")

    correlation_limitation = pd.DataFrame({
        "common_months": [", ".join(sorted(common_months))],
        "issue": ["Not enough overlapping months"],
        "explanation": [
            "The crime and 311 datasets only share one overlapping month. "
            "Because correlation analysis requires multiple shared time periods, "
            "meaningful correlations could not be calculated."
        ]
    })

    correlation_limitation.to_csv(
        "outputs/tables/correlation_limitation.csv",
        index=False
    )

else:
    crime_pivot = crime.pivot_table(
        index="month",
        columns="category",
        aggfunc="size",
        fill_value=0
    )

    service_pivot = service.pivot_table(
        index="month",
        columns="category",
        aggfunc="size",
        fill_value=0
    )

    crime_pivot.columns = [str(col) + "_crime" for col in crime_pivot.columns]
    service_pivot.columns = [str(col) + "_311" for col in service_pivot.columns]

    combined = crime_pivot.join(service_pivot, how="inner")

    correlation_matrix = combined.corr()
    correlation_matrix.to_csv("outputs/tables/correlation_matrix.csv")

    corr_pairs = correlation_matrix.stack().reset_index()
    corr_pairs.columns = ["variable_1", "variable_2", "correlation"]

    corr_pairs = corr_pairs[
        (corr_pairs["variable_1"].str.endswith("_crime")) &
        (corr_pairs["variable_2"].str.endswith("_311"))
    ]

    top_correlations = corr_pairs.sort_values(
        by="correlation",
        ascending=False
    ).head(20)

    top_correlations.to_csv("outputs/tables/top_correlations.csv", index=False)

print("\nAnalysis complete. Outputs saved to outputs/figures and outputs/tables.")
