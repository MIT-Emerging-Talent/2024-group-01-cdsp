# Raw Datasets
We use an aggregation of two datasets from two different sources: FAO & World Bank.
 
## Source: World Bank
The dataset was retrieved from  Markup :  [the World Bank Open Data platform](https://data.worldbank.org/indicator/SP.URB.TOTL.IN.ZS), specifically from the indicator on urban population (SP.URB.TOTL.IN.ZS) available at the World Bank Urban Population Indicator. The data represents the urban population of different countries over various years, including urban population growth, female population metrics, survival rates, age dependency ratio, death rates, and death registration completeness.
### Structure:
1. Urban Population Growth (Annual%)
2. Population Ages 25-29
3. Female (% of Female Population)
4. Survival to Age 65, Female (% of Cohort)
5. Age Dependency Ratio (% of Working-Age Population)
6. Death Rate, Crude (per 1000 People)
7. Completeness of Death Registration with Cause-of-Death Information (%)
The data is organized chronologically and geographically, presenting trends in urban population dynamics and related indicators across different countries.
### Possible Flaws:
1. Incomplete Data: The completeness of death registration may vary, leading to potential inaccuracies.
2. Data Lag: Reporting delays could affect the timeliness of specific metrics.
3. Methodology Variations: Differences in data collection methods across countries may introduce inconsistencies.
4. Population Bias: Gender-specific metrics may overlook non-binary and diverse gender identities.
### Recreation:
To recreate the dataset, one can access the World Bank Open Data platform, navigate to the Urban Population indicator, select relevant countries and metrics, and export the data in their preferred format for further analysis. Data visualization tools like Python's Matplotlib or Tableau can create visual representations similar to the line graph, bar graph, and map formats provided by the World Bank interface.

## Source: FAO
The dataset was obtained from FAOSTAT's open data platform, accessible at FAOSTAT Open Data. FAOSTAT provides comprehensive information on land use across various categories and elements related to agriculture, forestry, water, and more.
### Structure:
1. Section 1:
   - Contains countries, regions, and special groups.
2. Section 2:
   - Elements include area, carbon stock in living biomass, and various indicators.
3. Section 3:
   - Items and item aggregates cover country area, land area (agriculture, forestland), other land (water, irrigation, agricultural practices, aquaculture and fisheries), and archived data.
4. Section 4:
   - Encompasses years from 1961 to 2021.
### Possible Flaws:
1. Data Completeness: Incomplete or missing data may impact analysis and interpretations.
2. Measurement Variability: Varied data collection methods might introduce inconsistencies.
3. Aggregation Errors: Incorrect data aggregation across different categories could lead to inaccuracies.
4. Data Formatting: The choice of output format (CSV or XLS) could affect data readability and analysis.
### Recreation:
- Visit Markup :  [the FAOSTAT website](https://www.fao.org/faostat/en/#data/RL), and access the desired land use dataset.
- Select relevant categories and elements based on countries, regions, or particular groups.
- Choose the desired output (table or pivot) and file type (CSV or XLS).
- Customize the data view with formatting options like comma separation, period separation, etc.
- Select the elements and sections of interest to view or download the data.
