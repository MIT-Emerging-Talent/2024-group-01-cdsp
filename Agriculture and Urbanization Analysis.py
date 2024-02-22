import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('darkgrid')
sns.set_palette('Set2')
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn import metrics
from sklearn.preprocessing import scale
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# importing land dataset
land= pd.read_csv("https://raw.githubusercontent.com/MIT-Emerging-Talent/2024-group-01-cdsp/main/data/Inputs_LandUse_E_All_Data_(Normalized).csv")

# having a view on the data
land.head()

# getting the data structure and types
land.info()

# getting a list of rows grouping (CSV levels)
land['Item'].unique()

land.isnull().sum()
# checking if any field is null

# selecting only the data under the Agriculutral land category
land = land[land["Item"]=="Agricultural land"]
land

# Creating a pivot table to transform the years from rows into columns to normalize the dataset + adding the column 'Area' which has the countries names
# land = land[['Area', 'Year', 'Value']]
land = land.pivot_table(values='Value', index='Area', columns=['Year'], aggfunc='first')
land['Area'] = land.index
land.head()

land.index

# New Section

# importing the urbanization dataset
urban= pd.read_csv("https://raw.githubusercontent.com/MIT-Emerging-Talent/2024-group-01-cdsp/main/data/Worldbank%20urbanization%20data-CSV.csv",header=2)
urban

# renaming the column containing the names of the countries to Area in accordance with the land dataset
urban = urban.rename(index={'Country Name': 'Area'})
urban = urban.rename(columns={'Country Name': 'Area'})
urban


urban.set_index("Area", inplace = True)
urban.index

# drop replications
land = land.drop_duplicates()
urban = urban.drop_duplicates()

#merging
agriculture = pd.merge(urban, land, left_index=True, right_on='Area')
agriculture.head()
