import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("Health.csv")
df[['Systolic', 'Diastolic']] = df['BloodPressure'].str.split('/', expand=True).astype(int)
df.drop('BloodPressure', axis=1, inplace=True)

print(df.head())
print(df.info())
print(df.describe())

df.isnull().sum()
df.duplicated().sum

df['Gender'].value_counts()
df['Gender'].value_counts().plot(kind="bar")
plt.show()


df['Diabetic'].value_counts().plot(kind='pie',autopct='%1.1f%%')
plt.title("Diabetic proportion")
plt.show()

df['City'].value_counts().plot(kind="bar")
plt.title("City distribution")
plt.show()

df['HeartRate'].hist()
plt.title("Heart rate distribution")
plt.show()

sns.boxplot(df['Cholesterol'])
plt.title("Cholesterol levels")
plt.show()

#Bivariate analysis


sns.scatterplot(data=df,x='Age',y='HeartRate')
plt.show()

sns.boxplot(data=df,x='Diabetic',y='Cholesterol')
plt.show()

sns.barplot(data=df,x='City',y='Temperature')
plt.xticks(rotation=45)
plt.show()


numeric_df = df.select_dtypes(include=[int, float])
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Analysis")
plt.show()
