import streamlit as st
import pickle
import numpy as np
st.image("https://github.com/Farhad-Davaripour/CFRP_Reinforced_HDD_overbend/blob/main/NClogo.png?raw=true",width=150)
st.subheader("An Application of Machine Learning to Predict the Peak Equivalent Stress Imposed on a CFRP Wrapped HDD Overbend")
st.write("by [Farhad Davaripour](https://www.linkedin.com/in/farhad-davaripour/)")
st.markdown("""This study employs machine leaning to predict the peak equivalent stress on an Horizontally directional drilling (HDD) overbend reinforced with Carbon-fiber-reinforced polymers 
(CFRP) wrap and subjected to combined loading (internal pressure and thermal expansion). The data used in this study is generated from the parametric study conducted via
 finite element (FE) analyses. The variables investigated in the FE analyses are CFRP thickness, CFRP length, fiber orientation, internal pressure, and pipe wall 
 thickness. """)
# Inpus on the sidebar
st.sidebar.title("Inputs")
diameter_over_thickness = slide_bar = st.sidebar.slider("Pipe's Diameter over wall-thickness", value=40, 
                      min_value=20, max_value=50)
CFRP_thickness = slide_bar = st.sidebar.slider('Thickness of the CFRP wrap (mm)', value=2, 
                      min_value=1, max_value=6)
FO = slide_bar = st.sidebar.radio("Fibre orientation",('Circumferencial', 'Longitudinal', 'Multi-directional'))
if FO=='Circumferencial':
    fibre_orientation=0
elif FO=='Longitudinal':
    fibre_orientation=1
else:
    fibre_orientation=2  
pressure = slide_bar = st.sidebar.slider('Internal pressure (MPa)', value=6, 
                      min_value=2, max_value=7) 
# loading the ML model
local_regression = pickle.load(open('regression.pickle','rb'))
# making the prediction
pred = local_regression.predict(np.array([[diameter_over_thickness,CFRP_thickness,fibre_orientation,pressure]]))
# Output
st.subheader('The predicted equivlent stress imposed on an HDD overbend is equial to: ')
st.subheader(round(pred[0][0],2))
