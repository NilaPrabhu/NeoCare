def diagnose_syndromes(age_months, length_cm, weight_kg, sex, head_circumference_cm):
    """
    Diagnose potential syndromes based on child's measurements and CDC data.

    :param age_months: Age of the child in months.
    :param length_cm: Length of the child in centimeters.
    :param weight_kg: Weight of the child in kilograms.
    :param sex: Sex of the child ('Male' or 'Female').
    :param head_circumference_cm: Head circumference of the child in centimeters.
    :return: A dictionary indicating potential matches with syndromes.
    """

    results = {
        'Turner Syndrome': False,
        'Prader-Willi Syndrome': False,
        'Microcephaly': False,
        'Macrocephaly': False
    }

    # Handling edge cases where age is out of the data range
    if age_months >= 24 or age_months < 0:
        return "Age is out of the expected range (0-23 months)."

    # Fetching relevant data from CDC dataset
    cdc_row = cdc_data.loc[cdc_data['Age'] == age_months]

    # Check for Turner Syndrome (Length < 5th Percentile)
    length_percentile_key = f'{sex}_Length_5th_Percentile'
    if length_cm < cdc_row[length_percentile_key].values[0]:
        results['Turner Syndrome'] = True

    # Check for Prader-Willi Syndrome (Weight > 95th Percentile)
    weight_percentile_key = f'{sex}_Weight_95th_Percentile'
    if weight_kg > cdc_row[weight_percentile_key].values[0]:
        results['Prader-Willi Syndrome'] = True

    # Check for Microcephaly & Macrocephaly (Head Circumference outside 2SD)
    head_circumference_key = f'{sex}_HeadCircumference_2SD'
    if head_circumference_cm < cdc_row[head_circumference_key].values[0] - 2:
        results['Microcephaly'] = True
    elif head_circumference_cm > cdc_row[head_circumference_key].values[0] + 2:
        results['Macrocephaly'] = True

    return results

# Example usage of the function
example_result = diagnose_syndromes(age_months=12, length_cm=70, weight_kg=10, sex='Male', head_circumference_cm=45)
example_result

"""
OUTPUT
{'Turner Syndrome': False,
 'Prader-Willi Syndrome': True,
 'Microcephaly': False,
 'Macrocephaly': True}
"""

# NeoScore -- Predictive Score 

def calculate_neoscore(age_months, length_cm, weight_kg, sex, head_circumference_cm, cdc_data):
    """
    Calculate the NeoScore for various syndromes based on child's measurements and CDC data.

    :param age_months: Age of the child in months.
    :param length_cm: Length of the child in centimeters.
    :param weight_kg: Weight of the child in kilograms.
    :param sex: Sex of the child ('Male' or 'Female').
    :param head_circumference_cm: Head circumference of the child in centimeters.
    :param cdc_data: CDC data DataFrame.
    :return: A dictionary indicating potential matches with syndromes and their NeoScores.
    """
    results = {
        'Turner Syndrome': {'Flag': False, 'Score': 0},
        'Prader-Willi Syndrome': {'Flag': False, 'Score': 0},
        'Microcephaly': {'Flag': False, 'Score': 0},
        'Macrocephaly': {'Flag': False, 'Score': 0}
    }

    # Handling edge cases where age is out of the data range
    if age_months >= 24 or age_months < 0:
        return "Age is out of the expected range (0-23 months)."

    # Fetching relevant data from CDC dataset
    cdc_row = cdc_data.loc[cdc_data['Age'] == age_months]

    # Turner Syndrome Check
    length_percentile_key = f'{sex}_Length_5th_Percentile'
    if length_cm < cdc_row[length_percentile_key].values[0]:
        results['Turner Syndrome']['Flag'] = True
        deviation_percentage = (cdc_row[length_percentile_key].values[0] - length_cm) / cdc_row[length_percentile_key].values[0]
        results['Turner Syndrome']['Score'] = min(100, max(0, deviation_percentage * 100))

    # Prader-Willi Syndrome Check
    weight_percentile_key = f'{sex}_Weight_95th_Percentile'
    if weight_kg > cdc_row[weight_percentile_key].values[0]:
        results['Prader-Willi Syndrome']['Flag'] = True
        deviation_percentage = (weight_kg - cdc_row[weight_percentile_key].values[0]) / weight_kg
        results['Prader-Willi Syndrome']['Score'] = min(100, max(0, deviation_percentage * 100))

    # Microcephaly & Macrocephaly Check
    head_circumference_key = f'{sex}_HeadCircumference_2SD'
    if head_circumference_cm < cdc_row[head_circumference_key].values[0] - 2:
        results['Microcephaly']['Flag'] = True
        deviation_percentage = (cdc_row[head_circumference_key].values[0] - 2 - head_circumference_cm) / head_circumference_cm
        results['Microcephaly']['Score'] = min(100, max(0, deviation_percentage * 100))
    elif head_circumference_cm > cdc_row[head_circumference_key].values[0] + 2:
        results['Macrocephaly']['Flag'] = True
        deviation_percentage = (head_circumference_cm - cdc_row[head_circumference_key].values[0] - 2) / head_circumference_cm
        results['Macrocephaly']['Score'] = min(100, max(0, deviation_percentage * 100))

    return results

