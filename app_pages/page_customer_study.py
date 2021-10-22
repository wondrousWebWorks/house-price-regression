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
df_full = load_house_price_data("train", "raw")

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

    # Customer Study Insights
    if st.checkbox("Customer Study Insights"):
        st.write(
            f"- **Overall Quality:**  The higher the Overall Quality, the "
            f"higher the Sale Price.\n"
            f"- **Year Built:** The more recent the construction date, "
            f"the higher the Sale Price. The increase is more noticeable "
            f"for properties constructed later than 1960.\n"
            f"- **Remodel Date:** The more recent the remodelling date, "
            f"the higher the Sale Price. The majority of out outliers with "
            f"higher Sale Prices tend to manifest for properties remodelled "
            f"after the nineteen-nineties.\n"
            f"- **Basement Square Footage:** There seems to be a strong "
            f"correlation with bigger basement sizes commanding higher prices. "
            f"The highest prices seem to come from properties with basement "
            f"areas between 1000 and just over 3000 square feet.\n"
            f"- **First Floor Square Footage:** There seems to be a "
            f"strong correlation with bigger first floor sizes commanding "
            f"higher prices. The highest prices seem to come from properties "
            f"with first floor areas between about 1000 and just over 2500 "
            f"square feet.\n"
            f"- **Ground Floor Square Footage:** There seems to be a "
            f"strong correlation with bigger ground floor sizes commanding "
            f"higher prices. The highest prices seem to come from properties "
            f"with first floor areas between about 2000 and just over 4000 "
            f"square feet.\n"
            f"- **Full Bathrooms:** Properties with two or three bathrooms "
            f"command higher prices. What is surprising here is that a "
            f"property without any bathrooms sold for nearly $400,000.\n"
            f"- **Rooms Above Grade:** Properties with five to nine rooms "
            f"above Grade do not show great variance in Sale Price. The "
            f"highest Sale Prices are for properties with 10 to 12 rooms.\n"
            f"- **Garage (Number of Cars):** Properties with room for "
            f"two or three cars sold for higher Sale Prices.\n"
            f"- **Garage Square Footage:** There seems to be a "
            f"correlation with Sale Price where bigger garage areas "
            f"sold for higher prices. What is interesting is that the "
            f"correlation holds true up to about 1200 square feet. "
            f"Properties with larger garage square footage did not sell "
            f"for the highest prices.\n"
        )

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
