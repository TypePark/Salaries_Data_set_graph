import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#DS = pd.read_csv("Salary2024.csv")

#print(DS.head())
#print(DS.shape)
#print(DS.dtypes)
#print(DS.describe())
#print(DS.isnull().sum())

#plt.figure(figsize=(10, 6))
#DS.boxplot(column=["salary"])
#plt.title("salaries")
#plt.show()

#print(DS["salary"].value_counts())

DS = pd.read_csv("Salary2024.csv")#.head(50)

DS_mean = DS.groupby('experience_level')["salary_in_usd"].mean().astype(int)

DS_mean_format = DS_mean.sort_values()
Salary = DS_mean_format.values
Experience = DS_mean_format.index
print(DS_mean_format)


max_salary_mean = (Salary.max())
#print(max_salary)
digit_max = len(str(max_salary_mean))
#print(digit_max , "digit")
tick_num = 10 ** (digit_max - 2) if digit_max > 1 else 1
#print(tick_num , "tick ")

ceiling_num = math.ceil(max_salary_mean / 10000) * 10000
#print(ceiling_num)


colors= ['#ff9999','#66b3ff','#99ff99','#ffcc99']
plt.figure(figsize=(8,6))

plt.bar(Experience, Salary, color=colors[:len(Salary)])
plt.title("Experience level to Salary")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.ylim(0, ceiling_num + 10000)
plt.yticks(range(0, ceiling_num + 1, tick_num))

#print(plt.ylim())
#print(plt.yticks())

for i in range(len(Salary)) :
    plt.text(i, Salary[i], DS_mean_format.iloc[i], ha="center")

plt.show()