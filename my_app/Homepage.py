import streamlit as st
st.markdown("""<b><h4 style='text-align:left;'>Overview:</h4></b>""", unsafe_allow_html=True)
st.write("""The following video provides a brief overview on how to use the dashbaord. Note that the video does not run on Mac
or IOS OS at this time.""")
video_file = open('https://github.com/Farhad-Davaripour/CFRP_Reinforced_HDD_overbend/blob/main/Introduction.mp4?raw=true', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)