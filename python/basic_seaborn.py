# Seaborn

import matplotlib.pyplot as plt
import seaborn as sns

# 기본 데이터셋
# print(sns.get_dataset_names())

tips = sns.load_dataset('tips')
print(tips.info())

# 산점도
sns.scatterplot(x="total_bill", y="tip", data=tips, hue = "size", palette="deep",style="time",size="size")

plt.show()

# stripplot
sns.stripplot(x='day', y='total_bill', data=tips, jitter = True, hue = "size", dodge = True)

plt.show()

# warmplot
sns.swarmplot(x='day', y='total_bill', data=tips, hue = "size", dodge = True)

plt.show()

# relplot 관계형 plot
sns.relplot(x='day', y='total_bill', data=tips, hue = "size", style="time")

plt.show()

# catplot
sns.catplot(x="day", y="time", kind = "strip", hue = "size")

plt.show()

# displot
sns.displot(tips["total_bill"], bins = 30)

plt.show()

# pairplot

sns.pairplot(data=tips, hue = "time")

plt.show()

# regplot
sns.regplot(data=tips, x= "total_bill", y="tip")

plt.show()

# heatmap
sns.heatmap(tips.corr(), annot = True, linewidths = 2, cmap = "magma")

plt.show()