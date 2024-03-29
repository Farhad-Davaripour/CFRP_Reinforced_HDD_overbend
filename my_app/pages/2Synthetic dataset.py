import streamlit as st
import streamlit_authenticator as stauth
import pandas as pd
from pathlib import Path
st.subheader('Synthetic dataset')
st.markdown("""The synthetic dataset is generated from multiple finite element analyses. Please contact 
Farhad Davaripour on his [Linked-in profile]("https://www.linkedin.com/in/farhad-davaripour/") for more info about the dataset.""")
# data acquisition
st.write("""The following table lists the analyses conducted using the validated FE model. Note that the fibre orientation of
0, 1, and 2 corresponds to the circumferential direction, longitudinal direction, and the combination of the two cases 
before (multi-direction).""")
##
df = pd.read_excel("data/data.xlsx")
features_list = ['t_steel', 'D/t', 'L_CFRP', 't_CFRP', 'fibre_orient', 'pressure']
target_variable = ['No_CFRP_vm','peak_vm', 'peak_vm_CFRP', 'vm_reduction_perc']
df = df.dropna()
st.table(df[features_list + target_variable].reset_index(drop=True))
