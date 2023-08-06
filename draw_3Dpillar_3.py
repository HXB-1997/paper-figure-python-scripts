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
#Ped
# dz = [0.232, 0,    0.314, 0.232,         #,'mAP50-95','recall','mAP50','precision'
#       0.210, 0.209,0.308,0.210,
#       0.297, 0.267,0.317,0.297,
#       0.348, 0.317,0.354,0.348]#高度
#cyclist
dz = [0.211, 0,    0.305, 0,         #,'mAP50-95','recall','mAP50','precision'
      0.213, 0.229,0.303,0.391,
      0.257, 0.281,0.327,0.398,
      0.351, 0.359,0.379,0.461]#高度

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