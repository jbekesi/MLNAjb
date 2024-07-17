import streamlit as st
import pandas as pd
from mlna import user_input, network



APP_TITLE = 'MLNA'
APP_SUB_TITLE = 'The MultiLingual Network Analysis package'

def main():

    st.set_page_config(APP_TITLE)
    st.markdown(f"##### {APP_SUB_TITLE}")

    # Prompt the user to upload a file
    uploaded_file = st.file_uploader("Upload a pickled data frame containing your texts:", type="pickle")
    if uploaded_file is not None:
        # Read the file into a DataFrame
        text_df = pd.read_pickle(uploaded_file)

        # Display the DataFrame
        st.write("Uploaded data frame:")
        st.dataframe(text_df)  # Use st.dataframe() for a more interactive display

        html_content = network.visualize_network (text_df, ['PERSON'], user_ents=None, user_dict=None, core=False, select_nodes=None, sources=None,\
        title='network_visualization', figsize=(1000, 700), bgcolor='black', font_color='white')

        st.components.v1.html(html_content, height=600, width=800)

if __name__ == "__main__":
    main()
