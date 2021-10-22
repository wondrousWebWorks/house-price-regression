import streamlit as st
from src.data_management import load_house_price_data
from src.data_management import load_pkl_file

from src.machine_learning.evaluate import evaluate_metrics

import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd

from sklearn.model_selection import train_test_split

def page_predict_sale_price_body():
    pd.set_option('display.float_format',  '{:,.2f}'.format)
    st.write("### Predict Property Sale Price")
    st.info(
        f"According to the project requirements, our client has "
        f"inherited four properties from her grandfather in Ames, Iowa. "
        f"The test data set for this project contains 1459 properties. "
        f"In order to obtain our four hypothetical properties, the "
        f"**last four from the test data set** were sliced out to be the "
        f"focus of our Sale Price predictions."
    )

    rf_model = load_pkl_file(f"outputs/models/rf_model.pkl")
    df_test = load_house_price_data("test", "cleaned")
    df_train = load_house_price_data("train", "cleaned")

    # Create four hypothetical inherited properties from test data set 
    inherited_properties = df_test.iloc[-4:]
    inherited_properties.index = [1, 2, 3, 4]

    st.write(f"#### Inherited Properties")

    st.write(inherited_properties)
    st.write("---")

    sale_price_prediction = rf_model.predict(inherited_properties)

    st.write("#### Predicted House Prices")
    prediction_df = pd.DataFrame(sale_price_prediction, columns=['Sale Price'])
    prediction_df.index = [1, 2, 3, 4]
    st.write(prediction_df)
    st.write("---")

    X = df_train.drop("SalePrice", axis=1)
    y = df_train["SalePrice"]

    X_train, X_val_and_test, y_train, y_val_and_test = train_test_split(
        X, y, test_size=0.3, random_state=42)

    X_val, X_test, y_val, y_test = train_test_split(
        X_val_and_test, y_val_and_test, test_size=0.5, random_state=42)
    
    train_preds = rf_model.predict(X_test)
    evaluation_metrics = evaluate_metrics(y_test, train_preds)

    st.write("#### The following evaluation metrics were obtained for the trained model")

    for key, value in evaluation_metrics.items():
        st.write(f"**{key}:** {value:.2f}")
