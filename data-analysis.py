#import libaries first
#if not present install using pip
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv("Expanded_data_with_more_features.csv")
print(df.head())
df.describe()
df.info()
df.isnull().sum()
df=df.drop("Unnamed: 0",axis=1)
print(df.head())
df["WklyStudyHours"] = df["WklyStudyHours"].str.replace("05-Odt","5-10")
df.head()
#plt.figure(figsize=(5,5))
#ax=sns.countplot(data= df,x="Gender")
#ax.bar_label(ax.containers[0])
#plt.show()
plt.figure(figsize=(8,8))
#gb=df.groupby("ParentEduc").agg({"MathScore":'mean',"ReadingScore":'mean',"WritingScore":"mean"})
#sns.heatmap(gb, annot=True)
#plt.show()
#gb=df.groupby("ParentMaritalStatus").agg({"MathScore":'mean',"ReadingScore":'mean',"WritingScore":"mean"})
#sns.heatmap(gb, annot=True)
#plt.show()
#sns.boxplot(data=df,x="MathScore")
#plt.show()
print(df["EthnicGroup"].unique())
groupA=df.loc[(df['EthnicGroup']=="group A")].count()
groupB=df.loc[(df['EthnicGroup']=="group B")].count()
groupC=df.loc[(df['EthnicGroup']=="group C")].count()
groupD=df.loc[(df['EthnicGroup']=="group D")].count()
groupE=df.loc[(df['EthnicGroup']=="group E")].count()
l=["group A","group B","group C","group D","group E"]
mlist=[groupA["EthnicGroup"],groupB["EthnicGroup"],groupC["EthnicGroup"],groupD["EthnicGroup"],groupE["EthnicGroup"]]
#plt.pie(mlist,labels=l,autopct="%1.2f%%")
#plt.title("Distribution of Ethnic Groups")
#plt.show()

ax=sns.countplot(data=df,x='EthnicGroup')
ax.bar_label(ax.containers[0])
plt.show()
