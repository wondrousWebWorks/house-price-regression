import streamlit as st

import pandas as pd

from src.data_management import load_house_price_data

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


def page_custom_prediction():
    """Get user input and make Sale Price prediction"""
    st.write("### Make Custom Predictions")

    df_train = load_house_price_data('train', 'raw')
    df_test_cleaned = load_house_price_data('test', 'cleaned')
    column_names = df_test_cleaned.columns
    custom_values = []

    feature1 = 'OverallQual'
    feature1 = st.selectbox(label=selected_feature_dict[feature1],
                            options=df_train[feature1].unique())

    feature2 = 'YearBuilt'
    feature2 = st.number_input(label=selected_feature_dict[feature2],
                               min_value=1860,
                               max_value=2010)

    feature3 = 'YearRemodAdd'
    feature3 = st.number_input(label=selected_feature_dict[feature3],
                               min_value=1950,
                               max_value=2010)

    feature4 = 'TotalBsmtSF'
    feature4 = st.number_input(label=selected_feature_dict[feature4],
                               min_value=0,
                               max_value=6000)

    feature5 = '1stFlrSF'
    feature5 = st.number_input(label=selected_feature_dict[feature5],
                               min_value=0,
                               max_value=4000)

    feature6 = 'GrLivArea'
    feature6 = st.number_input(label=selected_feature_dict[feature6],
                               min_value=0,
                               max_value=5000)

    feature7 = 'FullBath'
    feature7 = st.selectbox(label=selected_feature_dict[feature7],
                            options=range(4))

    feature8 = 'TotRmsAbvGrd'
    feature8 = st.selectbox(label=selected_feature_dict[feature8],
                            options=range(15))

    feature9 = 'GarageCars'
    feature9 = st.selectbox(label=selected_feature_dict[feature9],
                            options=range(5))

    feature10 = 'FullBath'
    feature10 = st.number_input(label=selected_feature_dict[feature10],
                                min_value=0,
                                max_value=1400)

    if st.button("Predict Price"):
        custom_values = [feature1, feature2, feature3,
                         feature4, feature5, feature6,
                         feature7, feature8, feature9,
                         feature10]
        df_custom = pd.DataFrame(custom_values).T
        df_custom.columns = column_names
        st.write(df_custom)
