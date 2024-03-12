# Project 1 - COMP4010
Project 1 for the course COMP4010 - Data Visualization

## Group member
|Name   |Student ID   |E-mail   |
|-------|-------------|---------|
|Hoang Trung Thanh   |V202100516   |21thanh.ht@vinuni.edu.vn   |
|Tran Tue Nhi   |V202000079   |20nhi.tt@vinuni.edu.vn  |
|Nguyen Minh Tuan   |V202000254   |20tuan.nm@vinuni.edu.vn   |

## Dataset chosen and reason to choose

We choose the dataset (2023-06-06 - Energy Data) for the first project. We choose this dataset as it has a wide range of data, and the correlation between features in the dataset is very intriguing to investigate. Furthermore, this is extremely relevant to the current global landscape, where energy consumption as well as emissions are highly concerned with by many people and instituions, as well as governments.

## Brief introduction and dimensions of the dataset

This dataset is collected from Our World in Data. It contains data on energy consumption, energy mix, electricity mix of different countries over years.

The relevant dimension in the datasets are:
- Country: The country of interest
- Year: Year of observation
- Population: Population of that country
- GDP: Total Gross Domestic Product of a country
- Biofuel/Coal/Fossil Fuel/gas/Hydro/Low Carbon/Nuclear/Oil/Solar/Wind etc. -> share of energy consumption/electricity generation/per capita generation/ etc. : Data on specific type of energy on specific metric.

## Two questions to be answered:
- What is the **scale** and **structure** of electricity generation of the 5 countries with the highest **(energy consumption/electricity generation/gdp)** and the world (Possibly in year 2023) ?
- What is the **scale** and **structure** of Vietnam's electricity generation over the past decade in energy generation ?

## Plans for answering each question
**Question 1**: The variables included in the dataset are: Country, GDP, Total Energy Consumption/Generation and percentage of energy generation for each type electricity generation. We will likely create a stacked bar chart for each country. If we plan to create a chart for a specific year (2023), then we will take the statistics of that year, or else we will create a new column which averages over the past decade for each country.

**Question 2**: The variables included in the dataset are: Country, Year, Total Energy Consumption/Generation and percentage of energy generation for each type electricity generation.
We have two plans for this:
- 1. Create a stacked bar chart for each year's electrical generation, in which each strip is a type of electricity generation.
- 2. Create a stacked bar chart/clustered column chart for each year's electrical generation in renewable versus non-renewable energy used in electrical generation. This will require us to create a new column in which the total non-renewable and renewable energy generation will be calculated as the sum of all renewable/non-renewable energy source used.
