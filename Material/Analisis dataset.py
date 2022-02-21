#!/usr/bin/env python
# coding: utf-8

# ### Importar librerias

# In[2]:


import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
font = {'size': 12}
plt.rc('font', **font)


# ### Leer, analizar y corregir datos NaN en el dataset 

# In[3]:


os.chdir("F:\----- PRACTICAS\Python\Data Science\CSVs")
datos=pd.read_csv("titanic.csv", delimiter=',')
datos.head()


# In[4]:


datos.dtypes


# In[5]:


datos.describe()


# In[6]:


datos.isna().sum()


# In[7]:


mediaEdades=round(datos['Age'].mean())
datos['Age']=datos['Age'].fillna(mediaEdades)
datos.isna().sum()


# In[8]:


datos['Cabin']=datos['Cabin'].fillna("NE")
datos.isna().sum()


# In[14]:


datos['Cabin'].value_counts()


# In[15]:


datos['Embarked']=datos['Embarked'].fillna("NE")
datos.isna().sum()


# In[16]:


datos['Embarked'].value_counts()


# In[17]:


datos.head()


# ### Para una mejor lectura cambiemos algunos datos

# In[18]:


datos['Survived']=datos['Survived'].map({
        0: 'No',
        1: 'Yes'
    })
datos.head()


# In[19]:


datos['Embarked']=datos['Embarked'].map({
        'S': 'Southampton',
        'C': 'Cherbourg',
        'Q': 'Queenstown'
    })
datos.head()


# ### Ya preparado el dataset, veamos que informacion valiosa podemos obtener del mismo

# In[20]:


datos.groupby(['Pclass', 'Survived'])['Survived'].count()
ax=sns.countplot(x='Pclass', hue='Survived', palette='Set1', data=datos)
ax.set(title='Estado del pasajero (murio/sobrevivio) dado a la clase a la que pertenecia', 
       xlabel='Clase del pasajero', ylabel='Total')
plt.show()


# In[21]:


datos.groupby(['Sex', 'Survived'])['Survived'].count()


# In[40]:


ax=sns.countplot(x='Sex', hue='Survived', palette='Set1', data=datos)
ax.set(title='Total de pasajeros con respecto al sexo', 
       xlabel='Sexo', ylabel='Total')
plt.show()


# In[41]:


ax=sns.catplot(x='Pclass', hue='Sex', col='Survived', palette='Set1', 
               data=datos, kind="count")
plt.show()


# <i style='color: red'>Funcion para colocar etiquetas a las graficas de barras</i>

# In[20]:


def autolabel(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate('{}'.format(height),
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  
                    textcoords="offset points",
                    ha='center', va='bottom')


# In[22]:


aux=datos.pivot_table(values='Age', index='Cabin', aggfunc='mean')
aux


# In[23]:


datos.groupby('Cabin').filter(lambda x: (x['Cabin'] == "F4").any())
datos.groupby('Cabin').filter(lambda x: (x['Cabin'] == "F4").any())['Age']


# In[24]:


aux.index[:5].to_list()


# In[25]:


aux[:5]['Age'].to_list()


# In[42]:


fig, ax=plt.subplots()
ax.set_ylabel('Edad')
ax.set_title('Edades promedio en las diferentes cabinas')
bar1=ax.bar(aux.index[:5].to_list(), aux[:5]['Age'].to_list())
        
autolabel(bar1)
plt.show()


# In[27]:


pd.crosstab(datos['Embarked'], datos['Survived'])


# In[43]:


ax=sns.countplot(x='Embarked', hue='Survived', data=datos)
ax.set(title='Distribucion de supervivencia segun lugar de embarque', 
       xlabel='Lugar', ylabel='Total')
plt.show()


# In[29]:


datos['Cabin'].groupby(datos['Cabin']).count()


# In[31]:


datos[datos['Age']<18]['Age'].count()


# In[32]:


intervaloEdad1=datos[datos['Age']<18].pivot_table(values='Age', index='Pclass', aggfunc='count')
intervaloEdad1


# In[33]:


intervaloEdad2=datos[(datos['Age']>=18) & (datos['Age']<=50)].pivot_table(values='Age', index='Pclass', aggfunc='count')
intervaloEdad2


# In[34]:


intervaloEdad3=datos[datos['Age']>50].pivot_table(values='Age', index='Pclass', aggfunc='count')
intervaloEdad3


# <i style='color: red'>Funcion para colocar etiquetas a las graficas de pastel</i>

# In[37]:


def funcPie(values):
    val = iter(values)
    return lambda pct: f"{pct:.1f}% ({next(val)})"


# In[49]:


fig, ax=plt.subplots(1, 3, figsize = (16, 7))
ax[0].pie(intervaloEdad1['Age'].to_list(), labels=intervaloEdad1.index.to_list(), 
        autopct=funcPie(intervaloEdad1['Age'].to_list()), shadow=True, startangle=90)
ax[0].axis('equal')
ax[0].set_title('Edades menores a 18')  
ax[1].pie(intervaloEdad2['Age'].to_list(), labels=intervaloEdad2.index.to_list(),
        autopct=funcPie(intervaloEdad2['Age'].to_list()), shadow=True, startangle=90)
ax[1].axis('equal') 
ax[1].set_title('Edades mayores o iguales a 18 y menores o iguales a 50')  
ax[2].pie(intervaloEdad3['Age'].to_list(), labels=intervaloEdad3.index.to_list(),
        autopct=funcPie(intervaloEdad3['Age'].to_list()), shadow=True, startangle=90)
ax[2].axis('equal')  
ax[2].set_title('Edades mayores a 50') 
plt.legend()
plt.show()


# In[50]:


datos[datos['Name'].str.match("Carter"+ r'\b', case=False)]['Name']


# In[53]:


familias=[]
for i in datos['Name']:
    apellido=str(i).split(',')[0]
    f=datos[datos['Name'].str.match(apellido+ r'\b', case=False)]['Name'].to_list()
    if(familias.count(f)==0):
        familias.append(f)
familias[:5]


# In[54]:


len(familias)


# In[55]:


for i in range(0, len(familias)-1):
    for j in range(i+1, len(familias)):
        if len(familias[j])>len(familias[i]):
            aux=familias[i]
            familias[i]=familias[j]
            familias[j]=aux
familias[:5]


# In[71]:


cont=[]
nombreFamilias=[]
for i in familias[:3]:
    aux=""
    cont.append(len(i))
    for j in i:
        aux+=j+'\n'
    nombreFamilias.append(aux)

fig, ax=plt.subplots(figsize = (18, 7))
ax.set_ylabel('Total')
ax.set_title('Familias mas numerosas')
bar1=ax.bar(nombreFamilias, cont)
autolabel(bar1)
plt.show()


# In[73]:


aux=datos[['Age', 'Sex', 'Pclass', 'Survived']].groupby('Age').filter(lambda x: (x['Age']==50).any())
aux


# In[74]:


aux.pivot_table(index='Sex', columns=['Survived', 'Pclass'], aggfunc='count').fillna(0)


# In[75]:


aux=datos.groupby(['Pclass', 'Sex'])['Pclass'].count()
aux


# In[76]:


aux.index


# In[77]:


aux[1]


# In[79]:


fig, ax=plt.subplots(1, 3, figsize = (16, 7))
ax[0].pie(aux[1].to_list(), labels=aux[1].index.to_list(), 
              autopct=funcPie(aux[1].to_list()), shadow=True, startangle=90)
ax[0].axis('equal')
ax[0].set_title('Total hombres y mujeres clase 1')
ax[1].pie(aux[2].to_list(), labels=aux[2].index.to_list(), 
              autopct=funcPie(aux[2].to_list()), shadow=True, startangle=90)
ax[1].axis('equal')
ax[1].set_title('Total hombres y mujeres clase 2')
ax[2].pie(aux[3].to_list(), labels=aux[3].index.to_list(), 
              autopct=funcPie(aux[3].to_list()), shadow=True, startangle=90)
ax[2].axis('equal')
ax[2].set_title('Total hombres y mujeres clase 3')
plt.legend()
plt.show()


# In[94]:


fig, ax=plt.subplots(figsize = (20, 5))
ax.scatter(datos['Age'], datos['Fare'])
ax.set_xlabel('Edad')
ax.set_ylabel('Tarifa')
ax.set_title('Relacion entre edad y la tarifa')
plt.show()


# In[98]:


clase1=datos[['Age', 'Fare', 'Pclass']].groupby('Pclass').filter(lambda x: (x['Pclass']==1).any())
clase2=datos[['Age', 'Fare', 'Pclass']].groupby('Pclass').filter(lambda x: (x['Pclass']==2).any())
clase3=datos[['Age', 'Fare', 'Pclass']].groupby('Pclass').filter(lambda x: (x['Pclass']==3).any())
fig, ax=plt.*(3, 1, figsize = (15, 15), constrained_layout=True)
ax[0].scatter(clase1['Age'], clase1['Fare'])
ax[0].set_xlabel('Edad')
ax[0].set_ylabel('Tarifa')
ax[0].set_title('Relacion entre edad y la tarifa clase 1')
ax[0].grid(True)
ax[1].scatter(clase2['Age'], clase2['Fare'])
ax[1].set_xlabel('Edad')
ax[1].set_ylabel('Tarifa')
ax[1].set_title('Relacion entre edad y la tarifa clase 2')
ax[1].grid(True)
ax[2].scatter(clase3['Age'], clase3['Fare'])
ax[2].set_xlabel('Edad')
ax[2].set_ylabel('Tarifa')
ax[2].set_title('Relacion entre edad y la tarifa clase 3')
ax[2].grid(True)
plt.show()


# In[81]:


datos.head()


# In[82]:


datos.drop(['Name','Ticket','PassengerId','Cabin'], 1, inplace=True)
datos.head()


# In[84]:


datos['Survived'].replace(('No', 'Yes'), (0, 1), inplace=True)
datos['Sex'].replace(('male', 'female'), (0, 1), inplace=True)
datos['Embarked'].replace(('Cherbourg','Queenstown','Southampton'), (0, 1, 2), inplace=True)
datos.head()


# In[85]:


plt.figure(figsize=(14,12))
sns.heatmap(datos.corr(), linewidths=0.1, square=True,  cmap='Blues', annot=True)
plt.show()

