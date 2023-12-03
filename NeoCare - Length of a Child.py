# Prerequisites 
# Install matplotlib pandas for generating visualization 
# pip install matplotlib pandas

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def find_percentile(length, age, sex, cdc_data_male, cdc_data_female):
    if sex == 'male':
        data = cdc_data_male
    else:
        data = cdc_data_female

    closest_age = data['Age'].iloc[(data['Age']-age).abs().argsort()[:1]].values[0]
    age_data = data[data['Age'] == closest_age]

    for col in age_data.columns[1:]:
        if length <= age_data[col].values[0]:
            percentile = int(col.strip('%'))
            return percentile, closest_age
    
    return 100, closest_age
# end Def find_percentile 

def plot_growth(length, age, sex, cdc_data_male, cdc_data_female):
    percentile, closest_age = find_percentile(length, age, sex, cdc_data_male, cdc_data_female)
    data = cdc_data_male if sex == 'male' else cdc_data_female

    plt.figure(figsize=(10, 6))
    for col in data.columns[1:]:
        plt.plot(data['Age'], data[col], label=f"{col} Percentile")

    plt.scatter([closest_age], [length], color='red', label='Child\'s Length')
    plt.title(f"Child's Growth Chart (Sex: {sex}, Age: {age})")
    plt.xlabel('Age (Months)')
    plt.ylabel('Length (cm)')
    plt.legend()
    plt.grid(True)
    plt.show()

    return percentile
# end Def plot_growth 

# Load the CDC data for males and females
cdc_data_male = pd.read_csv('cdc_data_male.csv')
cdc_data_female = pd.read_csv('cdc_data_female.csv')

# Conduct Tests / Load Data 

# Load the CDC data for males and females
# Assuming the data files are named 'cdc_data_male.csv' and 'cdc_data_female.csv'
cdc_data_male = pd.read_csv('cdc_data_male.csv')
cdc_data_female = pd.read_csv('cdc_data_female.csv')

# Find Percentile 
result = find_percentile(70, 2, 'male', cdc_data_male, cdc_data_female)
print(f"The child is in the {result}th percentile for their length and age.")

# Generate Plot Growth 

percentile = plot_growth(70, 24, 'male', cdc_data_male, cdc_data_female)
print(f"The child is in the {percentile}th percentile for their length and age.")

