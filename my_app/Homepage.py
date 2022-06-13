import streamlit as st
import pickle
import numpy as np
# st.image("https://github.com/Farhad-Davaripour/streamlit-example/blob/master/NClogo.png?raw=true",width=150)
st.subheader("An Application of Machine Learning to Predict the Peak Equivalent Stress Imposed on a CFRP Wrapped HDD Overbend")
st.write("by [Farhad Davaripour](https://www.linkedin.com/in/farhad-davaripour/)")
st.markdown("""This study employs machine leaning to predict the peak equivalent stress on an Horizontally directional drilling (HDD) overbend reinforced with Carbon-fiber-reinforced polymers 
(CFRP) wrap and subjected to combined loading (internal pressure and thermal expansion). The data used in this study is generated from the parametric study conducted via
 finite element (FE) analyses. The variables investigated in the FE analyses are CFRP thickness, CFRP length, fiber orientation, internal pressure, and pipe wall 
 thickness. """)
# Schamtic view of the HDD overbend
url = "https://github.com/Farhad-Davaripour/CFRP_Reinforced_HDD_overbend/blob/main/HDD-Schematic.png?raw=true"
st.markdown("""Below figure demonstrates a schematic view of a pipeline partly constructed using HDD method. 
The HDD overbend is highlighted in the figure.""")
st.image(url,width=750)
# Inpus on the sidebar
st.sidebar.title("Overview")
#
with st.sidebar.expander("Pipeline inputs"):
    diameter_over_thickness = slide_bar = st.slider("Pipe's Diameter over wall-thickness", value=40, 
                        min_value=20, max_value=50)
    pressure = slide_bar = st.slider('Internal pressure (MPa)', value=6, 
                      min_value=2, max_value=7) 
with st.sidebar.expander("CFRP inputs"):
    CFRP_thickness = slide_bar = st.slider('Thickness of the CFRP wrap (mm)', value=2, 
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
pred = local_regression.predict(np.array([[diameter_over_thickness,CFRP_thickness,fibre_orientation,pressure]]))
# Output
st.subheader('The predicted equivlent stress imposed on an HDD overbend is equial to: ')
st.subheader(str(round(pred[0][0],2))+" MPa")
