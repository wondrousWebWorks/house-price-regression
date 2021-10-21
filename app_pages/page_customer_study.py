import streamlit as st
from src.data_management import load_house_price_data

import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np
import plotly.express as px

features_to_study = ['OverallQual', 'YearBuilt', 'YearRemodAdd', 'TotalBsmtSF',
                    '1stFlrSF', 'GrLivArea', 'FullBath', 'TotRmsAbvGrd',
                    'GarageCars', 'GarageArea', 'SalePrice']

selected_feature_dict = {
    'OverallQual': 'Overall Quality',
    'YearBuilt': 'Year Built',
    'YearRemodAdd': 'Remodel Date',
    'TotalBsmtSF': 'Total Basement Square Footage',
    '1stFlrSF': 'Total First Floor Square Footage',
    'GrLivArea': 'Above Grade (Ground) Living Area Square Footage',
    'FullBath': 'Number of Full Bathrooms',
    'TotRmsAbvGrd': 'Number of Rooms above Grade',
    'GarageCars': 'Garage (Number of Cars)',
    'GarageArea': 'Garage Area Square Footage',
    'SalePrice': 'Sale Price'
}

# load data
df_full = load_house_price_data()

def page_customer_study_body():
    # hard copied from ExploratoryDataAnalysis notebook
    st.write("### House Price Prediction Customer Study")
    st.info(
        f"The client is interested in understanding the patterns from the customer base, "
        f"so that the client can learn the most relevant variables correlated "
        f"to a churned customer.")

    # inspect collected data
    if st.checkbox("Inspect House Sales Data"):
        inspect_data(df_full)
    st.write("---")

    # Correlation Study Summary
    st.write(
        f"A correlation study was conducted in the notebook to better understand how "
        f"the feature variables are correlated to Sale Price. \n"
        f"\n**The most correlated variable are:** "
    )

    for feature in features_to_study:
        st.write(
            f"**{feature}:** {selected_feature_dict[feature]}"
        )

    st.info(
        f"The correlation plot below shows 37 (out of 79) features "
        f"which show significant enough correlation with Sale Price "
        f"to be reported. \n"
        f"\n "
        f"We are interesting in features which show a correlation of "
        f"greater than 0.5, which are features exceeding the red "
        f"line in the plot in the Feature Correlation section below."
    )

    df_eda = df_full.filter(features_to_study)

    # Individual plots per variable
    if st.checkbox("Feature Correlation"):
        plot_correlation_table()

        st.info(
            f"Following are each of the highest correlating "
            f"feature variables plotted against Sale Price.\n"
        )



        for feature in features_to_study:
            if feature == 'SalePrice':
                continue
            else:
                correlation_scatter_plot(feature)

    st.write("---")
        
    # Parallel plot
    if st.checkbox("Parallel Plot"):
        st.write(
            f"* Information in yellow indicates the profile from a churned customer")
        pass

def inspect_data(df):
    st.write(
        f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns, find below the first 10 "
        f"rows and a quick inspection of each variable content.")
    st.write(df.head(10))
    
    for col in df.columns: st.write(f"* **{col}**:\n{df[col].unique()}\n")

def plot_correlation_table():
    corr = df_full.corr()[['SalePrice']].abs()
    fig, ax = plt.subplots(figsize=(12, 5))
    sns.lineplot(data=corr)
    plt.xticks(rotation=70)
    plt.title(f"Correlation of Features with Sale Price", fontsize=20,y=1.05)
    plt.legend("Correlation")
    plt.axhline(y=0.5, color='r', linestyle='--')
    st.pyplot(fig)

def correlation_scatter_plot(feature):
    fig, ax = plt.subplots()
    ax.scatter(df_full[feature], df_full['SalePrice'])
    title = f"Distribution of {selected_feature_dict[feature]}"
    plt.title(title)
    plt.ylabel("Sale Price")
    plt.xlabel(selected_feature_dict[feature])
    st.pyplot(fig)
