import streamlit as st
st.markdown("""<b><h4 style='text-align:left;'>Overview:</h4></b>""", unsafe_allow_html=True)
st.write("""The following video provides a brief overview on how to use the dashbaord. Note that the video does not run on Mac
or IOS OS at this time.""")
video_file = open('https://github.com/Farhad-Davaripour/CFRP_Reinforced_HDD_overbend/blob/1c7a2b9c6f7ddeddf0b33e199f43b5e4f1179689/Introduction.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)