import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page_summary import page_summary_body
from app_pages.page_customer_study import page_customer_study_body
from app_pages.page_project_hypothesis import page_project_hypothesis_body
from app_pages.page_predict_sale_price import page_predict_sale_price_body
from app_pages.page_custom_prediction import page_custom_prediction

# Create an instance of the app 
app = MultiPage(app_name="HousePricePrediction")

# Add your app pages here using .add_page()
app.add_page("Quick Project Summary", page_summary_body)
app.add_page("Customer Study", page_customer_study_body)
app.add_page("Project Hypothesis", page_project_hypothesis_body)
app.add_page("Predict Property Sale Price", page_predict_sale_price_body)
app.add_page("Custom Feature Sale Price Prediction", page_custom_prediction)

# Run the  app
app.run()
