import streamlit as st
st.markdown("""<b><h4 style='text-align:left;'>Overview:</h4></b>""", unsafe_allow_html=True)
st.write("""The following video provides a brief overview on how to use the dashbaord. Note that the video does not run on Mac
or IOS OS at this time.""")
with open('https://drive.google.com/file/d/1Wz0S8aJBeTT9ofpHSSQKm9XEmnsbLP9r/view?usp=sharing', 'rb') as video:
    st.video(video)