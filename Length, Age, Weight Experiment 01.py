# Conducting the experiments 
# For a given input, Age of a baby in months is 1, the length is 24", Male baby, Weight is 11.7lb. 

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Given input for the baby
age_months = 1  # in months
length_inches = 24  # baby's length in inches
weight_pounds = 11.7  # baby's weight in pounds

# Convert length to cm and weight to kg for the plot (1 inch = 2.54 cm, 1 pound = 0.453592 kg)
length_cm = length_inches * 2.54
weight_kg = weight_pounds * 0.453592

# Load the CDC benchmark image
benchmark_image_path = '/mnt/data/image.png'
benchmark_image = mpimg.imread(benchmark_image_path)

# Create a plot
fig, ax1 = plt.subplots(figsize=(15, 20))

# Display the CDC benchmark image
ax1.imshow(benchmark_image, aspect='auto', extent=[0, 36, 0, 105])

# Overlay the baby's data
# Add a red dot for baby's length at the corresponding age
ax1.plot(age_months, length_cm, 'ro', markersize=10, label=f'Baby\'s Length: {length_cm} cm')
# Add a blue dot for baby's weight at the corresponding age
ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
ax2.plot(age_months, weight_kg, 'bo', markersize=10, label=f'Baby\'s Weight: {weight_kg} kg')

# Since the weight scale is on the right side of the chart, we set the limits according to the image scale
ax2.set_ylim(0, 16)

# Labels & Title
ax1.set_xlabel('Age (Months)')
ax1.set_ylabel('Length (cm)')
ax2.set_ylabel('Weight (kg)', color='b')
plt.title('CDC Growth Chart with Baby\'s Length and Weight Overlay')

# Legend
handles1, labels1 = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
plt.legend(handles1 + handles2, labels1 + labels2, loc='upper left')

# Show the plot
plt.show()

# Save the overlay plot to a file
overlay_image_path = '/mnt/data/growth_chart_overlay.png'
plt.savefig(overlay_image_path)

overlay_image_path

# OUTPUT: growth_chart_emphasized_overlay.png 

# Results 
# For the 1-month-old male baby with a length of 24 inches (60.96 cm) and a weight of 11.7 pounds (5.30703 kg), I've created a plot that overlays this baby's length and weight on the benchmark growth chart provided by the CDC.
# Based on the benchmark chart, the baby's length at 60.96 cm would be well above the 95th percentile for length, 
# indicating that the baby is much taller than average for his age. His weight at 5.31 kg also appears to be above the 95th percentile, 
# indicating a higher weight compared to average peers. This can be considered healthy.

# ------
# Adjust the horizontal lines to span across the entire width of the plot for better readability.

# Re-creating the plot with full-width horizontal lines
fig, ax1 = plt.subplots(figsize=(15, 20))

# Display the CDC benchmark image again
ax1.imshow(benchmark_image, aspect='auto', extent=[0, 36, 0, 105])

# Overlay the baby's data with full-width horizontal lines for length and weight
# Add a red horizontal line across the plot for baby's length
ax1.hlines(y=length_cm, xmin=0, xmax=36, colors='r', linestyles='dashed', lw=2, label=f'Baby\'s Length: {length_cm} cm')
# Add a blue horizontal line across the plot for baby's weight
ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
ax2.hlines(y=weight_kg, xmin=0, xmax=36, colors='b', linestyles='dashed', lw=2, label=f'Baby\'s Weight: {weight_kg} kg')

# Add red and blue stars to denote the exact position for the baby's length and weight
ax1.plot(age_months, length_cm, 'r*', markersize=20)
ax2.plot(age_months, weight_kg, 'b*', markersize=20)

# Adjust the secondary y-axis (weight) scale according to the image
ax2.set_ylim(0, 16)

# Enhance labels & title for better visibility
ax1.set_xlabel('Age (Months)', fontsize=14, weight='bold')
ax1.set_ylabel('Length (cm)', fontsize=14, weight='bold')
ax2.set_ylabel('Weight (kg)', fontsize=14, weight='bold', color='b')
plt.title('CDC Growth Chart with Full-Width Highlighted Baby\'s Length and Weight', fontsize=16, weight='bold')

# Emphasize the legend with a larger font
handles1, labels1 = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
plt.legend(handles1 + handles2, labels1 + labels2, loc='upper left', fontsize=12)

# Show the plot with full-width horizontal lines
plt.show()

# Save the plot with full-width horizontal lines to a file
full_width_highlighted_overlay_image_path = '/mnt/data/growth_chart_full_width_highlighted_overlay.png'
plt.savefig(full_width_highlighted_overlay_image_path)

full_width_highlighted_overlay_image_path

# OUTPUT: growth_chart_full_width_highlighted_overlay.png

