import pandas as pd
import streamlit as st
import requests
from io import StringIO
# from sqlalchemy.orm import sessionmaker
# from table_meta import mst_cat, seller_list

st.set_page_config(layout="wide")
# session = sessionmaker(bind=engine)()

def load_original_data():
    url = 'https://raw.githubusercontent.com/Harirak/test_streamlit/main/category_eda.csv?token=GHSAT0AAAAAACSH7IEFBSLIJH5SSIBFIKZ4ZSCXQYQ'
    response = requests.get(url)
    if response.status_code == 200:
        return pd.read_csv(StringIO(response.text))
    else:
        st.error("Failed to load data from Github")

# result = session.query(mst_cat.c.description).filter(mst_cat.c.level==5).all()
# session.close()

# opt = pd.DataFrame(result)
# df_opt = pd.read_excel("category_eda.xlsx")
df_opt = load_original_data()

opt_lv1 = df_opt['NEW SUBCATEGORY-L4 (88) - Sub Cate'].unique()
options_lv1 = st.multiselect("What is Category LV4", list(opt_lv1))



opt = df_opt.loc[:, 'NEW SUBCATEGORY-L5 (463)'].to_list() if (options_lv1==[] or options_lv1==['All']) else df_opt.loc[df_opt['NEW SUBCATEGORY-L4 (88) - Sub Cate'].isin(options_lv1), 'NEW SUBCATEGORY-L5 (463)'].to_list()
options_lv2 = st.multiselect("What is Product", opt, [])

st.write("You selected:", options_lv2)


st.divider()
st.header("Search Remark")

st.text_input("Remark: ", key='remark')
st.table(df_opt.loc[df_opt['REMARK'].fillna('').str.contains(st.session_state.remark),['NEW SUBCATEGORY-L4 (88) - Sub Cate','NEW SUBCATEGORY-L5 (463)','REMARK']] if st.session_state.remark else None)
