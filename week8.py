import streamlit as st
st.title('Largest of 3 Numbers')
def maximum(a, b, c): 
    if (a >= b) and (a >= c): 
        return a 
    elif (b >= a) and (b >= c): 
        return b 
    else: 
        return c         
# Driven code 
a = st.number_input("First number: ")
b = st.number_input("Second number: ")
c = st.number_input("Third number: ")
st.write(maximum(a, b, c))
