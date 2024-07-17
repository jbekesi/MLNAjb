import streamlit as st
import pandas as pd



APP_TITLE = 'MLNA'
APP_SUB_TITLE = 'The MultiLingual Network Analysis package'


st.markdown(
    """
    Hello world! I am here.
    """
)


# def main():

#     st.set_page_config(APP_TITLE)
#     st.markdown(f"##### {APP_SUB_TITLE}")

#     # Prompt the user to upload a file
#     uploaded_file = st.file_uploader("Choose a pickle file", type="pickle")
#     if uploaded_file is not None:
#         # Read the file into a DataFrame
#         text_df = pd.read_pickle(uploaded_file)

#         # Display the DataFrame
#         st.write("Uploaded data frame:")
#         st.dataframe(text_df)  # Use st.dataframe() for a more interactive display

# if __name__ == "__main__":
#     main()
