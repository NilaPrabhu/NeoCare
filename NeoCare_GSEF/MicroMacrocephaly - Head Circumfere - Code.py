# Micro & Macrocephaly - Head Circumference for Age Experiment

import pandas as pd
import numpy as np
import scipy.stats as stats

# CDC Growth Chart Data for Females and Males
# Source: https://www.cdc.gov/growthcharts/data/set1clinical/cj41c020.pdf
# The data below represents the mean and standard deviation for head circumference at various ages for females and males

# Female data (in cm)
female_data = {
    "Age (months)": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    "Mean": [34.9, 36.5, 37.8, 38.9, 39.8, 40.5, 41.1, 41.6, 42.0, 42.4, 42.7, 43.0, 43.3],
    "SD": [1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3]
}

# Male data (in cm)
male_data = {
    "Age (months)": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    "Mean": [35.8, 37.4, 38.6, 39.6, 40.5, 41.2, 41.9, 42.4, 42.9, 43.3, 43.6, 43.9, 44.2],
    "SD": [1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3]
}

# Convert to DataFrame
df_female = pd.DataFrame(female_data)
df_male = pd.DataFrame(male_data)

# Function to classify head circumference
def classify_head_circumference(age_months, head_circumference, sex):
    """
    Classify head circumference as microcephaly, macrocephaly, or normal based on CDC growth charts.
    
    Parameters:
    age_months (int): Age of the child in months
    head_circumference (float): Measured head circumference in cm
    sex (str): Sex of the child ('Male' or 'Female')
    
    Returns:
    str: Classification result
    """

    # Select the appropriate dataset based on sex
    if sex.lower() == 'female':
        df = df_female
    elif sex.lower() == 'male':
        df = df_male
    else:
        return "Invalid sex"

    # Get the mean and standard deviation for the given age
    if age_months in df['Age (months)'].values:
        mean = df[df['Age (months)'] == age_months]['Mean'].values[0]
        sd = df[df['Age (months)'] == age_months]['SD'].values[0]
    else:
        return "Age not in dataset"

    # Calculate the standard deviation difference
    sd_diff = (head_circumference - mean) / sd

    # Classify based on standard deviation difference
    if sd_diff < -2:
        return "Microcephaly"
    elif sd_diff > 2:
        return "Macrocephaly"
    else:
        return "Normal"

# Experiment: Female, 4 months old, Head Circumference 38 cm, Expected Output: Normal 
# result = classify_head_circumference(4, 38, "Female")

# Experiment: Female, 2 months old, Head Circumference 60 cm, Expected Output: Macrocephaly 
result = classify_head_circumference(2, 60, "Female")

print(f"Micro & Macrocephaly - Head Circumference for Age Experiment is {result}.")

