import streamlit as st
# st.set_page_config(
#     page_title="StockX",
#     layout = 'wide'
#     ,page_icon="/Users/gourangaghosh/files/final year oroject/images/line-chart-svgrepo-com.svg"
#     )
from datetime import date
import datetime as dt
import firebase_admin
from firebase_admin import credentials
from json.decoder import JSONDecodeError
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go
import plotly.express as px
from firebase_admin import auth
from firebase_admin import auth
if not firebase_admin._apps:
  cred = credentials.Certificate('stockx-2f1aa-30f869cd7b8f.json')
  deafult_app = firebase_admin.initialize_app(cred)
class SessionState:
        def __init__(self):
            self.email = None
            self.is_authenticated = False
def app(sessions_state):

    #reading the css file
    with open('/Users/gourangaghosh/files/final year oroject/land.css')as f:
        land_css = f.read()

    #display the image with css styling

    st.write(f'<style>{land_css}</style>', unsafe_allow_html=True)
    col1,col2 = st.columns([2,7])


    # this stuff is inside of a container
    with st.container():
        col1.image('/Users/gourangaghosh/files/final year oroject/images/StockX-3.png', caption=None, width=300)
        col1.header("Your one stop solution for stock analysis and future prediction")
        col1.markdown("Signup today to learn more", unsafe_allow_html=False)
        col2.image('/Users/gourangaghosh/files/final year oroject/images/landing_page_img.png',caption=None)

    #AUTHENTICATION

    def authentications(email):
        try:
            user = auth.get_user_by_email(email)
            sessions_state.email = user.email
            return user.uid
            
        except auth.UserNotFoundError:
            return None
            st.warning('login failed', icon=None)


    def login_callback(email):
        uid = authentications(email)
        if uid:
            sessions_state.is_authenticated = True
            st.sidebar.success('Login successful')
            print('is authenticated set to')
        else:
            st.sidebar.warning('Login failed')
        
    choice = st.sidebar.selectbox('login/signup',['Login','Signup'])

        

    if choice =='Login':
        email = st.sidebar.text_input('Please enter your email address')
        password = st.sidebar.text_input('please enter your password',type = 'password')
        Login = st.sidebar.button('Login' ,key="login_button",on_click =lambda: login_callback(email))

    else:
        email = st.sidebar.text_input('Please enter your email address')
        password = st.sidebar.text_input('please enter your password',type = 'password')
        user_name = st.sidebar.text_input('please input your user-name')
        submit = st.sidebar.button('Create my account')


        if submit:
            password = str(password)
            if len(password) <= 8:
                st.sidebar.warning('password must be at least 8 char ', icon=None)
            else:
                user = auth.create_user(email = email,password = password,uid = user_name)
                st.sidebar.success('your account created successfully', icon="✅")
                st.sidebar.success('you can now login', icon=None)

    # problem with the password recognition understood so far 
    # user = auth.create_user(email = email,password = password,uid = user_name) getting mixed up between the same 2 variable passwords
