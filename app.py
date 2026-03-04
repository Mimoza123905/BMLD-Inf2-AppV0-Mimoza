import streamlit as st

st.set_page_config(page_title="Meine App", page_icon=":material/home:")

pg_home = st.Page("views/home.py", title="Home", icon=":material/home:", default=True)
pg_second = st.Page("views/unterseite_a.py", title="Unterseite A", icon=":material/info:")
pg_add = st.Page("views/addieren.py", title="Addieren", icon=":material/calculator:")
pg_ph = st.Page("views/ph.py", title="pH Rechner", icon=":material/science:")

pg = st.navigation([pg_home, pg_second, pg_add, pg_ph])
pg.run()