# Testing the function with the same example case
neoscore_result = calculate_neoscore(age_months=12, length_cm=70, weight_kg=10, sex='Male', head_circumference_cm=45, cdc_data=cdc_data)
neoscore_result

"""
OUTPUT
{'Turner Syndrome': {'Flag': False, 'Score': 0},
 'Prader-Willi Syndrome': {'Flag': True, 'Score': 15.0},
 'Microcephaly': {'Flag': False, 'Score': 0},
 'Macrocephaly': {'Flag': True, 'Score': 3.5748792270531418}}
"""

# Conducted Five Experiments and Determined Final NeoScore 
example_cases = [
    {'age_months': 6, 'length_cm': 60, 'weight_kg': 7, 'sex': 'Female', 'head_circumference_cm': 40},
    {'age_months': 18, 'length_cm': 75, 'weight_kg': 11, 'sex': 'Male', 'head_circumference_cm': 48},
    {'age_months': 10, 'length_cm': 68, 'weight_kg': 9, 'sex': 'Female', 'head_circumference_cm': 44},
    {'age_months': 14, 'length_cm': 72, 'weight_kg': 12, 'sex': 'Male', 'head_circumference_cm': 47},
    {'age_months': 3, 'length_cm': 55, 'weight_kg': 5, 'sex': 'Female', 'head_circumference_cm': 37}
]

# Function to calculate the final NeoScore as an average of the flagged syndromes' scores
def final_neoscore(neoscore_results):
    scores = [value['Score'] for value in neoscore_results.values() if value['Flag']]
    return sum(scores) / len(scores) if scores else 0

# Conducting the experiment with the example cases
experiment_results = []
for case in example_cases:
    neoscore_results = calculate_neoscore(case['age_months'], case['length_cm'], case['weight_kg'], 
                                          case['sex'], case['head_circumference_cm'], cdc_data)
    final_score = final_neoscore(neoscore_results)
    experiment_results.append({'Case': case, 'Results': neoscore_results, 'Final NeoScore': final_score})

experiment_results

