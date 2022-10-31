"""
Created on Mon Oct 31 14:54:43 2022
@author: 1013327
"""

import streamlit as st

def intro():
    import streamlit as st
    st.write("# Welcome to Streamlit! 👋")
    st.sidebar.success("Select a demo above.")
    st.markdown("""Resume Creator""")

def mapping_demo():
    import streamlit as st
    st.write("# Welcome to Streamlit! 👋")
    st.sidebar.success("Select a demo above.")
    
def plotting_demo():
    import streamlit as st
    st.write("# Welcome to Streamlit! 👋")
    st.sidebar.success("Select a demo above.")

def data_frame_demo():
    import streamlit as st
    st.write("# Welcome to Streamlit! 👋")
    st.sidebar.success("Select a demo above.")

page_names_to_funcs = {
    "—": intro,
    "Plotting Demo": plotting_demo,
    "Mapping Demo": mapping_demo,
    "DataFrame Demo": data_frame_demo
}

demo_name = st.sidebar.selectbox("Choose a demo", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()
