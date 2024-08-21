# -*- coding: utf-8 -*-
"""Phi - SS5.7.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zF4HnsOtTmt4LWgeEnYgarcSZFFWEn1-

# **My ETL process**

Let write my own etl process

## **1. Install and import libraries**"""

"""Import libraries"""

# Import libraries
import pandas as pd
from sqlalchemy import create_engine
import pymysql
import requests
import os

def download_csv_from_github(url):
    '''
    Function to download the CSV file from GitHub and save it in
    the same directory as the current Python file, using the original 
    filename from the URL.
    Args:
    url: URL of the CSV file on GitHub.
    '''

    # Determine current directory path
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Extract original file name from URL
    filename = url.split('/')[-1]

    # Generate full path for destination file
    filepath = os.path.join(current_dir, filename)

    # Send request to download and save file
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        print(f"Okela: {filepath}")
    else:
        print(f"Oops: {response.status_code}")

if 'VSCODE_PID' in os.environ: # If programming with vscode environment then download the csv files below
    download_csv_from_github("https://raw.githubusercontent.com/phiphi522001/My-etl-process/main/enrollees_data.csv")
    download_csv_from_github("https://raw.githubusercontent.com/phiphi522001/My-etl-process/main/enrollees_education.csv")
    download_csv_from_github("https://raw.githubusercontent.com/phiphi522001/My-etl-process/main/work_experience.csv")

"""## **2. ETL process**

### **2.1. Extract data**

Extract the data from data sources listed above
"""

# Load enrollees data to dataframe
enrollees_df = pd.read_csv('https://raw.githubusercontent.com/phiphi522001/My-etl-process/main/enrollees_data.csv')

# Load enrollees education data to dataframe
enrollees_education_df = pd.read_csv('https://raw.githubusercontent.com/phiphi522001/My-etl-process/main/enrollees_education.csv')

# Load work experience data to dataframe
work_experience_df = pd.read_csv('https://raw.githubusercontent.com/phiphi522001/My-etl-process/main/work_experience.csv')

# Create connection to company_course database
engine = create_engine('mysql+pymysql://etl_practice:550814@112.213.86.31:3360/company_course')
training_hours_df = pd.read_sql_table('training_hours', con=engine) # Load training_hours table's data to dataframe
employment_df = pd.read_sql_table('employment', con=engine) # Load employment table's data to dataframe

# Read the html tables
tables = pd.read_html('https://sca-programming-school.github.io/city_development_index/index.html')
cdi_df = tables[0] # Load data of tables[0] to df

"""### **2.2. Transform data**

#### **2.2.1. Enrollees data**

##### **2.2.1.1. Data profiling**

Display 10 random rows in dataframe
"""

enrollees_df.sample(10)

"""Display basic info"""

enrollees_df.info()

"""Summary statistics for numerical and non-numerical columns"""

enrollees_df.describe(include='object')

"""Number of missing values and duplicate rows"""

enrollees_df.isnull().sum()

"""##### **2.2.1.2. Fixing data types**"""

enrollees_df = enrollees_df.convert_dtypes()
enrollees_df.info()

"""##### **2.2.1.3. Checking consistency**

Checking consistency for `gender` column
"""

enrollees_df['gender'].unique()

"""##### **2.2.1.4. Handling missing values**

Handling missing values for gender column
"""

enrollees_df['gender'].fillna(enrollees_df['gender'].mode()[0], inplace=True)
enrollees_df['gender'].info()

"""Check again how many rows are duplicated"""

enrollees_df.duplicated().sum()

"""#### **2.2.2. Enrollees education**

##### **2.2.2.1. Data profiling**
"""

enrollees_education_df.sample(10)

enrollees_education_df.info()

enrollees_education_df.describe(include='object')

enrollees_education_df.isnull().sum()

"""##### **2.2.2.2. Fixing data types**"""

enrollees_education_df = enrollees_education_df.convert_dtypes()
enrollees_education_df.info()

"""##### **2.2.2.3. Checking consistency**"""

enrollees_education_df['enrolled_university'].unique()

enrollees_education_df['education_level'].unique()

enrollees_education_df['major_discipline'].unique()

"""##### **2.2.2.4. Handling missing values**"""

enrollees_education_df['enrolled_university'].fillna(enrollees_education_df['enrolled_university'].mode()[0], inplace=True)
enrollees_education_df['enrolled_university'].info()

enrollees_education_df['education_level'].fillna(enrollees_education_df['education_level'].mode()[0], inplace=True)
enrollees_education_df['education_level'].info()

