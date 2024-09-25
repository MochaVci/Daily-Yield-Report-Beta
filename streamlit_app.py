import streamlit as st
import pandas as pd
import math
from pathlib import Path
from streamlit_extras.app_logo import add_logo
from st_aggrid import AgGrid

# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='PE Daily Yield Report Beta',
    layout="wide",
    initial_sidebar_state="collapsed",
    page_icon='/workspaces/Daily-Yield-Report-Beta/data/image/schedule.png', # This is an emoji shortcode. Could be a URL too.
)

#st.sidebar.image("/workspaces/Daily-Yield-Report/data/image/Western_Digital_logo.svg.png")
st.logo("/workspaces/Daily-Yield-Report-Beta/data/image/Western_Digital_logo.svg.png")
st.sidebar.success("select a page above.")
#st.sidebar.title("Daily Yield Report")
#rad = st.sidebar.radio("Navigation",["Home","About"])
#st.session_state.sidebar_state = "collapsed"

# -----------------------------------------------------------------------------
# Draw the actual page

# Set the title that appears at the top of the page.
'''
# 📆 Daily Yield Report Beta

Welcome to Yield Daily Report Beta! We're testing a new platform to help you track and analyze daily yield data. Explore our features and provide feedback to help us improve!
'''

# Add some spacing
''
''

import pandas as pd

# ข้อมูลสำหรับแต่ละผลิตภัณฑ์
data_leo_a = {
    "Product": ["Leo-A"] * 6,
    "Model": ["LHC-SJ-16HD-12TB-PN"] * 6,
    "O/L": ["90.5%"] * 6,
    "Week": ["FW08", "FW09", "FW10", "FW11", "FW12", "FW13"],
    "Yield": ["91.1% (22.2K)", "91.8% (17.8K)", "90.8% (18.7K)", "90.6% (25.8K)", "SRST (7.6K)", "Func (2.6K)"]
}

data_leo_b = {
    "Product": ["Leo-B"] * 6,
    "Model": ["LEE-SJ-16HD-14TB-MO-PN"] * 6,
    "O/L": ["84.5%"] * 6,
    "Week": ["FW08", "FW09", "FW10", "FW11", "FW12", "FW13"],
    "Yield": ["89.9% (20.2K)", "89.0% (3.7K)", "88.2% (4.4K)", "86.9% (4.5K)", "Func (5.3K)", "S5W (7)"]
}

data_paris_d = {
    "Product": ["Paris-D"] * 6,
    "Model": ["PDQJ-SJ-18HD-C20TB-SZ"] * 6,
    "O/L": ["84.0%"] * 6,
    "Week": ["FW08", "FW09", "FW10", "FW11", "FW12", "FW13"],
    "Yield": ["84.5% (90.8K)", "84.7% (126.3K)", "84.5% (134.8K)", "Final 83.8%* (84.3K)", "SRST (50.0K)", "S5W (22)"]
}

data_paris_c = {
    "Product": ["Paris-C"] * 18,
    "Model": [
        "PCM-COM-18HD-C18TB"] * 6 + ["PCM-COM-18HD-C16TB"] * 6 + ["PCM-COM-18HD-C14TB-IN"] * 6,
    "O/L": ["87.0%"] * 12 + ["86.0%"] * 6,
    "Week": [
        "FW08", "FW09", "FW10", "FW11", "FW12", "FW13",
        "FW08", "FW09", "FW10", "FW11", "FW12", "FW13",
        "FW08", "FW09", "FW10", "FW11", "FW12", "FW13"
    ],
    "Yield": [
        "89.4% (35.4K)", "87.2% (34.7K)", "91.3% (22.4K)", "Final 90.4%* (8.2K)", "SRST (3.8K)", "S5W (12)",
        "91.8% (67.7K)", "90.4% (59.1K)", "91.2% (26.5K)", "Final 91.1%* (71.4K)", "SRST (34.9K)", "S5W (19)",
        "", "small production", "88.8% (8.4K)", "small production", "SRST (9.9K)", ""
    ]
}


# สร้าง DataFrame
df_leo_a = pd.DataFrame(data_leo_a)
df_leo_b = pd.DataFrame(data_leo_b)
df_paris_d = pd.DataFrame(data_paris_d)
df_paris_c = pd.DataFrame(data_paris_c)

# รวม DataFrame ทั้งหมด
df = pd.concat([df_leo_a, df_leo_b, df_paris_d, df_paris_c], ignore_index=True)

product = df['Product'].unique()
selected_product = st.multiselect(
    'Specific Product',
    product,
    product)

selected_week = st.multiselect(
    'Specific Week',
    sorted(df['Week'].unique()),
    sorted(df['Week'].unique()))
''
''
# Filter the data
filtered_df = df[(df['Product'].isin(selected_product))&
                 (df['Week'].isin(selected_week))]

# แปลง DataFrame
df_pivot = filtered_df.pivot_table(index=['Product', 'Model', 'O/L'], columns='Week', values='Yield', aggfunc='first').reset_index()
new_order = ["Product","Model","O/L"] + sorted(selected_week)
df_pivot = df_pivot[new_order]
st.dataframe(df_pivot, hide_index = True, use_container_width=True)

''
st.divider()