
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_json(r"C:\Users\TEMP\Pictures\ait582-proj-data.json")

###
df


# In[2]:


A = df['DESCRIPTION'].str.split(";|,", n = 3, expand = True)
A


# In[3]:


####
A.columns = ['LAST_NAME', 'FIRST_NAME', 'AGE']
A


# In[5]:



#####
B = A['FIRST_NAME'].str.split(".", n = 3, expand = True)
B


# In[6]:


B.columns = ['TITLE','F_NAME','NONE']
B



# In[7]:


####
Beta = pd.concat([A, B], axis=1)
Beta


# In[8]:


####
AIT = Beta.drop(['F_NAME','NONE'],axis=1)
AIT


# In[9]:


###
AIT['TITLE'] = AIT['TITLE'].str.strip()
AIT['TITLE']


# In[10]:


###
AIT['TITLE'].value_counts()




# In[11]:


####
#Rat['D'].value_counts()

AIT['GENDER'] = AIT['TITLE'].replace({'Mr':'Male','Miss':'Female','Mrs':'Female','Master':'Male','Dr':'Male','Rev':'Male','Col':'Male','Major':'Male','Mlle':'Female','Jonkheer':'Male','Ms':'Female','Capt':'Female','Don':'Male','Mme':'Female','Sir':'Male','Lady':'Female','the Countess':'Female'})
AIT['GENDER']


# In[12]:



###
AIT


# In[13]:


######
Dataset = pd.concat([df, AIT], axis=1)
Dataset


####
#Dataset.head()


# In[15]:


###
Data_modified = Dataset.drop(Dataset.index[0])

###
Data_modified


# In[16]:


####
import numpy as np
Data_modified['AGE'].replace('', np.nan, inplace=True)
Data_modified['AGE']



# In[17]:


Data_modified.to_csv("AIT582_DATA_NOTCLEANED.csv")


# In[19]:


import numpy as np
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# In[21]:


###GENDER VS SUCCESS ##
sns.countplot(x = 'GENDER', hue = 'SUCCESS', data = Data_modified, palette = 'magma')
plt.title('GENDER vs SUCCESS')
plt.show()


# In[23]:


###SEATCLASS vs SUCCESS##
sns.countplot(x = 'SEATCLASS', hue = 'SUCCESS', data = Data_modified, palette = 'magma')
plt.title('SEATCLASS vs SUCCESS')
plt.show()


# In[25]:


###test success##
sns.countplot(x = 'GUESTS', hue = 'SUCCESS', data = Data_modified, palette = 'magma')
plt.title('GUESTS vs SUCCESS')
plt.show()


# In[41]:


###test success##
plt.figure(figsize=(100,30))
sns.countplot(x = 'FARE', hue = 'SUCCESS', data = Data_modified, palette = 'magma', linewidth = 15)
plt.title('FARE vs SUCCESS')
plt.show()