"""
OUTPUT 
[{'Case': {'age_months': 6,
   'length_cm': 60,
   'weight_kg': 7,
   'sex': 'Female',
   'head_circumference_cm': 40},
  'Results': {'Turner Syndrome': {'Flag': False, 'Score': 0},
   'Prader-Willi Syndrome': {'Flag': True, 'Score': 25.403726708074537},
   'Microcephaly': {'Flag': False, 'Score': 0},
   'Macrocephaly': {'Flag': True, 'Score': 5.760869565217384}},
  'Final NeoScore': 15.58229813664596},
 {'Case': {'age_months': 18,
   'length_cm': 75,
   'weight_kg': 11,
   'sex': 'Male',
   'head_circumference_cm': 48},
  'Results': {'Turner Syndrome': {'Flag': True, 'Score': 4.906284454244772},
   'Prader-Willi Syndrome': {'Flag': False, 'Score': 0},
   'Microcephaly': {'Flag': False, 'Score': 0},
   'Macrocephaly': {'Flag': False, 'Score': 0}},
  'Final NeoScore': 4.906284454244772},
 {'Case': {'age_months': 10,
   'length_cm': 68,
   'weight_kg': 9,
   'sex': 'Female',
   'head_circumference_cm': 44},
  'Results': {'Turner Syndrome': {'Flag': False, 'Score': 0},
   'Prader-Willi Syndrome': {'Flag': True, 'Score': 20.33816425120774},
   'Microcephaly': {'Flag': False, 'Score': 0},
   'Macrocephaly': {'Flag': True, 'Score': 7.213438735177859}},
  'Final NeoScore': 13.7758014931928},
 {'Case': {'age_months': 14,
   'length_cm': 72,
   'weight_kg': 12,
   'sex': 'Male',
   'head_circumference_cm': 47},
  'Results': {'Turner Syndrome': {'Flag': False, 'Score': 0},
   'Prader-Willi Syndrome': {'Flag': True, 'Score': 20.833333333333336},
   'Microcephaly': {'Flag': False, 'Score': 0},
   'Macrocephaly': {'Flag': True, 'Score': 4.347826086956517}},
  'Final NeoScore': 12.590579710144926},
 {'Case': {'age_months': 3,
   'length_cm': 55,
   'weight_kg': 5,
   'sex': 'Female',
   'head_circumference_cm': 37},
  'Results': {'Turner Syndrome': {'Flag': False, 'Score': 0},
   'Prader-Willi Syndrome': {'Flag': True, 'Score': 24.78260869565218},
   'Microcephaly': {'Flag': False, 'Score': 0},
   'Macrocephaly': {'Flag': True, 'Score': 4.4653349001175044}},
  'Final NeoScore': 14.623971797884842}]
  """

# Generate HeatMap 

import seaborn as sns

# Creating the Heatmap with the updated data

plt.figure(figsize=(8, 10))
sns.heatmap(adjusted_heatmap_data, annot=True, cmap='coolwarm')
plt.title('Heatmap of NeoScores', fontweight='bold', fontsize=14)
plt.xlabel('Syndromes', fontweight='bold', fontsize=12)
plt.ylabel('Babies', fontweight='bold', fontsize=12)
plt.text(x=adjusted_heatmap_data.shape[1] + 0.5, y=adjusted_heatmap_data.shape[0]/2, s='NeoScore', 
         verticalalignment='center', rotation=270, fontsize=12, fontweight='bold')
plt.xticks(fontsize=10, fontweight='bold')
plt.yticks(fontsize=10, fontweight='bold')
plt.tight_layout()
plt.show()


# Generate Stacked Bar Chart '

import matplotlib.pyplot as plt
import pandas as pd

# Assuming 'adjusted_heatmap_data' is the DataFrame with the updated scores
# Reproducing the Stacked Bar Chart with the updated data

plt.figure(figsize=(8, 10))
adjusted_heatmap_data.plot(kind='bar', stacked=True, colormap='viridis')
plt.title('Stacked Bar Chart of NeoScores', fontweight='bold', fontsize=14)
plt.xlabel('Babies', fontweight='bold', fontsize=12)
plt.ylabel('NeoScore', fontweight='bold', fontsize=12)
plt.xticks(fontsize=10, fontweight='bold', rotation=0)
plt.yticks(fontsize=10)
plt.legend(title='Syndromes', fontsize=10, title_fontsize='13', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()


