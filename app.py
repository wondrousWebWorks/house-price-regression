import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page_summary import page_summary_body

# Create an instance of the app 
app = MultiPage(app_name= "HousePricePrediction")

# Add your app pages here using .add_page()
app.add_page("Quick Project Summary", page_summary_body)

# Run the  app
app.run()