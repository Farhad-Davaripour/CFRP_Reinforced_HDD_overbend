import streamlit as st
import streamlit_authenticator as stauth
import pandas as pd
st.markdown("""The synthetic dataset is generated from multiple finite element analyses. Please contact 
Farhad Davaripour on his [Linked-in profile]("https://www.linkedin.com/in/farhad-davaripour/") if you wish to review the dataset.""")
###
# names = ['Farhad Davaripour']
# usernames = ['fd7385']
# passwords = ['4562193IRANsaze']
# hashed_passwords = stauth.Hasher(passwords).generate()
# authenticator = stauth.Authenticate(names,usernames,hashed_passwords,
#     'some_cookie_name','some_signature_key')
# name, authentication_status, username = authenticator.login('Login','main')
# if authentication_status:
#     authenticator.logout('Logout', 'main')
#     st.write('Welcome *%s*' % (name))
#     st.write('I should find a way to show the data in here.')
#     # pd.read_excel()
# elif authentication_status == False:
#     st.error('Username/password is incorrect')
# elif authentication_status == None:
#     st.warning('Please enter your username and password')
