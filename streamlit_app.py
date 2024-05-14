import pandas as pd
import streamlit as st
import requests
from io import StringIO



st.set_page_config(layout="wide")

def load_original_data():
    url = 'https://raw.githubusercontent.com/Harirak/test_streamlit/main/category_eda.csv'
    response = requests.get(url)
    if response.status_code == 200:
        return pd.read_csv(StringIO(response.text))
    else:
        st.error("Failed to load data from Github")

df_opt = load_original_data()
df_opt['NEW SUBCATEGORY-L5 (463)'] = df_opt['NEW SUBCATEGORY-L5 (463)'].str.strip()



############
st.header("Select What is Product")

opt = df_opt.loc[:, 'NEW SUBCATEGORY-L5 (463)'].to_list()  
options_lv2 = st.multiselect("What is Product", opt, [])

st.write("You selected:", options_lv2)

st.divider()
###########
st.header("Search Remark")

st.text_input("Remark: ", key='remark')
st.table(df_opt.loc[df_opt['REMARK'].fillna('').str.contains(st.session_state.remark),['NEW SUBCATEGORY-L4 (88) - Sub Cate','NEW SUBCATEGORY-L5 (463)','REMARK']] if st.session_state.remark else None)

st.divider()
###########
st.header("Check 400 Cat from 88 Cat")
opt_lv1 = df_opt['NEW SUBCATEGORY-L4 (88) - Sub Cate'].unique()
options_lv1 = st.multiselect("What is Category 88", list(opt_lv1))
opt_ = df_opt.loc[df_opt['NEW SUBCATEGORY-L4 (88) - Sub Cate'].isin(options_lv1), ['NEW SUBCATEGORY-L4 (88) - Sub Cate','NEW SUBCATEGORY-L5 (463)','REMARK']]
opt_['REMARK'] = opt_['REMARK'].fillna('')
st.table(opt_)
# options_lv2 = st.multiselect("What is Product", opt_, [])
