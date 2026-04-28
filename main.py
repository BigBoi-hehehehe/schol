import streamlit as st

st.title('Mooo')
st.write('Cow')

name = st.text_input('Name do: ')
age = st.number_input('Age do:')

if st.button('Submit'):
    st.write(f'Hello, {name}. Just leave :(')