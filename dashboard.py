import streamlit as st
import pandas as pd

def load_metadata(file_path):
    try:
        metadata = pd.read_csv(file_path)
        return metadata
    except Exception as e:
        st.error(f"Error loading metadata: {e}")
        return None
    
def display_metadata(metadata):
    if metadata is not None:
        st.write("### Extracted Metadata")
        st.dataframe(metadata)
    else:
        st.warning("No metadata to display.")
        
st.title("Metadata Dashboard")

metadata = load_metadata("metadata.csv")

display_metadata(metadata)