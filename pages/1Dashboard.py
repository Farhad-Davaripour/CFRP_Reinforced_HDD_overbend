import streamlit as st
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit.components.v1 as components
# st.image("https://github.com/Farhad-Davaripour/streamlit-example/blob/master/NClogo.png?raw=true",width=150)
# st.markdown('__'*34)
st.markdown("""<b><h3 style='text-align:center;'>An Application of Machine Learning to Predict the 
            Peak Equivalent Stress Imposed on a CFRP Wrapped HDD Overbend</h3></b>""", unsafe_allow_html=True)
st.write("by [Farhad Davaripour](https://www.linkedin.com/in/farhad-davaripour/)")
st.markdown("""This study employs machine leaning to predict the peak equivalent stress on an Horizontally directional drilling (HDD) overbend reinforced with Carbon-fiber-reinforced polymers 
(CFRP) wrap and subjected to combined loading (internal pressure and thermal expansion). The data used in this study is generated from the parametric study conducted via
 finite element (FE) analyses. The variables investigated in the FE analyses are CFRP thickness, CFRP length, fiber orientation, internal pressure, and pipe wall 
 thickness. """)
# Schamtic view of the HDD overbend
st.markdown("""Below figure demonstrates a schematic view of a pipeline partly constructed using HDD method. 
The HDD overbend is highlighted in the figure.""")
url = "https://github.com/Farhad-Davaripour/CFRP_Reinforced_HDD_overbend/blob/main/HDD-Schematic.png?raw=true"
col1,mid,col2 = st.columns([0.1,5,1])
with mid:
    st.image(url,width=650,caption='A schematic view of a pipeline partly constructed using HDD method')
with col2:
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.image("https://github.com/Farhad-Davaripour/CFRP_Reinforced_HDD_overbend/blob/main/scroll%20down%20for%20more.png?raw=true",width=120)
# Inpus on the sidebar
st.sidebar.title("Input parameters:")
#
with st.sidebar.expander("Pipeline inputs:"):
    diameter_over_thickness = slide_bar = st.slider("Pipe's Diameter over wall-thickness:", value=40, 
                        min_value=20, max_value=50)
    pressure = slide_bar = st.slider('Internal pressure (MPa):', value=9, 
                      min_value=2, max_value=10) 
with st.sidebar.expander("CFRP inputs:"):
    CFRP_thickness = slide_bar = st.slider('Thickness of the CFRP wrap (mm):', value=5, 
                        min_value=0, max_value=6)
    FO = slide_bar = st.radio("Fibre orientation",('Circumferencial', 'Longitudinal', 'Multi-directional'))
    if FO=='Circumferencial':
        fibre_orientation=0
    elif FO=='Longitudinal':
        fibre_orientation=1
    else:
        fibre_orientation=2  
# Note
st.sidebar.markdown("""Note: The input variables above could be adjusted by the user which will automatically update the 
peak equivalent stress imposed on the HDD overbend (displayed on the main page). According to the results obtained from 
feature engineering, the CFRP length is not incorporated (as a feature variable) in the ML model.""")
# loading the ML model
local_regression = pickle.load(open('regression.pickle','rb'))
# making the prediction
pred_reinforced = local_regression.predict(np.array([[diameter_over_thickness,CFRP_thickness,fibre_orientation,pressure]]))
pred_unreinforced = local_regression.predict(np.array([[diameter_over_thickness,0.0,0,pressure]]))
# Output
st.markdown("""<b><h4 style='text-align:left;'>Output:</h4></b>""", unsafe_allow_html=True)
st.markdown("""The present work employs a data driven approach to predict the peak equivalent stress imposed on the HDD overbend under combined loading.
The data is generated using finite element models and multiple regression models including multi-linear model, second order polynomial model, 
Random forest, and SVM are evaluated to find the model that yields the highest accuracy. The detailed analyses showed that using the second 
order polynomial model leads to the highest accuracy. The model performance is provided in the Model Performance page. Also, The 
predicted peak equivlent stress imposed on an HDD overbend is presented in the following bar chart: 
""")
df = pd.DataFrame({"Unreinforced HDD overbend":round(pred_unreinforced[0][0],2),
                "Reinforced HDD overbend":round(pred_reinforced[0][0],2)},index=['Unreinforced','Rreinforced'])
# plotting the bar chart
col1,mid,col2 = st.columns([1,5,1])
fig, ax = plt.subplots(figsize=(6,4))
with mid:
    plt.ylabel('Peak equivalent stress (MPa)')
    plt.ylim((0,450))
    ax.bar(x=df.index,height=df.values[0],color=['darkBlue','darkgreen'])
    st.pyplot(fig)
    st.markdown("<p style='text-align:center;'>Peak equivalent stress imposed on the HDD overbend</p>", unsafe_allow_html=True)
# adding discussion after the bar chart
unwrapped = round(pred_unreinforced[0][0],2)
wrapped = round(pred_reinforced[0][0],2)
st.write(f"""As presented in the above figure, using CFRP reinforcement, the peak equivalent stress on the HDD overbend decreased by
<b style=color:darkgreen;>{round((unwrapped-wrapped)/unwrapped*100,2)}%</b> from <b style=color:darkgreen;>{unwrapped} MPa</b> to 
            <b style=color:darkgreen;>{wrapped} MPa</b>""" , unsafe_allow_html=True)
