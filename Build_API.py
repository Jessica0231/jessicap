
# coding: utf-8

# In[13]:


from typing import Optional


# In[14]:


from fastapi import FastAPI


# In[15]:


import pandas as pd
import json
import urllib


# In[16]:


app = FastAPI()


# In[17]:


data = pd.read_csv('Jumlah Siswa di Kabupaten Batang 2018-2019.csv')


# In[18]:


datas = data.drop(columns=['Laki -Laki TK', 'perempuan TK', 'Laki -Laki RA', 'perempuan RA', 'Laki -Laki SD', 'perempuan SD', 'Laki -Laki MI', 'perempuan MI', 'Laki -Laki SMP', 'perempuan SMP', 'Laki -Laki MTS', 'perempuan MTS', 'Laki -Laki SMA', 'perempuan SMA', 'Laki -Laki SMK', 'perempuan SMK', 'Laki -Laki MA', 'perempuan MA'])


# In[19]:


datas.rename(columns = {'Kecamatan                                       ':'Kecamatan', 'jumlah_siswa_per_kecamatan':'Jumlah Siswa'}, inplace = True)


# In[20]:


#5 Kecamatan dengan Jumlah Siswa Terbanyak di Kabupaten Batang Tahun 2018-2019
@app.get("/top5kecamatan")
def read_top5kecamatan():
    display = datas.sort_values(by='Jumlah Siswa')
    displayto = display.head(5)
    return displayto.to_dict(orient='records')


# In[28]:


#Jumlah Siswa di Kabupaten Batang Tahun 2018-2019
@app.get("/jumlahsiswa")
def read_jumlahsiswa():
    total = data['Jumlah Siswa'].sum()
    displayto2 = print('Jumlah siswa di Kabupaten Batang tahun 2018-2019 adalah', total, 'orang')
    return displayto2

