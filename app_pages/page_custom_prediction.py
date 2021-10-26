import streamlit as st

import pandas as pd

from src.data_management import (
    load_house_price_data, load_pkl_file
)

# Map column names to a more legible format
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

    # Load train and test data sets
    df_train = load_house_price_data('train', 'raw')
    df_test_cleaned = load_house_price_data('test', 'cleaned')

    # Load trained RandomForest model
    rf_model = load_pkl_file("outputs/models/rf_model.pkl")

    # Get feature names from DataFrame columns
    column_names = df_test_cleaned.columns

    # Will store values from inputs
    custom_values = []

    feature1 = 'OverallQual'
    feature1 = st.selectbox(label=f"{selected_feature_dict[feature1]} (1 to 10)",
                            options=range(1, 11))

    feature2 = 'YearBuilt'
    feature2 = st.number_input(label=f"{selected_feature_dict[feature2]} (1860 to 2010)",
                               min_value=1860,
                               max_value=2010)

    feature3 = 'YearRemodAdd'
    feature3 = st.number_input(label=f"{selected_feature_dict[feature3]} (1950 to 2010)",
                               min_value=1950,
                               max_value=2010)

    feature4 = 'TotalBsmtSF'
    feature4 = st.number_input(label=f"{selected_feature_dict[feature4]} (0 to 6000)",
                               min_value=0,
                               max_value=6000)

    feature5 = '1stFlrSF'
    feature5 = st.number_input(label=f"{selected_feature_dict[feature5]} (0 to 4000)",
                               min_value=0,
                               max_value=4000)

    feature6 = 'GrLivArea'
    feature6 = st.number_input(label=f"{selected_feature_dict[feature6]} (0 to 5000)",
                               min_value=0,
                               max_value=5000)

    feature7 = 'FullBath'
    feature7 = st.selectbox(label=f"{selected_feature_dict[feature7]} (0 to 4)",
                            options=range(4))

    feature8 = 'TotRmsAbvGrd'
    feature8 = st.selectbox(label=f"{selected_feature_dict[feature8]} (1 to 14)",
                            options=range(1, 15))

    feature9 = 'GarageCars'
    feature9 = st.selectbox(label=f"{selected_feature_dict[feature9]} (0 to 4)",
                            options=range(5))

    feature10 = 'GarageArea'
    feature10 = st.number_input(label=f"{selected_feature_dict[feature10]} (0 to 2000)",
                                min_value=0,
                                max_value=2000)

    if st.button("Predict Price"):
        custom_values = [feature1, feature2, feature3,
                         feature4, feature5, feature6,
                         feature7, feature8, feature9,
                         feature10]
        df_custom = pd.DataFrame(custom_values).T
        df_custom.columns = column_names

        # Make prediction on custom data
        custom_prediction = rf_model.predict(df_custom)
        st.info(
            f"#### Predicted Sale Price for Entered Parameters: ${custom_prediction[0]}" # noqa: E501
        )
