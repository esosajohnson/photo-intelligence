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
        
def show_ISO_distribution(metadata):
    if metadata is not None and 'ISO' in metadata.columns:
        st.write("### ISO Distribution")
        iso_counts = metadata['ISO'].value_counts().sort_index()
        st.bar_chart(iso_counts)
    else:
        st.warning("ISO data not available for distribution chart.")
        
def show_focal_length_distribution(metadata):
    if metadata is not None and 'FocalLength' in metadata.columns:
        st.write("### Focal Length Distribution")
        focal_length_counts = metadata['FocalLength'].value_counts().sort_index()
        st.bar_chart(focal_length_counts)
    else:
        st.warning("Focal Length data not available for distribution chart.")

def show_flash_usage(metadata):
    if metadata is not None and 'Flash' in metadata.columns:
        st.write("### Flash Usage Distribution")
        flash_counts = metadata['Flash'].value_counts()
        st.bar_chart(flash_counts)
    else:
        st.warning("Flash data not available for distribution chart.")

st.title("Metadata Dashboard")

metadata = load_metadata("metadata.csv")

display_metadata(metadata)
show_ISO_distribution(metadata)
show_focal_length_distribution(metadata)
show_flash_usage(metadata)