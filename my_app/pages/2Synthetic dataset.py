import streamlit as st
import streamlit_authenticator as stauth
import pandas as pd
from pathlib import Path
st.markdown("""The synthetic dataset is generated from multiple finite element analyses. Please contact 
Farhad Davaripour on his [Linked-in profile]("https://www.linkedin.com/in/farhad-davaripour/") for more infor about the dataset.""")
# data acquisition
st.write('The following table lists the analyses conducted using the validated FE model:')
##
path = list(Path.cwd().iterdir())[8]/"data.xlsx"
df = pd.read_excel(path)
features_list = ['t_steel', 'D/t', 'L_CFRP', 't_CFRP', 'fibre_orient', 'pressure']
target_variable = ['No_CFRP_vm','peak_vm', 'peak_vm_CFRP', 'vm_reduction_perc']
df = df.dropna()
st.table(df[features_list + target_variable].reset_index())