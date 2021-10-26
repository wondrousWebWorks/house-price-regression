import streamlit as st


def page_project_hypothesis_body():

    st.write("### Hypothesis and Validation")

    st.success(
        f"* I suspected that not all 80 feature variables affect house "
        f"prices equally: Correct\n"
        f"\nThe correlation study at Customer Study supports the hypothesis "
        f"and suggests that only 10 features show strong correlation with "
        f"property prices. A strong correlation would be a value of greater "
        f"than 0.5\n"
    )
