import numpy as np
import pandas as pd
import streamlit as st
import joblib

@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_house_price_data(target, type):
    if target == "train" and type =="raw":
        df = pd.read_csv("inputs/datasets/raw/train.csv")
    elif target == "test" and type == "raw":
        df = pd.read_csv("inputs/datasets/raw/test.csv")
    elif target == "train" and type == "cleaned":
        df = pd.read_csv("outputs/datasets/cleaned/TrainSetCleaned.csv")
    elif target == "test" and type == "cleaned":
        df = pd.read_csv("outputs/datasets/cleaned/TestSetCleaned.csv")
    return df


def load_pkl_file(file_path):
    return joblib.load(filename=file_path)