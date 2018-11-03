
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import os


# In[2]:


ID_RT = input("Ingrese RT a Consultar: ")
ID_RT = int(ID_RT)


# In[3]:


mainpath = "C:/Users/mromo/Desktop/Rappi/Datasets/"
cuentas= "Cuentas Bancarias.csv"
bancario = os.path.join(mainpath,cuentas)
Semanas = {}


# In[4]:


for x in 26 and range(28,35):
    pagos = "S" + str(x) + "/" + "Pagos Vigentes.xlsx"
    pagable = os.path.join(mainpath,pagos)
    if x < 27:
        pagina = "Resumen s" + str(x)
    else:
        pagina = "semana" + str(x)
    Semanas[x] = pd.read_excel(pagable, pagina, header = 2)


# In[5]:


RT_Info = pd.DataFrame(columns = Semanas[30].columns)


# In[6]:


RT_Info


# In[7]:


for x in Semanas:
    Semanas[x].rename(columns ={'id':'ID'})
    RT_Info = RT_Info.append(Semanas[x].loc[Semanas[x]['id'] == ID_RT], sort=False)
    print(x)


# In[8]:


Semanas[34].columns


# In[9]:


RT_Info


# In[10]:


RT_Detail = RT_Info.loc[:,'id':'Descto Equipo efectivo']


# In[11]:


RT_Detail.dropna(how="all")


# In[12]:


RT_Detail= RT_Detail.drop(list(RT_Detail)[2:12],axis=1)
RT_Detail


# In[13]:


RT_Summary = pd.DataFrame(columns = RT_Detail.columns)
RT_Summary


# In[14]:


RT_Summary = RT_Detail.groupby('id').sum()


# In[15]:


RT_Summary = RT_Summary.drop(list(RT_Summary)[0:18] , axis =1)
RT_Summary

