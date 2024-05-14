import pandas as pd
import streamlit as st
# from sqlalchemy.orm import sessionmaker
# from table_meta import mst_cat, seller_list

st.set_page_config(layout="wide")
# session = sessionmaker(bind=engine)()


# result = session.query(mst_cat.c.description).filter(mst_cat.c.level==5).all()
# session.close()

# opt = pd.DataFrame(result)
df_opt = pd.read_excel("D:\\Users\\harirak.i\\OneDrive - ASSET WORLD CORP PUBLIC CO.,LTD\\EDA\\005. CWS\\002. AFP Seller list\\012. Cat 460\\category_eda.xlsx")


opt_lv1 = df_opt['NEW SUBCATEGORY-L4 (88) - Sub Cate'].unique()
options_lv1 = st.multiselect("What is Category LV4", list(opt_lv1))



opt = df_opt.loc[:, 'NEW SUBCATEGORY-L5 (463)'].to_list() if (options_lv1==[] or options_lv1==['All']) else df_opt.loc[df_opt['NEW SUBCATEGORY-L4 (88) - Sub Cate'].isin(options_lv1), 'NEW SUBCATEGORY-L5 (463)'].to_list()
options_lv2 = st.multiselect("What is Product", opt, [])

st.write("You selected:", options_lv2)


st.divider()
st.header("Search Remark")

st.text_input("Remark: ", key='remark')
st.table(df_opt.loc[df_opt['REMARK'].fillna('').str.contains(st.session_state.remark),['NEW SUBCATEGORY-L4 (88) - Sub Cate','NEW SUBCATEGORY-L5 (463)','REMARK']] if st.session_state.remark else None)
