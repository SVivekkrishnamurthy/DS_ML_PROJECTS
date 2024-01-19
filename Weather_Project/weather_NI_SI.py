import pandas as pd
import numpy as np 
import streamlit as st
import matplotlib as plt 

NI_DF = pd.read_csv('input/NI_list_v04r00.csv')

st.write(NI_DF)