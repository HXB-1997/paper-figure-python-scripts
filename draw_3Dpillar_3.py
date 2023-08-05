import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)


fig = plt.figure()
ax = fig.add_subplot(projection='3d')
x, y = np.random.rand(2, 100) * 4
print("x= ",x)
hist, xedges, yedges = np.histogram2d(x, y, bins=4, range=[[0, 4], [0, 4]])

# Construct arrays for the anchor positions of the 16 bars.
xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25, indexing="ij")
xpos = xpos.ravel()
ypos = ypos.ravel()
zpos = 0

# Construct arrays with the dimensions for the 16 bars.
dx = dy = 0.5 * np.ones_like(zpos)
dz = [0.347,0,0.391, 0,         #,'mAP50-95','recall','mAP50','precision'
      0.202,0.433,0.446,0.513,
      0.320,0.449,0.473,0.563,
      0.361,0.491,0.534,0.631]#高度


colors = ['r', 'g', 'b', 'y',
          'r', 'g', 'b', 'y',
          'r', 'g', 'b', 'y',
          'r', 'g', 'b', 'y']

ax.bar3d(xpos, ypos, zpos, dx, dy, dz, zsort='average', color=colors)

# 设置x轴和y轴的刻度标签
labels_x = ['Group 1', 'Group 2', 'Group 3', 'Group 4']
labels_y = ['Data 1', 'Data 2', 'Data 3', 'Data 4']
ax.set_xticks(xpos + dx / 2)  # 设置x轴刻度位置为柱子的中心
ax.set_yticks(ypos + dy)  # 设置y轴刻度位置为柱子的中心
ax.set_xticklabels(['-','-','-','MASK-RCN','-','-','-','YOLOV5','-','-','-','YOLOV8','-','-','-','OURS'])  # 设置x轴刻度标签为自定义标签
ax.set_yticklabels(['-','-','-','-','-','-','-','-','-','-','-','-','mAP50-95','recall','mAP50','precision'])  # 设置y轴刻度标签为自定义标签

plt.show()