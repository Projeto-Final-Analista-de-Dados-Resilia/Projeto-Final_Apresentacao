import pandas as pd
import warnings
warnings.simplefilter(action='ignore',category=FutureWarning)
import matplotlib.pyplot as ml
import numpy as np
import seaborn as sns
import re


principal = pd.read_csv('./csv_alterado/dados_combinados.csv')
df = pd.DataFrame(principal)
df['Date'] = pd.to_datetime(df['Date'])

df

dfcor=df.pivot_table(columns='Name',index='Date',values='Close', aggfunc='mean',).reindex(pd.date_range(start='2020-09-01',end='2021-06-30'),method='nearest')
#dfcor
corrprincipal = dfcor.corr(method = 'pearson')

#corrprincipal
ml.figure(figsize=(12,10), dpi = 200)
vmin = 0
vmax = 1
annot = True
cmap = sns.light_palette("#252237", as_cmap=True)

hm = sns.heatmap(data=corrprincipal, vmin=vmin,vmax=vmax,annot=annot, cmap=cmap)
hm.patch.set_facecolor('none')
ml.show()