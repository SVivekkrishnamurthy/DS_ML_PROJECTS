import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
from colorama import Fore
import math
import warnings
warnings.filterwarnings('ignore') 

st.set_page_config(page_title="!!!!Weather Analysis!!!!", page_icon=":bar_chart:", layout="wide")

st.title(":bar_chart: Weather Time Series Analysis")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

f1 = st.file_uploader(":file_folder: Upload a file", type=(["csv","txt","xlsx","xls"]))

if f1 is not None:
    filename = f1.name
    st.write(filename)
    df = pd.read_csv(filename, encoding='ISO-8859-1')
else:
    os.chdir(r"D:\DS_ML\DS_ML_PROJECTS\Weather_Project\Input")
    df = pd.read_csv("weather.csv", encoding='ISO-8859-1')

col1, col2 = st.columns((2))
df['ISO_TIME'] = pd.to_datetime(df["ISO_TIME"], errors='coerce')

startDate = pd.to_datetime(df["ISO_TIME"]).min()
endDate = pd.to_datetime(df["ISO_TIME"]).max()

with col1:
    date1 = pd.to_datetime(st.date_input("Start Date", startDate))

with col2:
    date2 = pd.to_datetime(st.date_input("Start Date", endDate))

df = df[(df["ISO_TIME"] >= date1) & (df["ISO_TIME"] <= date2)].copy()

st.sidebar.header("Choose filter")
basin = st.sidebar.multiselect("BASIN",df['BASIN'].unique())

if not basin:
    df2 = df.copy()
else:
    df2 = df[df["BASIN"].isin(basin)]

subbasin = st.sidebar.multiselect("SUBBASIN",df2["SUBBASIN"].unique())

if not basin:
    df3 = df2.copy()
else:
    df3 = df2[df2["SUBBASIN"].isin(subbasin)]

names = st.sidebar.multiselect("NAME",df3["NAME"].unique())


if not basin and not subbasin and not names:
    filtered_df =df
elif not subbasin and not names:
    filtered_df = df[df["BASIN"].isin(basin)]
elif not basin and not names:
    filtered_df = df[df["SUBBASIN"].isin(subbasin)]
elif subbasin and names:
    filtered_df = df3[df["SUBBASIN"].isin(subbasin) & df3["NAME"].isin(names)]
elif basin and names:
    filtered_df = df3[df["SUBBASIN"].isin(basin) & df3["NAME"].isin(names)]
elif basin and subbasin:
    filtered_df = df3[df["SUBBASIN"].isin(basin) & df3["NAME"].isin(subbasin)]
elif names:
    filtered_df = df3[df3["NAME"].isin(names)]
else:
    filtered_df = df3[df3["BASIN"].isin(basin) & df3["SUBBASIN"].isin(subbasin) & df3["NAME"].isin(names)]


category_df = filtered_df.groupby()