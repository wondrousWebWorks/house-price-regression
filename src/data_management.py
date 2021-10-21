import numpy as np
import pandas as pd
import streamlit as st
import joblib

@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_house_price_data():
    df = pd.read_csv("inputs/datasets/raw/train.csv")
    return df


def load_pkl_file(file_path):
    return joblib.load(filename=file_path)