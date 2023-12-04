import pandas as pd

# Load the provided CDC growth chart data for male and female babies
file_male = '/mnt/data/Male Babibes - Data Table of Infant Weight-for-age Charts.csv'
file_female = '/mnt/data/Female Babibes - Data Table of Infant Weight-for-age Charts.csv'

male_growth_chart = pd.read_csv(file_male)
female_growth_chart = pd.read_csv(file_female)

# Displaying the first few rows of each dataset to understand their structure
male_growth_chart.head(), female_growth_chart.head()

# Model for Prader-Willi syndrome  
def check_prader_willi_risk(age_months, weight_kg, sex, male_chart, female_chart):
    """
    Check if a baby's weight for their age is indicative of Prader-Willi syndrome risk.

    :param age_months: Age of the baby in months.
    :param weight_kg: Weight of the baby in kilograms.
    :param sex: Sex of the baby ('Male' or 'Female').
    :param male_chart: DataFrame with growth chart data for males.
    :param female_chart: DataFrame with growth chart data for females.
    :return: Risk assessment based on weight for age.
    """
    # Selecting the appropriate chart based on sex
    chart = male_chart if sex == 'Male' else female_chart

    # Finding the closest age row in the chart
    closest_age_row = chart.iloc[(chart['Age (in months)'] - age_months).abs().argsort()[:1]]

    # Checking if the weight is significantly below the average for the age
    if weight_kg < closest_age_row['3rd Percentile Weight (in kilograms)'].values[0]:
        return "High risk of Prader-Willi syndrome (weight significantly below average)"
    elif weight_kg < closest_age_row['10th Percentile Weight (in kilograms)'].values[0]:
        return "Potential risk of Prader-Willi syndrome (weight below average)"
    else:
        return "Low risk of Prader-Willi syndrome based on weight (within normal range)"

# Applying the function to the provided case: a 2-month-old male baby weighing 7 kg
prader_willi_risk = check_prader_willi_risk(2, 7, 'Male', male_growth_chart, female_growth_chart)
prader_willi_risk

# RESULT
# 'Low risk of Prader-Willi syndrome based on weight (within normal range)'

# Model for multiple_cases of Prader-Willi syndrome  
# Creating a function to process multiple cases at once
def process_multiple_cases(cases, male_chart, female_chart):
    """
    Process multiple cases to check for Prader-Willi syndrome risk based on weight for age.

    :param cases: A list of dictionaries, each containing age, weight, and sex of the subjects.
    :param male_chart: DataFrame with growth chart data for males.
    :param female_chart: DataFrame with growth chart data for females.
    :return: A list of risk assessments for each subject.
    """
    results = []
    for case in cases:
        risk = check_prader_willi_risk(case['age_months'], case['weight_kg'], case['sex'], male_chart, female_chart)
        results.append({'age_months': case['age_months'], 'weight_kg': case['weight_kg'], 'sex': case['sex'], 'risk': risk})
    
    return results

# Defining the sample cases
sample_cases = [
    {'age_months': 1, 'weight_kg': 2.5, 'sex': 'Female'},
    {'age_months': 6, 'weight_kg': 4, 'sex': 'Male'},
    {'age_months': 24, 'weight_kg': 14, 'sex': 'Female'},
    {'age_months': 72, 'weight_kg': 30, 'sex': 'Male'},
    {'age_months': 120, 'weight_kg': 50, 'sex': 'Female'}
]

# Processing the sample cases
results = process_multiple_cases(sample_cases, male_growth_chart, female_growth_chart)
results

#Result 
"""
    Result
    [{'age_months': 1,
    'weight_kg': 2.5,
    'sex': 'Female',
    'risk': 'High risk of Prader-Willi syndrome (weight significantly below average)'},
    {'age_months': 6,
    'weight_kg': 4,
    'sex': 'Male',
    'risk': 'High risk of Prader-Willi syndrome (weight significantly below average)'},
    {'age_months': 24,
    'weight_kg': 14,
    'sex': 'Female',
    'risk': 'Low risk of Prader-Willi syndrome based on weight (within normal range)'},
    {'age_months': 72,
    'weight_kg': 30,
    'sex': 'Male',
    'risk': 'Low risk of Prader-Willi syndrome based on weight (within normal range)'},
    {'age_months': 120,
    'weight_kg': 50,
    'sex': 'Female',
    'risk': 'Low risk of Prader-Willi syndrome based on weight (within normal range)'}]
"""

# Code to generate the plot 
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# Load the baseline graph image
img = mpimg.imread('/mnt/data/Prader-Willi syndrome Baseline Graph.png')

# Define the subject data based on the age (in months) and weight (in kg)
subjects = [
    {'age_months': 1, 'weight_kg': 2.5, 'label': '1-month-old Female'},
    {'age_months': 6, 'weight_kg': 4, 'label': '6-month-old Male'},
    {'age_months': 24, 'weight_kg': 14, 'label': '24-month-old Female'},
    {'age_months': 72, 'weight_kg': 30, 'label': '72-month-old Male'},
    {'age_months': 120, 'weight_kg': 50, 'label': '120-month-old Female'}
]

# Display the baseline graph
fig, ax = plt.subplots(figsize=(12, 10))
ax.imshow(img, extent=[0, 24, 0, 18])  # Set the extent to match the age (months) and weight (kg) scale of the image

# Plot the subjects on the graph
for subject in subjects:
    ax.plot(subject['age_months'], subject['weight_kg'], 'ro')  # 'ro' is for red color and circle markers
    ax.text(subject['age_months'], subject['weight_kg'], subject['label'], fontsize=9, ha='right')

# Set the title and labels
ax.set_title('Subjects Plotted on Prader-Willi Syndrome Baseline Graph')
ax.set_xlabel('Age (Months)')
ax.set_ylabel('Weight (Kg)')

# Show the plot with subjects
plt.show()

