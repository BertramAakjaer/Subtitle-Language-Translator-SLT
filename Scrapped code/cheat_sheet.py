import streamlit as st
import pandas as pd
import numpy as np
import time

st.title("My App's UI Cheat Sheet")  # Main title for the cheat sheet

# Your UI elements and code go here
st.write("This is plain text.")
st.markdown("You can use **Markdown** for formatting!")
st.header("This is a header")
st.subheader("Subheader")
st.caption("This is a smaller caption")

data = {"Name": ["Alice", "Bob"], "Age": [25, 30]}
st.table(data)
st.json(data)

name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=0)
color = st.color_picker("Choose a color:")
selection = st.selectbox("Pick an option:", ["A", "B", "C"])
uploaded_file = st.file_uploader("Choose a file")

if st.button("Click me!"):
    st.write("You clicked the button!")

col1, col2 = st.columns(2)  # Two columns
with col1:
    st.write("Content in the first column")
with col2:
    st.write("Content in the second column")

with st.expander("Click to expand"):
    st.write("Hidden content")

tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])
with tab1:
    name2 = st.text_input("Enter your name:22")
with tab2:
    name3 = st.text_input("Enter your name:323")


with st.spinner("Loading..."):
    # Simulate some processing
    time.sleep(2)

st.success("Operation completed!")
st.warning("This is a warning message.")
st.error("An error occurred.")


# 1. Data Display and Interaction
with st.expander("Data Display"):
    st.subheader("Tables and Charts")
    df = pd.DataFrame(np.random.randn(10, 3), columns=["A", "B", "C"])
    st.write(df)

    st.subheader("Interactive Charts")
    chart_type = st.selectbox("Choose chart type:", ["line", "bar", "area"])
    if chart_type == "line":
        st.line_chart(df)
    elif chart_type == "bar":
        st.bar_chart(df)
    else:
        st.area_chart(df)

# 2. Input Widgets and State
with st.expander("Inputs & State"):
    st.subheader("Input Widgets")
    name = st.text_input("Your Name")
    number = st.number_input("Choose a Number", min_value=0, max_value=100)

    st.subheader("Session State")
    if "counter" not in st.session_state:
        st.session_state.counter = 0
    if st.button("Increment"):
        st.session_state.counter += 1
    st.write("Counter:", st.session_state.counter)

# 3. Layout Customization
with st.expander("Layout & Theming"):
    st.subheader("Columns")
    col1, col2 = st.columns(2)
    with col1:
        st.write("Column 1 Content")
    with col2:
        st.write("Column 2 Content")

    st.subheader("Sidebar")
    with st.sidebar:
        st.write("Sidebar Content")

# 4. Caching (for efficiency)
@st.cache_data(ttl=600)  # Cache for 10 minutes
def get_data():
    # Simulate fetching data (replace with your actual data source)
    return pd.DataFrame({"X": range(10), "Y": np.random.randn(10)})

with st.expander("Caching"):
    st.subheader("Cached Data Example")
    data = get_data()
    st.write(data)

# 5. Progress & Status
with st.expander("Status Messages"):
    st.subheader("Status Updates")
    st.success("Success Message")
    st.warning("Warning Message")
    st.error("Error Message")

    st.subheader("Progress")
    with st.spinner("Working..."):
        # Simulate some processing time
        import time
        time.sleep(2)