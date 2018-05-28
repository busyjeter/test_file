import matplotlib.pyplot as plt 

x_value=list(range(1,1001))
y_value=[x**2 for x in x_value]
plt.scatter(x_value,y_value,c=y_value,cmap=plt.cm.Blues,edgecolor='none',s=10)


# 设置图表标题并给坐标轴加上标签 
plt.title("Square Numbers", fontsize=24) 
plt.xlabel("Value", fontsize=14) 
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小 
plt.tick_params(axis='both', which='major', labelsize=14)

plt.axis([0,1100,0,1100000])

# plt.show()
plt.savefig('squares_plot.png',bbox_inches='tight')
