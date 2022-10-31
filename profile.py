import streamlit as st

def intro():
    import streamlit as st
    st.write("# Welcome to Streamlit! 👋")
    st.sidebar.success("Select a demo above.")
    st.markdown("""Resume Creator""")

def sales_force_analytics():
    import streamlit as st
    st.write("# Sales Force Analytics")
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
    "Introduction": intro,
    "Sales Force Analytics": sales_force_analytics,
    "Mapping Demo": mapping_demo,
    "DataFrame Demo": data_frame_demo
}

demo_name = st.sidebar.selectbox("Choose a demo", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()
