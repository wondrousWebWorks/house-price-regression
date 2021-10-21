import streamlit as st
import matplotlib.pyplot as plt

def page_summary_body():

    st.write("### Quick Project Overview")

    st.info(
        f"**Project Terms & Jargon**\n"
        f"* A **customer** is a person who consumes your service or product.\n"
        f"* A **prospect** is a potential customer.\n"
        f"* A **feature** is an aspect the property that's provided in the data set.\n"
        f"**Project Dataset**\n"
        f"* The dataset represents **House Price Sales data for Ames, Iowa**. "
        f"It contains data on individual house sales with information on features including"
        f"(but not limited to) the amount of bathrooms, rooms, garage space for cars, "
        f"house condition, square footage or prominent features and many more."
        f"There is a total of 80 features in the data set which can be viewed"
        f"[here](https://github.com/wondrousWebWorks/house-price-regression#2-dataset-content).")

    st.write(
        f"* For additional information, please visit and **view** the "
        f"[README file](https://github.com/wondrousWebWorks/house-price-regression).")
    
    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in understanding which features most "
        f"affect the value of house prices in Ames, Iowa.\n"
        f"* 2 - The client is interested in estimating the value of four "
        f"properties they inherited from their grandfather."
        )
