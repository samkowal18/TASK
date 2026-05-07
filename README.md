# Temporal Patterns and Relationships Between Crime and 311 Service Requests in Chicago
## Contributors
Avery Terri
* Data collection and acquisition
* Data profiling and documentation
* Data quality assessment
* Data cleaning and preprocessing
* Feature engineering
  
Sam Kowal
* Exploratory data analysis
* Correlation Analysis attempt and Limitation documentation
* Interpretation of results
* Report writing (findings & solutions)
* Visualizations and output tables

## Project Summary
The goal of this project is to analyze patterns in public safety and community service activity in Chicago using datasets from
the city of [Chicago Open Data Portal](https://data.cityofchicago.org/). Specifically, this project explores how reported crime incidents 
and 311 service requests* vary over time and whether there are observable relationships between different types of crime and types
of service requests. 

Understanding these relationships is important because both datasets reflect different aspects of urban life. Crime data captures
reported public safety incidents, while 311 service requests represent non-emergency concerns reported by residents, like infrastructure
issues or environmental concerns. By examining both, this project aims to identify patterns that may suggest connections between community
conditions and public safety trends. 

The **primary research questions** for this analysis are:
* Are there observable correlations between specific types of crime and specific 311 service requests?
* How do crime incidents and service requests vary over time (monthly)?

To address these questions, both datasets were cleaned, standardized, and transformed to enable comparison. Temporal features such as
year and month were extracted from time fields, and categorical variables were simplified to focus on the most relevant and frequent
categories. The datasets were then aggregated at the monthly level, allowing for consistent comparison and reducing noise present in daily
data. 

Preliminary analysis focused on identifying distributions of crime types and service request categories, as well as examining trends over time.
Correlation analysis was performed on aggregated monthly data to explore potential relationships between categories across datasets. 

Overall, this projects aims to provide insight into how patterns in public service requests and crime reports may be related, while also
highlighting the limitations of working with large, real-world urban datasets. 

## Storage and Organization

To support reproducibility and clarity, the project follows a structured design: 
```
data/
├── raw/             
│   ├── chicago_crime.csv
│   └── chicago_311.csv
├── processed/
│   ├── crime_clean.csv
│   └── 311_clean.csv    
             
outputs/
├── figures/         
├── tables/           

README.md
requirements.txt
```

Raw datasets are stored in data/raw and are never edited directly. All preprocessing steps are performed through scripts in the
scripts/ folder, and outputs are stored in the data/processed/ and outputs/ folder. This separation ensures transparency and allows
the entire workflow to be reproduced. 

## Data Description and Profiling
### Dataset #1: Chicago Crime Data
**Source:** [Chicago Open Data Portal](https://data.cityofchicago.org/)

* Search "Crime"
* Select *Crimes - 2001 to present*
* Filter for desired time frame (using 2025-2026 for this project)

**Acquisition:** 

Downloaded a CSV file and stored in data/raw/chicago_crime.csv

**Coverage:**

This dataset includes reported crime incidents in Chicago from 2001 to the present, with each row representing a single
incident. For this analysis, we will be using data from May 2025-May 2026. 

**Format:**

CSV (tabular)

**Variables Used:**

- **date:** Date when the incident occured. It's sometimes a best estimate. 
- **primary_type:** The primary description of the IUCR (Illinois Uniform Crime Reporting code) code

**Description:**

The dataset provides detailed records of reported crimes, allowing analysis of how different types of incidents vary over time.
Only temporal and categorical variables were used in this project to maintain focus on trends rather than spatial analysis. 

**Ethical Considerations:**

Although the dataset is anonymized, it represents real-world incidents. Additionally, it only includes reported crimes. Meaning that
the data may not fully refelct actual crime rates. 

____
### Dataset #2: Chicago 311 Service Requests
**Source:** [Chicago Open Data Portal](https://data.cityofchicago.org/)

* Search "311"
* Select *311 Service Requests*
* Filter for desired time frame (using 2025-2026 for this project)
  
**Acquisition:**

Downloaded a CSV file and stored in data/raw/chicago_311.csv

**Coverage:**

This dataset contains non-emergency service requests submitted by residents, including issues such as potholes, sanitation, and infrastructure
maintenance. For this analysis, we will be using data from May 2025-May 2026.

**Format:**

CSV (tabular)

**Variables:**

- **CREATED_DATE:** When the incident was reported.
- **SR_TYPE:** Description of the incident.

**Description:**

Each record represents a request submitted by a resident. The dataset reflects patterns in community concerns and engagement over time.

**Ethical Considerations:**

Data is anonymized and publicly available. However, it does reflect citizen reporting behavior, which may vary accross communities and introduce
bias. Areas with higher engagement may appear to have more issues simply due to increased reporting.

____
**Dataset Integration**

The datasets were integrated through temporal aggregation, using shared datetime fields. Both datasets were aligned at the monthly level, allowing comparison
of:
* Crime frequency by type
* Service request frequency by type

Because there is no shared unique identifier, integration was performed through aggregation rather than direct joins. 

## Data Quality Assessment

Data Quality was assessed through inspection and summary statistics during preprocessing. 

**Completeness**

Both datasets contained missing values, particularly in timestamp fields. Since temporal analysis is central to the project,
records with missing values were removed. Cateogrical variables were largely complete, though some contained ambiguous or missing labels.

**Consistency**

There were inconsistencies in column naming conventions and category labels accross datasets. Similar categories were sometimes
labeled differently, requiring standardization before analysis.

**Accuracy**

Some timestamp values were improperly formatted or invalid. These were identified during conversion to datetime format and removed when necessary.

**Class Imbalance**

A small number of categories dominated both datasets. For example, certain crime types and service request categories appeared much more
frequently than others. This imbalance made it difficult to analyze less common categories and influenced the decision to focus on the most
frequent types.

**Bias and Limitations**

Both datasets are subject to reporting bias:
* Crime data includes only reported incidents
* 311 data depends on citizen reporting behavior

Additionally, inconsistencies in reporting frequency and timing introduced variability in the data. Aggregating data at the monthly level helped reduce
noise and improve interpretability. 

## Data Cleaning

Data Cleaning was performed using Python scripts to ensure consistency and usability accross both datasets.

**Column Standardization:**

Column names were converted to lowercase and formatted consistently to allow easier processing and integration.

**Handling Missing Values:**

Rows with missing or invalid timestamps were removed, as they could not be used in temporal analysis. 
Missing categorical values were either removed or grouped where appropriate.

**Duplicate Removal:**

Duplicate records were removed to prevent double-counting and ensure accurate aggregation.

**Datetime Conversion:**

Timestamp fields were converted into a consistent datetime format. This step was essential
for extracting temporal features and aligning the datasets.

**Feature Engineering:**

New variables were created from timestamps, including:

* year
* month
* day of week

These features enabled aggregation and trend analysis.

**Category Standardization:**

Similar categories were grouped together to reduce redundancy and improve clarity. 
Less frequent categories were consolidated to focus the analysis on meaningful patterns.

**Filtering:**

Both datasets were filtered to include only the most frequent and relevant categories. 
This reduced noise and improved computational efficiency.

## Findings
The analysis explored patterns in Chicago crime reports and 311 service requests using cleaned datasets aggregated by category and month. Exploratory data analysis was used to identify the most common categories in each dataset and compare monthly patterns over time.

For crime reports, the most frequent categories were theft, battery, criminal damage, assault, motor vehicle theft, other offense, deceptive practice, burglary, narcotics, and criminal trespass. Theft was the most common crime category, with 24,939 records, followed by battery with 20,215 records. These results suggest that a small number of categories account for a large share of reported crime incidents in the dataset.

For 311 service requests, the most frequent category was “311 INFORMATION ONLY CALL,” with 303,884 records. This was followed by aircraft noise complaints, graffiti removal requests, garbage cart maintenance, rodent baiting/rat complaints, abandoned vehicle complaints, tree debris clean-up requests, tree emergencies, pothole complaints, and water in basement complaints. The large number of information-only calls suggests that many 311 records reflect general resident inquiries rather than only infrastructure or maintenance problems.

The monthly trend analysis showed that the two datasets did not fully cover the same time period. The 311 service request data covered May 2025 through October 2025, while the crime data mainly covered October 2025 through April 2026. Because of this, the combined monthly trend chart shows 311 activity concentrated in earlier months and crime activity concentrated in later months. Only October 2025 appears in both datasets.

Correlation analysis was attempted by aggregating both datasets at the monthly level and comparing category counts over time. However, the cleaned crime and 311 datasets only shared one overlapping month: October 2025. Since correlation analysis requires multiple shared time periods, meaningful category-level correlations could not be calculated from the current files. As a result, the analysis focused on descriptive findings, including the most common categories and monthly patterns within each dataset.

Overall, the findings show that both datasets provide useful information about public safety and community concerns in Chicago, but the lack of overlapping months limits the ability to analyze relationships between crime and 311 service requests. Future analysis could improve this by using datasets with the same date range or by collecting a longer shared time period for both crime incidents and 311 service requests.

## Challenges
One major challenge was aligning the two datasets over time. Although both datasets relate to public activity in Chicago, they did not fully cover the same months after cleaning. The 311 service request data covered May 2025 through October 2025, while the crime data mainly covered October 2025 through April 2026. This meant that only October 2025 appeared in both datasets.

This lack of overlap limited the planned correlation analysis. Since correlation requires multiple shared time points, meaningful correlations between crime categories and 311 service request categories could not be calculated. Instead, the project focused on descriptive analysis, including the most common categories and monthly trends within each dataset.

Another challenge was working with large real-world datasets that contained imbalanced categories. A few categories appeared much more often than others, which made it necessary to focus on the top categories for clearer analysis and visualization.

## Future Work

Future work could improve this project by using crime and 311 service request datasets that cover the exact same time period. A longer shared time range would allow for more meaningful correlation analysis and stronger comparisons between public safety incidents and community service requests.

Another improvement would be to analyze the data at the daily or weekly level instead of only at the monthly level. This could provide more detailed insight into whether certain service request patterns appear before or after changes in crime reports. However, this would also require careful handling of noise and missing data.

Future analysis could also include geographic information, such as community areas, wards, or police districts. Adding location-based analysis would make it possible to examine whether certain neighborhoods experience stronger relationships between crime reports and 311 service requests.

Finally, future versions of the project could include additional datasets, such as weather, public transit activity, or socioeconomic indicators, to better understand outside factors that may influence both crime and resident service requests.

## Visualizations

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
plt.show()

## Reproducing

To reproduce the analysis:

1. Install the required Python packages listed in `requirements.txt`.

2. Make sure the cleaned datasets are saved in the following locations:

   - `data/processed/crime_clean.csv`
   - `data/processed/service_clean.csv`

3. Run the analysis script from the main project folder:

```bash
python notebooks/analysis.py




