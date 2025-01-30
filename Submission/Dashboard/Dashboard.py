# -*- coding: utf-8 -*-
"""Dashboard.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1A3q7_0M5btZqcbc_vsqomurVRH-rFuRN

# Proyek Analisis Data: Persewaan Sepeda
- **Nama:** Anindita Gayatri
- **Email:** agayatri123@yahoo.co.id
- **ID Dicoding:** anindita_gayatri_ukA6
"""

import datetime
import streamlit as st

st.title("dashboard")

st.subheader('Interactive Streamlit')
 
date = st.date_input(label='Tanggal Sewa Sepeda', min_value=datetime.date(1900, 1, 1))
st.write('Tanggal Sewa:', date)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

# load the dataset
df_all_data= pd.read_csv('all_data.csv')
df_all_data.head()

st.title("dashboard")

st.subheader('Jumlah Pemakai Sewa Sepeda')

col1, col2 = st.columns(2)

with col1:
    total_pemakai_monthly = df_all_data['registered'].sum()
    st.metric("Pemakai Registered", value=total_pemakai_monthly)

with col2:
    total_pemakai_casual = df_all_data['casual'].sum()
    st.metric("Pemakai Casual", value=total_pemakai_casual)

fig, ax = plt.subplots(figsize=(16, 8))
colors = ["#7CFC00"]

sns.barplot(
    x="mnth",
    y="registered",
    data=df_all_data.sort_values(by="mnth", ascending=False),
    palette=colors,
    ax=ax
    )
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)

st.pyplot(fig)

x = np.random.normal(15, 5, 250)

fig, ax = plt.subplots(figsize=(16, 8))
colors = ["#90CAF9"]

sns.barplot(
    x="mnth",
    y="casual",
    data=df_all_data.sort_values(by="mnth", ascending=False),
    palette=colors,
    ax=ax
    )
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)

st.pyplot(fig)


