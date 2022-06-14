import streamlit as st
st.subheader('Model Performance')
st.markdown(""" In the present study, the numerical investigation is carried out using a shell-beam based finite element (FE) model in Abaqus. The FE model comprises 
a combination of shell and beam elements where shell elements are employed to model the Horizontal Directional Drilling (HDD) overbend
and a few meters of its adjacent straight sections and the beam elements are employed to model the pipeline until the virtual anchor 
point. The beam and shell elements are constrained using the structural coupling method in Abaqus, which allows for radial deformation
 of the pipeline at the transition region from beam to shell elements.

The model development is carried out based on the following steps: (i) a shell-based model is built to replicate the physical test conducted 
by Skarakis et al. (2017) on a Carbon-Fiber-Reinforced Polymers (CFRP) wrapped pipe bend subjected to cyclic loadings, (ii) the pipe bend in 
the shell-based model is then altered to replicate a typical HDD overbend (i.e., the bend angle is modified to 12°), (iii) the shell-based model
 is extended using 1d beam elements to represent a pipeline. Note that only half of the pipeline is modelled, taking advantage of the 
 symmetry. More detail on the FE validation will be presented at the International Pipeline Conference (IPC2022)
in September 2022, in Calgary, Alberta.

**Reference:**   

Skarakis, I., Chatzopoulou, G., Karamanos, S. A., Tsouvalis, N. G., & Pournara, A. E. (2017). CFRP Reinforcement and Repair of Steel Pipe Elbows Subjected to Severe Cyclic Loading.
 Journal of Pressure Vessel Technology, 139(5). (Accepted).   

Davaripour Farhad, Roy Kshama, Maghoul Pooneh "Application of Carbon Fibre Reinforced Polymer Wrap on Horizontal Directional Drilling Overbends Under Combined Loading"
IPC 2022 (Accepted)
""")