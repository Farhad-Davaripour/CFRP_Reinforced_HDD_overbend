## An Application of Machine Learning to Predict the Peak Equivalent Stress Imposed on a CFRP Wrapped HDD Overbend
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/farhad-davaripour/cfrp_reinforced_hdd_overbend/main/my_app/Homepage.py)   

The present study is the continuation of the research work on the application of Carbon-Fiber-Reinforced Polymers (CFRP) wrap to enhance the mechanical behavior of pipe bends. The initial study was carried out on side bends subjected only to thermal expansion induced loads, which is  being published in the ASCE Journal (Journal of Pipeline Systems - Engineering and Practice). The doi of the paper once published is as follows: [doi: 10.1061/(ASCE)PS.1949-1204.0000677](10.1061/(ASCE)PS.1949-1204.0000677)

The present study examins the the application of CFRP wrap on Horizontal Directional Drilling (HDD) overbends subjected to combined loading (internal pressure and thermal expansion). Below figure demonstrates a schematic view of a pipeline partly constructed using HDD method, with the HDD overbend highlighted in the figure.
<p align="center">
<img width="750" src="https://github.com/Farhad-Davaripour/CFRP_Reinforced_HDD_overbend/blob/main/images/HDD-Schematic.png?raw=true" alt="HDD overbend">
</p>
<p align="center">A schematic view of a pipeline partly constructed using HDD method</p>

Also, this study employs a data driven approach to predict the peak equivalent stress imposed on the reinforce HDD overbend. The data is generated usign finite element analyses by varying 5 characteristics including pipe's wall thickness, internal pressure, CFRP length, CFRP thickness, and Fibre orientation of the CFRP wrap. A dashboard is also developed using Streamlit library in python which demonstrates the impact of each feature variable on the peak equivalent stress that is imposed on the HDD overbend.
