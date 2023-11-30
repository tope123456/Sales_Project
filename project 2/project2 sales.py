#importing python libraries 
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 
import numpy as np 
from scipy.stats import t
from scipy.stats import norm 

#importing the data into python 
sales_data= pd.read_csv("C:\\Users\\TEMITOPE\\Desktop\\project\\Sample - Superstore.csv", encoding='latin1')

#checking for duplicates 
sales_data.isna().any()

#coverting the date columns to proper date 
sales_data['Order Date'] = pd.to_datetime(sales_data['Order Date'])
def get_season(month):
    if month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    elif month in [9, 10, 11]:
        return 'Autumn'
    else:
        return 'Winter'
def get_Quater(month):
    if month in [1, 2, 3]:
        return 'Q1'
    elif month in [4, 5, 6]:
        return 'Q2'
    elif month in [7, 8, 9]:
        return 'Q3'
    elif month in [10, 11, 12]:
        return 'Q4'
    else:
        return 'Winter'
sales_data['Quater'] = sales_data['Order Date'].dt.month.apply(get_Quater)

sales_data['Season'] = sales_data['Order Date'].dt.month.apply(get_season)


sales_data['Order Date'] = sales_data['Order Date'].dt.strftime('%Y-%m-%d')

sales_data['Ship Date'] = pd.to_datetime(sales_data['Ship Date'])

sales_data['Ship Date'] = sales_data['Ship Date'].dt.strftime('%Y-%m-%d')


#Data Visualization: sales made by each state 
sales_data1=sales_data.groupby("State")["Sales"].sum().reset_index()
sales_data1=sales_data1.sort_values(by='Sales', ascending=False)
sns.set_style('whitegrid',rc={"axes.xmargin": 0.8})  # Optional: Set a style for the plot
plt.figure(figsize=(8, 6))
ay=sns.barplot(x='State', y='Sales', data= sales_data1, palette='viridis')
plt.xlabel('State')
plt.ylabel('Sales')
plt.title('Sales Made by Each States')
ay.set_xticklabels(sales_data1['State'], fontsize=6)  # Adjust fontsize as needed
ay.tick_params(axis='x', which='both', pad=10)

# profit by each state 
plt.xticks(rotation=90) 
sales_data2=sales_data.groupby("State")["Profit"].sum().reset_index()
sales_data2=sales_data2.sort_values(by='Profit', ascending=False)
sns.set_style('whitegrid',rc={"axes.ymargin": 0.8})  # Optional: Set a style for the plot
plt.figure(figsize=(8, 6))
ax=sns.barplot(x='Profit', y='State', data= sales_data2, palette='viridis')
plt.xlabel('Profit')
plt.ylabel('Sales')
plt.title('Profit Made by Each States')
plt.yticks(rotation=0) 
ax.set_yticklabels(sales_data2['State'], fontsize=6)  # Adjust fontsize as needed
ax.tick_params(axis='y', which='both', pad=10)


#profit by each quater 
sales_data3=sales_data.groupby("Quater")["Profit"].sum().reset_index()
sns.set_style('whitegrid')  # Optional: Set a style for the plot
plt.figure(figsize=(8, 6))
sns.barplot(x='Quater', y='Profit', data= sales_data3, palette='viridis')
plt.xlabel('Quaters')
plt.ylabel('Profit')
plt.title('Profit Made in Each Quater')
plt.yticks(rotation=0) 


warnings.simplefilter(action='ignore', category=FutureWarning)

#hypothesis testing using ANOVA 
alpha = 0.05
import pingouin 
anova_result=pingouin.anova(data = sales_data, dv="Sales",between="Category")
print(anova_result)