import matplotlib.pyplot as plt
import numpy as np

# 生成示例数据
# x = np.linspace(0, 10, 100)
# y1 = np.sin(x)
# y2 = np.cos(x)
# y3 = np.sin(x) + np.cos(x)

x1 = [0.320, 0.342, 0.35, 0.4777]
y1 = [74.89,75.46,78.66,79.42]
x2 = [0.305,0.324,0.345,0.353]
y2 = [41.9,45.89,48.62,51]
x3 = [0.3,0.311,0.325,0.373]
y3 = [59,62.37,63.58,64.97]
markers = ['o', '^', 's', 'D']  # 不同数据点的标记样式
# 绘制折线图
for i in range(4):
    plt.plot(x1[i], y1[i], color='blue', linewidth=2, marker=markers[i])
for i in range(4):
    plt.plot(x2[i], y2[i], color='blue', linewidth=2, marker=markers[i])
for i in range(4):
    plt.plot(x3[i], y3[i], color='blue', linewidth=2, marker=markers[i])        
plt.plot(x1, y1, color='orange', label='CAR', linewidth=2)
plt.plot(x2, y2, color='green', label='Ped.', linewidth=2)
plt.plot(x3, y3, color='red', label='Cyc.', linewidth=2)
# plt.plot(x4, y4, color='red', label='OURS', linewidth=2)
# plt.plot(color='blue', linewidth=2, marker=markers[1],label='mask-RCNN')
# 添加标题和标签
plt.title('High 2D Accuracy Improves 3D Object Detection', fontsize=16)
plt.xlabel('2D Segment Accuracy', fontsize=12)
plt.ylabel('3D Detection Accuracy', fontsize=12)

# 添加图例
plt.legend()

# 添加标记样式说明
markers = ['o', '^', 's', 'D']
marker_labels = ['Circle', 'Triangle', 'Square', 'Diamond']

plt.plot(0.457,70.5, color='blue', linewidth=2, marker=markers[0])
plt.text(0.46,70,"MASK-RCNN", fontsize=10)
plt.plot(0.457,68.5, color='blue', linewidth=2, marker=markers[1])
plt.text(0.46,68,"YOLOV5", fontsize=10)
plt.plot(0.457,66.5, color='blue', linewidth=2, marker=markers[2])
plt.text(0.46,66,"YOLOV8", fontsize=10)
plt.plot(0.457,64.5, color='blue', linewidth=2, marker=markers[3])
plt.text(0.46,64,"OURS", fontsize=10)
# 将标记样式说明添加到图表旁边
# for i, marker in enumerate(markers):
#     plt.text(4.2, y3[i], marker_labels[i], fontsize=10)


# 调整坐标轴范围
plt.xlim(0.38, 0.5)
plt.ylim(40, 80)
# 设置x轴刻度间隔为0.02
plt.xticks(np.arange(0.28, 0.51, 0.02))
# 添加网格线
plt.grid()

# 显示图形
plt.show()
