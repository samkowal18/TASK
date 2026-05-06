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
* Correlation Analysis
* Interpretation of results
* Report writing (findings & solutions)

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
* Filter for desired time frame

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
* Filter for desired time frame
  
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


