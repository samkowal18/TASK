Update on each task:
Since the initial project plan, we have made progress across all steps from obtaining our data to analysis. Below is an update on each task, along with specific artifacts in our project repository. 
Data acquisition: We identified and downloaded both datasets from the City of Chicago Open Data Portal: The Chicago Crime Data and the Chicago 311 Service Requests data. We reviewed schema for each dataset to understand the key variables like timestamps, crime type, request type, and data completeness. 
Data cleaning and preprocessing: Initial data cleaning has been completed. This includes handling missing values, removing duplicates, and standardizing column names across the datasets for consistency. We also made sure that both datasets use compatible datetime formats for integration. 
Feature engineering: we extracted temporal features from the datetime fields, including year, month, and day of the week. These features are essential for analyzing temporal trends and aligning the datasets for comparison. Additionally, we began to group similar categories as there are some crimes that are less frequent and it can make our approach too broad. 
Exploratory data analysis: Some analysis has been completed to understand the distribution of crime types and service request categories. Summary statistics and frequency counts were generated, and early visualizations were created to identify trends. 
Correlation analysis: We began to explore relationships between crime types and 311 service requests using aggregated temporal data. Initial correlation matrices have been generated at the monthly level, allowing us to identify potential associations between categories. 
Visualization: Several visualizations have been developed to communicate patterns over time and across categories. These include line charts showing trends in crime and service requests, bar charts of category frequencies, and heatmaps illustrating correlations. 
Draft report: A draft of the report has been started, focusing on methodology and early findings from the exploratory analysis. This document will be expanded as additional insights are finalized.
Workflow documentation: We have begun to document the overall workflow, including a diagram that outlines the data pipeline from raw data through analysis and visualization. 

Updated timeline:
Data acquisition: Completed
Data cleaning & preprocessing: Completed
Feature engineering: Completed
Exploratory data analysis: In progress
Complete by: April 17th
Correlation analysis: In progress
Complete by: April 20th
Visualization: In progress
Complete by: April 23rd
Draft Report: Not started
Complete by: April 30th
Submit: Not started
Complete by: May 1st

Changes to the Project Plan:
Since submitting our initial project plan, we have made some adjustments based on our progress and feedback from Milestone 2. 
First, we made a more clear timeline to show when we should complete each task and ensure we’re making progress on the project. We needed to slightly adjust for the complexity of the data cleanup process, which deals with multiple missing values and inconsistencies in labels, making this step take longer than anticipated. 
Next, we narrowed the scope of our analysis to focus on the most frequent and relevant crime types. We originally planned to analyze all categories, but after further reviewing the datasets, we decided that this approach would be too broad and less accurate, since there’s a large number of categories with crimes that are less frequent. Only looking at the most frequent and relevant crimes would be more beneficial and meaningful, producing clearer and more interpretable results. 
We also shifted our focus from looking at analyzing daily, monthly, and yearly trends to just looking at monthly trends, since daily data was too granular and gave us too much extra information, making the data more difficult to interpret. Monthly data is still detailed but can help us interpret it more efficiently. 
We added several visualizations to better recognize patterns in the data. 
Lastly, we clarified how we would measure relationships between crime data and 311 service requests by using correlation analysis over time, instead of simple comparisons, to better assess relationships between variables. 
Overall, these have helped us create a more focused and meaningful project. 

Challenges:
We have encountered a few challenges throughout this project so far. 
One of the main challenges was the large size of the datasets. Both the crime and 311 service request datasets contain a significant number of records, which made the process take longer than expected. We decided to focus on the most frequent and relevant crime types to narrow our scope and make our analysis more detailed. We also filtered the data to make the process more manageable without losing vital information. 
Another challenge was missing and inconsistent data, with unclear labels, similar categories being sometimes labeled differently across datasets, and some missing timestamps. We solved this by cleaning the data, which involved removing missing values when needed and standardizing categories. 
Additionally, we also had a challenge with analyzing the relationship between crime data and 311 service requests. We solved this issue by using a correlation analysis with monthly data instead of daily, which had too much variability and made it difficult to correctly interpret the data. 

Summary:
Sam = For this milestone, I focused on exploratory data analysis and understanding different patterns within the datasets. I looked at potential relationships between crime types and 311 service request categories to identify key trends and areas of focus by using correlation analysis. I also helped adjust the project scope by narrowing the analysis to the most relevant and frequent categories. I helped with the writing part as well, clearly communicating analytical findings and insights.
