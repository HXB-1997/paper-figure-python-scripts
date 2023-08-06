import matplotlib.pyplot as plt
import numpy as np

species = ("F-PP with Gauss", "F-PP with Instance", "Ours with Gauss", "Ours with Instance")

#CAR
# penguin_means = {
#     'Easy': (88.90, 90.17, 88.96, 91.34),
#     'Moderate': (79.28, 82.49, 78.65, 83.58),
#     'Hard': (78.07, 78.55, 80.32, 81.47),
# }
#Pedestrian
# penguin_means = {
#     'Easy': (66.11,67.27,68.34,70.30),
#     'Moderate': (61.89,64.21,63.45,66.62),
#     'Hard': (56.91,57.71,55.39,58.00),
# }
#cyclist
penguin_means = {
    'Easy': (87.54,89.34,90.51,91.12),
    'Moderate': (72.78,75.26,75.89,76.61),
    'Hard': (66.07,66.15,69.70,71.25),
}


x = np.arange(len(species))  # the label locations
width = 0.25  # the width of the bars
multiplier = 0

fig, ax = plt.subplots()

for attribute, measurement in penguin_means.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    ax.bar_label(rects, padding=3)
    
    # Plot lines connecting the top points of the bars with the same color
    color = rects[0].get_facecolor()
    ax.plot(x + offset , measurement, linestyle='--', marker='o', color=color)
    
    multiplier += 1

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Average Precision', fontsize=14)
# ax.set_title('Penguin attributes by species')
ax.set_xticks(x + width, species)
ax.legend(loc='upper left', ncols=3, fontsize=12)
ax.set_ylim(60, 100)
ax.tick_params(axis='both', which='major', labelsize=12)
plt.show()
