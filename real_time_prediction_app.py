import streamlit as st
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit.components.v1 as components
import time
# st.image("https://github.com/Farhad-Davaripour/streamlit-example/blob/master/NClogo.png?raw=true",width=150)
# st.markdown('__'*34)
st.markdown("""<b><h3 style='text-align:center;'>An Application of Machine Learning to Predict the 
            Peak Equivalent Stress Imposed on a CFRP Wrapped HDD Overbend</h3></b>""", unsafe_allow_html=True)
st.write("by [Farhad Davaripour](https://www.linkedin.com/in/farhad-davaripour/)")
st.markdown("""This study employs machine leaning to predict the peak equivalent stress on an Horizontally Directional Drilling (HDD) overbend reinforced with Carbon-fiber-reinforced polymers 
(CFRP) wrap and subjected to combined loading (internal pressure and thermal expansion). The peak equivalent stress on the HDD overbend is predicted using a machine learning model trained based on the dataset synthetically
    generated using validated finite element models. The variables investigated in the FE analyses are CFRP thickness, CFRP length, fiber orientation, internal pressure, and pipe wall 
thickness. The figure on the right demonstrates a schematic view of a pipeline partly constructed using HDD method. 
The HDD overbend is highlighted in the figure. """)
col1,mid,col2 = st.columns([1,5,1])
with mid:
    url = "https://github.com/Farhad-Davaripour/CFRP_Reinforced_HDD_overbend/blob/main/images/HDD-Schematic.png?raw=true"
    st.image(url,width=500,caption='A schematic view of a pipeline partly constructed using HDD method')
with col2:
    st.image("https://github.com/Farhad-Davaripour/CFRP_Reinforced_HDD_overbend/blob/main/images/scroll%20down%20for%20more.png?raw=true",width=120)
## Realtime data
placeholder = st.empty()
for seconds in range(200):
    with placeholder.container():
        diameter_over_thickness = int(np.random.choice(range(20, 50)))
        pressure = np.random.choice(range(2, 10))
        CFRP_thickness = np.random.choice(range(0, 6))
        fibre_orientation = np.random.choice(range(0,3))
        time.sleep(1)
        # loading the ML model
        local_regression = pickle.load(open('regression.pickle','rb'))
        # making the prediction
        pred_reinforced = local_regression.predict(np.array([[diameter_over_thickness,CFRP_thickness,fibre_orientation,pressure]]))
        pred_unreinforced = local_regression.predict(np.array([[diameter_over_thickness,0.0,0,pressure]]))
        # Output
        st.markdown("""<b><h4 style='text-align:left;'>Output:</h4></b>""", unsafe_allow_html=True)
        st.markdown(""" The following bar chart shows the prediction based on real time radomly generated input values listed
        in the table below:
        """)
        df = pd.DataFrame({"Unreinforced HDD overbend":round(pred_unreinforced[0][0],2),
                        "Reinforced HDD overbend":round(pred_reinforced[0][0],2)},index=['Unreinforced','Rreinforced'])
        # randomly generated imput variables
        FO = ['Circumferential','Longitudinal','Multi-directional'][fibre_orientation]
        df_input = pd.DataFrame({'Value':[diameter_over_thickness,pressure,CFRP_thickness]},
        index=['D/t ratio','internal pressure (MPa)','CFRP thickness (mm)'])
        df_FO = pd.DataFrame({"Type":['Circumferential','Longitudinal','Multi-directional'][fibre_orientation]},index=['Fibre orientation'])
        col1,mid,col2 = st.columns([1,0.1,2])
        with col1:
            st.write('\n')
            st.write('\n')
            st.table(df_input)
            st.table(df_FO)
        # plotting the bar chart
        fig, ax = plt.subplots(figsize=(6,4))
        with col2:
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
