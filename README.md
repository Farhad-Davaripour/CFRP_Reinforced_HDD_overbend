## An Application of Machine Learning to Predict the Peak Equivalent Stress Imposed on a CFRP Wrapped HDD Overbend
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/farhad-davaripour/cfrp_reinforced_hdd_overbend/main/my_app/Homepage.py)   

The present study is the continuation of the research work on the application of Carbon-Fiber-Reinforced Polymers (CFRP) wrap to enhance the mechanical behavior of pipe bends. The initial study was conducted on side bends subjected only to thermal expansion induced loads. The results derived from this study will be published on the ASCE Journal (Journal of Pipeline Systems - Engineering) and Practice. The paper is already accepted and is in the process of publication with the doi of [10.1061/(ASCE)PS.1949-1204.0000677](10.1061/(ASCE)PS.1949-1204.0000677).  

The present study examins the the application of CFRP wrap on Horizontal Directional Drilling (HDD) overbends subjected to combined loading (internal pressure and thermal expansion). Below figure demonstrates a schematic view of a pipeline partly constructed using HDD method, with the HDD overbend highlighted in the figure.

![Figure](https://github.com/Farhad-Davaripour/CFRP_Reinforced_HDD_overbend/blob/main/HDD-Schematic.png?raw=true)
   
Also, this study employs a data driven approach to predict the peak equivalent stress imposed on the reinforce HDD overbend. The data is generated usign finite element analyses by varying 4 characteristics including pipe's wall thickness, CFRP length, CFRP thickness, and Fibre orientation of the CFRP wrap. A dashboard is also developed using Streamlit library in python which demonstrates the impact of each feature variable on the peak equivalent stress that is imposed on the HDD overbend.
