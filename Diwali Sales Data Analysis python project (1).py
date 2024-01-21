#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[5]:


df=pd.read_csv(r"C:\Users\Pallavi\Downloads\Diwali Sales Data.csv")


# In[6]:


print(df)


# In[8]:


df.head(10)


# In[7]:


df.tail(10)


# In[9]:


df.shape


# In[10]:


df.info()


# In[11]:


#to delete unwanted/blank column use drop
df.drop(['Status','unnamed1'],axis=1,inplace=True)


# In[12]:


df.info()


# In[13]:


#check for null values
pd.isna(df)


# In[14]:


#drop the null values
df.dropna(inplace=True)


# In[22]:


df.isna().sum()


# In[15]:


#change the datatype
df.info()


# In[16]:


df['Amount']=df['Amount'].astype(int)


# In[17]:


df['Amount'].dtype


# In[18]:


#rename the column name
df.columns


# In[19]:


df.rename(columns={'Marital_Status':'shaadi'},inplace=True)


# In[20]:


df.columns


# In[21]:


df.describe()


# In[22]:


df[['Age','Orders']].describe()


# # EXPLORATORY DATA ANALYSIS

# In[23]:


# plotting a bar chart for Gender and it's count
df.info()


# In[28]:


ax= sns.countplot(x='Gender',data=df)
for bars in ax.containers:
    ax.bar_label(bars)


# In[34]:


# plotting a bar chart for gender vs total amount
gen_amount= df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.barplot(x='Gender',y='Amount',data=gen_amount)
for bars in ax.containers:
    ax.bar_label(bars)


# In[46]:


# Age-group
ax=sns.countplot(x='Age Group',data=df,hue='Gender')
for bars in ax.containers:
    ax.bar_label(bars)


# In[55]:


#Statet
#plotting the barplot for orders vs top 10 states
sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Orders')


# In[57]:


## shaadi
ax = sns.countplot(data = df, x = 'shaadi')
sns.set(rc={'figure.figsize':(7,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[59]:


sales_state = df.groupby(['shaadi', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data = sales_state, x = 'shaadi',y= 'Amount', hue='Gender')


# In[60]:


#ocupation
sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Occupation')

for bars in ax.containers:
    ax.bar_label(bars)


# In[61]:


sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Occupation',y= 'Amount')


# In[62]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)


# In[63]:


sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_Category',y= 'Amount')


# In[64]:


sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_ID',y= 'Orders')


# In[66]:


# top 10 most sold products (same thing as above)

fig1, ax1 = plt.subplots(figsize=(12,7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')


# In[ ]:


#Conclusion:
#+Married women age group 26-35 yrs from UP, Maharastra and Karnataka working in IT, Healthcare and Aviation are more likely to buy products from Food, Clothing and Electronics category

