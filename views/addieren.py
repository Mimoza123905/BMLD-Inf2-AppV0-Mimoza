Import streamlit as st 
from fuctions.addieren Import add, substract 

st.titel("Addieren")

st. write ("Hier ist mein Rechner") 

with st.form ("addieren_form"):
    nummer_1 = st.number_Input()
    nummer_2 = st.number_Input()
    resultat = add(number_1, number_2)

    submit = st.form_submit_button("Berechnen")
    if submit:
        st.write(resultat)
        