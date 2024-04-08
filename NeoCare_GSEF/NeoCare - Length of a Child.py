# Prerequisites 
# Install matplotlib pandas for generating visualization 
# pip install matplotlib pandas

# Mathematical Representation 
# 

# LaTeX notation for the equation  
# \[ \text{closest\_age} = a_j \text{ where } j = \underset{i}{\text{arg min}} \, |a_i - \text{age}| \]
# 
# Python Code 

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

# Female data (in cm)
cdc_data_female = {
    "Age": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    "Mean": [34.9, 36.5, 37.8, 38.9, 39.8, 40.5, 41.1, 41.6, 42.0, 42.4, 42.7, 43.0, 43.3],
    "SD": [1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3]
}

# Male data (in cm)
cdc_data_male = {
    "Age": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    "Mean": [35.8, 37.4, 38.6, 39.6, 40.5, 41.2, 41.9, 42.4, 42.9, 43.3, 43.6, 43.9, 44.2],
    "SD": [1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3]
}

# Load the CDC data for males and females
# cdc_data_male = pd.read_csv('cdc_data_male.csv')
# cdc_data_female = pd.read_csv('cdc_data_female.csv')

# Conduct Tests / Load Data 

# Load the CDC data for males and females
# Assuming the data files are named 'cdc_data_male.csv' and 'cdc_data_female.csv'
# cdc_data_male = pd.read_csv('cdc_data_male.csv')
# cdc_data_female = pd.read_csv('cdc_data_female.csv')

# Find Percentile 
result = find_percentile(70, 2, 'male', cdc_data_male, cdc_data_female)
print(f"The child is in the {result}th percentile for their length and age.")

# Generate Plot Growth 

percentile = plot_growth(70, 24, 'male', cdc_data_male, cdc_data_female)
print(f"The child is in the {percentile}th percentile for their length and age.")

