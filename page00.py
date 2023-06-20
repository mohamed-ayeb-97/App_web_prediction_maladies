# Modules
import pyrebase
import streamlit as st
from Agile_project import ml

# Configuration Key
firebaseConfig = {
  'apiKey': "AIzaSyB63ItQ6FaGSxpX0G5pbdKwKo7NKUA9HaI",
  'authDomain': "agile-b9cb9.firebaseapp.com",
  'projectId': "agile-b9cb9",
  'databaseURL': "https://agile-b9cb9-default-rtdb.firebaseio.com/",
  'storageBucket': "agile-b9cb9.appspot.com",
  'messagingSenderId': "1061522388885",
  'appId': "1:1061522388885:web:922d6e410d6a9208e5689c"
};
# Firebase Authentication
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
# Database Authentication
db = firebase.database()
storage = firebase.storage()

st.title("E-HealthCare ML Web App")

# Authentication

choice = st.sidebar.selectbox('login/Signup', ['Login', 'Sign up'])

email = st.sidebar.text_input('Please enter your email')

password = st.sidebar.text_input('Please enter your password', type = 'password')

if choice == 'Sign up':

  handle = st.sidebar.text_input('Please input your app handle name', value='Default')
  submit = st.sidebar.button('Create my account')

  if submit:
    user = auth.create_user_with_email_and_password(email, password)
    st.success('Your account is created')
    # Sign up
    user = auth.sign_in_with_email_and_password(email, password)
    db.child(user['localId']).child("Handle").set(handle)
    db.child(user['localId']).child("ID").set(user['localId'])
    st.title('Welcome ' + handle)
    st.info('Login via login drop down selection')
if choice == 'Login':
  login = st.sidebar.checkbox('Login')
  if login:
    user = auth.sign_in_with_email_and_password(email, password)

    ml()