enrollees_education_df['major_discipline'].fillna(enrollees_education_df['major_discipline'].mode()[0], inplace=True)
enrollees_education_df['major_discipline'].info()

enrollees_education_df.duplicated().sum()

"""#### **2.2.3. Training hours**

##### **2.2.3.1. Data profiling**
"""

training_hours_df.sample(10)

training_hours_df.info()

training_hours_df.describe()

training_hours_df.duplicated().sum()

"""##### **2.2.3.2. Removing outliers**"""

# Quartiles calcualtion
Q1 = training_hours_df['training_hours'].quantile(0.25)
Q3 = training_hours_df['training_hours'].quantile(0.75)

# IQR calculation
IQR = Q3 - Q1

# Lower and Upper bounds for non-outliers calculating
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

cond1 = training_hours_df['training_hours'] >= lower_bound
cond2 = training_hours_df['training_hours'] <= upper_bound

training_hours_df_clean = training_hours_df[cond1 & cond2]

training_hours_df_clean.info()

"""#### **2.2.4. Work experience**

##### **2.2.4.1. Data profiling**
"""

work_experience_df.sample(10)

work_experience_df.info()

work_experience_df.describe(include='object')

"""##### **2.2.4.2. Fixing data types**"""

work_experience_df = work_experience_df.convert_dtypes()
work_experience_df.info()

"""##### **2.2.4.3. Checking consistency**"""

work_experience_df['relevent_experience'].unique()

work_experience_df['experience'].unique()

work_experience_df['company_size'].unique()

work_experience_df['company_type'].unique()

work_experience_df['last_new_job'].unique()

"""##### **2.2.4.4. Handling missing values**"""

work_experience_df['relevent_experience'].fillna(work_experience_df['relevent_experience'].mode()[0], inplace=True)
work_experience_df['relevent_experience'].info()

work_experience_df['experience'].fillna(work_experience_df['experience'].mode()[0], inplace=True)
work_experience_df['experience'].info()

work_experience_df['company_size'].fillna(work_experience_df['company_size'].mode()[0], inplace=True)
work_experience_df['company_size'].info()

work_experience_df['company_type'].fillna(work_experience_df['company_type'].mode()[0], inplace=True)
work_experience_df['company_type'].info()

work_experience_df['last_new_job'].fillna(work_experience_df['last_new_job'].mode()[0], inplace=True)
work_experience_df['last_new_job'].info()

work_experience_df.duplicated().sum()

"""#### **2.2.5. City development**

##### **2.2.5.1. Data profiling**
"""

cdi_df.sample(10)

cdi_df.info()

cdi_df.describe()

"""##### **2.2.5.2. Removing outliers**"""

Q1 = cdi_df['City Development Index'].quantile(0.25)
Q3 = cdi_df['City Development Index'].quantile(0.75)

# IQR calculation
IQR = Q3 - Q1

# Lower and Upper bounds for non-outliers calculating
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

cond1 = cdi_df['City Development Index'] >= lower_bound
cond2 = cdi_df['City Development Index'] <= upper_bound

cdi_df_clean = cdi_df[cond1 & cond2]

cdi_df_clean.info()

"""#### **2.2.6. Employment data**

##### **2.2.6.1. Data profiling**
"""

employment_df.sample(10)

employment_df.info()

employment_df.duplicated().sum()

"""### **2.3. Load data into warehouse**

After data transforming, we load the data into the warehouse. Our warehouse database is located here:

Host: `112.213.86.31`\
Port: `3360`\
Login: `etl`\
Password: `488579`\
Database name: `data_warehouse`\
Create another MySQL connection to load data into warehouse:
"""

# Create an engine object to connect to the database
warehouse_engine = create_engine('mysql+pymysql://etl:488579@112.213.86.31:3360/data_warehouse')

"""Then write dataframes into the warehouse database using the `to_sql()` method:"""

# Write dataframes to database
enrollees_df.to_sql('dim_enrollees', con=warehouse_engine, if_exists='replace', index=False)
enrollees_education_df.to_sql('dim_enrollees_education', con=warehouse_engine, if_exists='replace', index=False)
training_hours_df_clean.to_sql('fact_training_hours', con=warehouse_engine, if_exists='replace', index=False)
work_experience_df.to_sql('dim_work_experience', con=warehouse_engine, if_exists='replace', index=False)
cdi_df_clean.to_sql('dim_cdi', con=warehouse_engine, if_exists='replace', index=False)
employment_df.to_sql('fact_employment', con=warehouse_engine, if_exists='replace', index=False)